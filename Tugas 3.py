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
#menampilkan jarak tempuh dari kota lokasi ke kota tujuan 
Uzbekistan.ruteTempuh(lokasi, pilihlokasitujuan)
