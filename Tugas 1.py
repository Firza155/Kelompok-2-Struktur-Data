print ("===SELAMAT DATANG DI RESTORAN KAMI===\n")
print (""" Nama Kelompok: 
       1. FIRZA MUSHERMANSYAH (23091397155)
       2. UMAR FARUQ (23091397157)
       3. PINGKY DWI SAFITRI (23091397172)
""")

#LinkedList dari Keranjang
class Keranjang :
    def __init__(self, menu, harga, next = None):
        self.menu = menu
        self.harga = harga 
        self.next = next

#LinkedList dari Keranjang_Saya
class Keranjang_Saya : 
    def __init__(self, menu, harga):
          self.head = Keranjang(menu, harga)
    
    #Fungsi untuk menambah pesanan
    def tambahkan_pesanan(self, menu, harga):
        keranjang = Keranjang (menu, harga, self.head)
        self.head = keranjang 
    
    #Fungsi untuk menampilkan pesanan
    def tampilkan_keranjang(self):
        keranjang = self.head

    #looping menampilkan menu dan harga pesanan 
        while keranjang:
            print (f"{keranjang.menu} : {keranjang.harga}")
            keranjang = keranjang.next

    #Fungsi untuk menotalkan harga semua pesanan
    def total_pesanan(self):
        total = 0
        
        keranjang = self.head
        #looping total harga pesanan yang ada dikeranjang 
        while keranjang:
            total += keranjang.harga
            keranjang = keranjang.next
        
        print(f"Total Harga Pesanan: Rp{total}")

#Array menu yang disediakan 
MENU = [["Mixue Ice Cream", 5_000], ["Boba Shake", 16_000], ["Mi Sundae", 14_000], ["Mi Ganas", 11_000], ["Creamy Mango Boba", 22_000]]

#daftar menu 
MIXUE_CABANG_MI =("""                               
===== DAFTAR MENU ===== 
1. Mixue Ice Cream: Rp5000
2. Boba Shake: Rp16000
3. Mi Sundae: Rp14000
4. Mi Ganas: Rp11000
5. Creamy Mango Boba: Rp22000
""")

print (MIXUE_CABANG_MI)

#Input user untuk memilih pesanan
pilih_menu = int(input ("tulis pesanan sesuai angka : ")) - 1
#untuk membaca array menu supaya user tidak salah input
keranjang_saya = Keranjang_Saya(MENU[pilih_menu ][0], MENU[pilih_menu ][1]) 

#menanyakan kepada user mau tambah pesanan atau tidak 
tambah_pesanan = input("Apakah tambahan pesanan? (y/t)")

#looping untuk input dari user
while True :
    #program jika user menginput "y"
    if tambah_pesanan == "y" :
       pilih_tambahan = int(input("Pesanan tambahan : ")) - 1
       #menambahkan pesanan kedalam keranjang 
       keranjang_saya.tambahkan_pesanan(MENU[pilih_tambahan][0], MENU[pilih_tambahan][1]) 
       tambah_pesanan = input("Apakah tambah pesanan? (y/t)")

    #program jika user menginput "t"
    else :
        #untuk menampilkan pesanan dan total harga
        keranjang_saya.tampilkan_keranjang()
        keranjang_saya.total_pesanan()
        break 
