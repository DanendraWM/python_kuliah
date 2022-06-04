def welcome():
    while True:
        print("===========================================================")
        print("                Welcome To Oke Coffee                      ")
        print("                Ngopi di asik di sini                      ")
        print("===========================================================")
        print("1 - Lihat list Produk")
        print("2 - Keluar Dari Sistem")

        menu = int(input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))
        if menu == 1:
            lihatMenu()
            beliKopi()
        elif menu == 2:
            print("terima kasih telah berkunjung ke coffee")
            break
        else:
            print("inputan error")



list_beli = {}
list_menu={
    1:{
        "nama_menu":"latte",
        "harga":30000
    },
    2:{
        "nama_menu":"soto",
        "harga":23000
    }
}

def beliKopi():
    id = len(list_beli)+1
    id_menu=int(input('masukan id menu : '))
    if id_menu not in list_menu:
        print('maaf id tidak di temukan')
        beliKopi()
    nama=input('masukan nama pembeli : ')
    meja=int(input('masukan nomor meja : '))
    nama_menu=list_menu[id_menu]["nama_menu"]
    harga=list_menu[id_menu]["harga"]
    list_beli[id]={'nama_pembeli':nama,'meja':meja,'nama_menu':nama_menu,'harga':harga}
    print(f"{'id':<5} {'nama pembeli':<10} {'menu ':<10} {'harga':<10} {'meja':<10}")
    for beli in list_beli:
        id=beli
        nama=list_beli[id]['nama_pembeli']
        meja=list_beli[id]['meja']
        nama_menu=list_beli[id]['nama_menu']
        harga=list_beli[id]['harga']
        print(f"{id:<5} {nama:^10} {nama_menu:^10} {harga:^10} {meja:^10}")
    ulang=input("ingin memesan lagi (y/n): ").lower()
    if ulang == "y":
        beliKopi()
    else:
        checkout()
        list_beli.clear()


def lihatMenu():
    print(f"{'id':<7} {'nama menu':<10} {'harga':<10}")
    for menu in list_menu:
        id = menu
        nama_menu = list_menu[id]['nama_menu']
        harga = list_menu[id]['harga']
        print(f"{id:<5} {nama_menu:^10} {harga:^10}")

def checkout():
    print("===========================================================")
    print("                  Hasil checkout                           ")
    print("===========================================================")
    print(f"{'id':<5} {'nama pembeli':<10} {'menu ':<10} {'harga':<10} {'meja':<10}")
    for beli in list_beli:
        id=beli
        nama=list_beli[id]['nama_pembeli']
        meja=list_beli[id]['meja']
        nama_menu=list_beli[id]['nama_menu']
        harga=list_beli[id]['harga']
        print(f"{id:<5} {nama:^10} {nama_menu:^10} {harga:^10} {meja:^10}")
    print("===========================================================")
    total=0
    for beli in list_beli:
        total+=list_beli[beli]["harga"]
    print(f"TOTAL HARGA                   {total}")
    

welcome()