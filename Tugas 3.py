print (""" Nama Kelompok: 
       1. FIRZA MUSHERMANSYAH (23091397155)
       2. UMAR FARUQ (23091397157)
       3. PINGKY DWI SAFITRI (23091397172)
""")

#class node 
class Peta:
    #metode init (inisiasi)
    def _init_(self):
        self.daftarKota = {}
    
    #metode tambahKota untuk menambah kota
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {} 
    
    #metode printKota untuk menampilkan kota
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")
    
    #metode tambahJalan untuk menambah jarak
    def tambahJalan(self, kota1, kota2, jarak):
        #jika kota1 dan kota2 ada di dalam daftarKota maka ditambahkan jaraknya
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    #metode hapusKota untuk menghapus kota yang di dalam list daftar kota
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
    
    #metode hapusJalan untuk menghapus jarak yang udah ada di dalam list daftar kota
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

    #metode ruteTempuh untuk menampilkan jarak tempuh dari kota1 ke kota2
    def ruteTempuh(self, kota1, kota2):
        #untuk memanggil metode dijkstra
        [daftar_jarak, daftar_rute] = self.dijkstra(kota1)
        #jika kota1 dan kota2 didalam daftarKota maka menampilkan jaraknya  
        if kota1 and kota2 in self.daftarKota: 
            #jika tidak ada yang menghubungkan kota1 ke kota2
            if not (kota1 in daftar_jarak or kota2 in daftar_jarak):
                #maka akan muncul harus memasukkan sesuai daftar kota
                print("kamu harus memasukkan sesuai daftar kota") 
            else :
                print("jarak tempuh yang ditempuh", daftar_jarak[kota2], "Km")
                print("kamu harus melewati kota", daftar_rute[kota2])
        #jika user menempuh antar kota yang tidak sesuai dengan daftar kota 
        else :
            print ("kamu harus melewati beberapa kota")

    #metode dijkstra untuk menampilkan untuk mencari keseluruhan rute dan total jarak yang ditempuh    
    def dijkstra(self, kota_awal):
        #variabel untuk memproses semua daftar kota 
        kota_ingin_dikunjungi = [*self.daftarKota.keys()]
        daftar_jarak = {}
        daftar_rute = {}

        #fungsi untuk menentukan jarak maksimal untuk tiap rute
        for kota in kota_ingin_dikunjungi:
            daftar_jarak[kota] = float("inf")
        daftar_jarak[kota_awal] = 0
        
        while kota_ingin_dikunjungi:
            #looping untuk menentukan kota terdekat dari kota awal
            kota_terdekat = None
            for kota in kota_ingin_dikunjungi:
                if kota_terdekat == None:
                    kota_terdekat = kota
                elif daftar_jarak[kota] < daftar_jarak[kota_terdekat]:
                    kota_terdekat = kota

            #fungsi untuk menghitung total jarak dari kota terdekat ke kota yang dituju 
            for kota_tetangga, jarak in self.daftarKota[kota_terdekat].items():
                total_jarak = round(daftar_jarak[kota_terdekat] + jarak, 1)
                if total_jarak < daftar_jarak[kota_tetangga]:
                    daftar_jarak[kota_tetangga] = total_jarak
                    daftar_rute[kota_tetangga] = kota_terdekat

            #untuk menghapus kota yang telah dikunjungi
            kota_ingin_dikunjungi.remove(kota_terdekat)

        #untuk mengoutput variabel daftar jarak dan daftar rute 
        return daftar_jarak, daftar_rute
    
#variabel untuk list dari nama nama kota di peta uzbekistan
PetaUzbekistan = ["Almalyk", "Angren", "Pop", "Kokand", "Namangan", "Margilan", "Fergana", "Marhamat", "Asaka", "Andijan"]
#variabel untuk memanggil class
Uzbekistan = Peta() 
#untuk memasukkan nama kota di dalam class
for kota in PetaUzbekistan : 
    Uzbekistan.tambahKota(kota) 

#aturan untuk input nama kota
print("""
*HARAP MEMASUKKAN NAMA KOTA SESUAI DENGAN DAFTAR DI BAWAH (huruf besar dan huruf kecilnya)
      
=====DAFTAR KOTA=====
""")

#menambahkan jarak antar kota yang dilewati
Uzbekistan.tambahJalan("Almalyk", "Angren", 53)
Uzbekistan.tambahJalan("Angren", "Kokand", 134)
Uzbekistan.tambahJalan("Angren", "Pop", 125)
Uzbekistan.tambahJalan("Kokand", "Pop", 50.5)
Uzbekistan.tambahJalan("Kokand", "Margilan", 77)
Uzbekistan.tambahJalan("Kokand", "Fergana", 88.7)
Uzbekistan.tambahJalan("Pop", "Namangan", 58)
Uzbekistan.tambahJalan("Namangan", "Andijan", 69.2)
Uzbekistan.tambahJalan("Margilan", "Asaka", 54.8)
Uzbekistan.tambahJalan("Margilan", "Marhamat", 54.5)
Uzbekistan.tambahJalan("Marhamat", "Asaka", 24.3)
Uzbekistan.tambahJalan("Asaka", "Andijan", 24.9)

#memanggil metode printKota untuk menampilkan daftar kota
Uzbekistan.printKota()

# variabel untuk menginput lokasi saat ini
lokasi = input("lokasi anda sekarang : ").title()
#variabel untuk memilih lokasi yang di tuju
pilihlokasitujuan = input("tujuan yang ingin di tuju : ").title()
#menampilkan jarak tempuh dari kota lokasi ke kota 
