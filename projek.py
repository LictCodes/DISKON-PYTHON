import os  
Menu = [
   {
      "id" : 1,
      "nama" : "Roti Aoka", 
      "harga" : 2_000
   },
   {
      "id" : 2,
      "nama" : "Roma Kelapa", 
      "harga" : 7_000
   }, 
   {
      "id" : 3,
      "nama" : "Mie goreng", 
      "harga" : 20_000
   }, 
   {
      "id" : 4,
      "nama" : "Nextar", 
      "harga" : 20_000
   }, 
]

def displayMenu() -> None :
   print("="*45)
   for i in Menu:
      print(f"   {i['id']}. {i['nama']}")
      print(f"   Harga : {i['harga']}")  
   print("="*45)
   
def getProdukById(_id : int) -> list or bool:
   for i in Menu :
      if i["id"] == _id :
         return Menu[_id - 1]
   return False
def jumlahkanHarga(*args) -> int:
   jumlah = 0 
   for i in args:
      jumlah += i
   return jumlah 
   
   
   
TITLE_TOKO = "Toko Mang Lucas"


# Menampilkan menu 
os.system ("clear")
print("   "+TITLE_TOKO)
displayMenu() 


#mengambil pesanan 
pesanan = []
while True :
   pesan = ""
   cust = int(input("Pilih Nomor : ")) 
   for i in Menu :
      if i["id"] == cust :
         pesan_brp = int(input("Ingin  pesan berapa : "))
         for i in range(pesan_brp):
            pesanan.append(cust)
         pesan = ""
         break
      else :
         pesan = "Barang Tidak ada"
   if pesan  != "":
      print(pesan)
      continue
   # Lagi? 
   lagi = input("Ingin pesan Lagi? <y/n>  ")
   match lagi :
      case "y" :
         continue
      case "Y" :
         continue 
      case "n":
         break 
      case "N":
         break 
harga_ = []
for i in pesanan :
   harga_.append(getProdukById(i)["harga"])
print(f"barang yang di pesan : {len(pesanan)}")
harga_ = jumlahkanHarga(*harga_)
diskon = 0
if harga_ >= 100_000:
   diskon = 0.02 * harga_ 
elif harga_ >= 200_000 :
   diskon = 0.05 * harga_ 
elif harga_ >= 300_000 :
   diskon = 0.10 * harga_ 

jumlah_bayar = harga_ - diskon
print(f"Jumlah Bayar : {jumlah_bayar}")