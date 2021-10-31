#   Program Diskon  #
import secrets as randomday

print("""
|---------------------------------------------------|                                                   
|            Welcome to Our Restaurant              |
|      ======================================       |                                          
|---------------------------------------------------|                                                   
""")

print('\n================================================')
print("\n--------Silahkan pilih menu dibawah ini---------")
print('\n================================================')


print("""
|-----------------------------------------------------|
|                     Menu  Kami                      |
|              Food :                                 |
|            (a) Nasi Goreng           : Rp. 15000    |
|            (b) Mie Goreng            : Rp. 16000    |
|            (c) Beef Burger           : Rp. 25000    |
|            (d) Special Omelette      : Rp. 20000    |
|            (e) Spaghetti             : Rp. 22000    |
|-----------------------------------------------------|
|             Drink :                                 |
|           (1) Ice Tea                : Rp. 5000     |
|           (2) Soft Drink             : Rp. 8000     |
|           (3) Aqua                   : Rp. 4000     |
|           (4) Ice Coffee             : Rp. 9000     |
|           (5) Milkshake              : Rp. 15000    |
|-----------------------------------------------------|
""")

print('\n-------------------------------------------------')
print("Kami juga mempunyai ketentuan diskon yang berlaku. \nKetentuannya adalah sebagai berikut")
print('--------------------------------------------------')

print("\n=== DISKON ===")
print("""
1.) Diskon setiap Pembelian 3 Minuman atau lebih sebesar 10%
2.) Diskon setiap Pembelian 2 Makanan atau lebih sebesar 5% 
3.) Diskon apabila melakukan pembayaran melalui E-wallet sebesar 5%
4.) Diskon hari weekend sebesar 5%
5.) Diskon hari weekdays sebesar 10%
""")

#  Input Makanan  #
F = 1

FoodPrice = []
FoodList = []
print("==========================================")
print("Silahkan Pesan Makanan sesuai selera anda")
print("Ketik 'selesai' jika selesai memesan")
print("==========================================")

while F > 0:
    FoodOrder = input("Silahkan Pesan Makanan anda = ")
    if FoodOrder == 'Nasi Goreng' or FoodOrder == 'nasi goreng':
        hargaf = 15000
        FoodPrice.append(hargaf) 
        FoodList.append(FoodOrder)
    elif FoodOrder == 'Mie Goreng' or FoodOrder == 'mie goreng':
        hargaf = 16000
        FoodPrice.append(hargaf) 
        FoodList.append(FoodOrder)
    elif FoodOrder == 'Beef Burger' or FoodOrder == 'beef burger':
        hargaf = 25000
        FoodPrice.append(hargaf) 
        FoodList.append(FoodOrder)
    elif FoodOrder == 'Special Omelette' or FoodOrder == 'special omelette':
        hargaf = 20000
        FoodPrice.append(hargaf) 
        FoodList.append(FoodOrder)
    elif FoodOrder == 'Spaghetti' or FoodOrder == 'spaghetti':
        hargaf = 20000
        FoodPrice.append(hargaf) 
        FoodList.append(FoodOrder)
    elif FoodOrder == 'Selesai' or FoodOrder == 'selesai':
        print("Pesanan Diterima")
        break
    else:
        print("Menu tidak tercantum. \nMohon cek kembali pesanan anda")
        
TotalFoodPrice = sum(FoodPrice)

#  Input Minuman  #
D = 1

DrinkPrice = []
DrinkList = []
print("==========================================")
print("Silahkan Pesan Minuman sesuai selera anda")
print("Ketik 'selesai' jika selesai memesan")
print("==========================================")

while D > 0:
    DrinkOrder = input("Silahkan Masukkan Pesanan Minuman anda = ")
    if DrinkOrder == 'Ice Tea' or DrinkOrder == 'ice tea':
        hargad = 5000
        DrinkPrice.append(hargad) 
        DrinkList.append(DrinkOrder)
    elif DrinkOrder == 'Soft Drink' or DrinkOrder == 'soft drink':
        hargad = 8000
        DrinkPrice.append(hargad) 
        DrinkList.append(DrinkOrder)
    elif DrinkOrder == 'Aqua' or DrinkOrder == 'aqua':
        hargad = 4000
        DrinkPrice.append(hargad) 
        DrinkList.append(DrinkOrder)
    elif DrinkOrder == 'Ice Coffee' or DrinkOrder == 'ice coffee':
        hargad = 9000
        DrinkPrice.append(hargad) 
        DrinkList.append(DrinkOrder)
    elif DrinkOrder == 'Milkshake' or DrinkOrder == 'milkshake':
        hargad = 15000
        DrinkPrice.append(hargad) 
        DrinkList.append(DrinkOrder)
    elif DrinkOrder == 'Selesai' or DrinkOrder == 'selesai':
        print("Pesanan Diterima")
        break
    else:
        print("Menu tidak tercantum. \nMohon cek kembali pesanan anda")
      
TotalDrinkPrice = sum(DrinkPrice)

#   Pemilihan hari beli dilakukan secara acak  #
TotalHari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
HariBeli = randomday.choice(TotalHari)

#  Pengaplikasian Diskon Makanan Jika Beli >2  #
if len(FoodList) >= 2:
    print("\n=====================================")
    print("Pesanan Makanan Anda : ")
    for FL in FoodList:
        print(FL)
    print("Total Harga : Rp.", TotalFoodPrice)
    print("=======================================")

    print("Anda mendapat diskon sebesar 5% karena memesan 2 menu atau lebih. \nTerima Kasih telah menghamburkan uang disini")
    TotalFoodPrice = TotalFoodPrice - (5/100*TotalFoodPrice)
    print("Harga makanan anda menjadi = Rp.", TotalFoodPrice)
    print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
    print("==================================================================")

else:
    print("=========================================")
    print("Pesanan Makanan Anda : ")
    for FL in FoodList:
        print(FL)
    print("Total Harga : Rp.", TotalFoodPrice)
    print("Gak diskon ya bang karena pesen 1 doang")
    print("========================================")


#  Pengaplikasian Diskon Minuman Jika Beli >3  #
if len(DrinkList) >= 2:
    print("=====================================")
    print("Pesanan Minuman Anda : ")
    for DL in DrinkList:
        print(DL)
    print("Total Harga : Rp.", TotalDrinkPrice)
    print("=====================================")

    print("Anda mendapat diskon sebesar 10% karena memesan 3 menu atau lebih")
    TotalDrinkPrice = TotalDrinkPrice - (5/100*TotalDrinkPrice)
    print("Harga makanan anda menjadi = Rp.", TotalDrinkPrice)
    print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
    print("===================================================================")

else:
    print("=========================================")
    print("Pesanan Minuman Anda : ")
    for DL in DrinkList:
        print(DL)
    print("Total Harga : Rp.", TotalDrinkPrice)
    print("Gak diskon ya bang karena pesen 1 doang")
    print("=========================================")

TotalPrice = TotalFoodPrice + TotalDrinkPrice

#  Pengaplikasian Diskon Pembayaran  #
print("\n=======================================")
print("Silahkan Pilih Metode Pembayaran : ")
print("1. Uang Cash. \n2. Credit Card. \n3. e-wallet. \n4. Ngutang")
print("=======================================")
Metode = input("Saya Memilih = ")
if Metode == 'E-Wallet' or Metode == 'e-wallet':
    print("Hore Diskon Tambahan berhasil didapat Sebesar 5% ")
    TotalPrice = TotalPrice - (5/100 * TotalPrice)
    print("=================================================")

elif Metode == 'Ngutang' or Metode == 'ngutang':
    print("Mau dipukul apa gimana?")
    print("==========================")

else:
    print("================================")
    print("Total Harga : Rp.", TotalPrice)
    print("Gak diskon ya bang")
    print("================================")

#  Pengaplikasian Diskon Hari  #
print("\n==========================================================")
print("Eits, masih ada diskon tambahan. \nHari ini hari apa hayo")
if HariBeli == 'Sabtu' or HariBeli == 'Minggu':
    print("Hore, karena hari ini hari", HariBeli, "\nKamu dapat diskon tambahan sebesar 5%")
    TotalPrice = TotalPrice - (5/100*TotalPrice)
    print("Jadi total harga yang kamu bayar = Rp. ", TotalPrice)
    print("======================================================")

else:
    print("Hore, karena hari ini hari", HariBeli, "Kamu dapat diskon tambahan sebesar 10%")
    TotalPrice = TotalPrice - (10/100*TotalPrice)
    print("Jadi total harga yang kamu bayar = Rp. ", TotalPrice)
    print("terima kasih telah berbelanja!")
    print("===============================================================================")
    