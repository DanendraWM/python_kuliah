kode_baju=input('masukan kode baju [SP/AD] : ')
ukuran=input('Masukan ukuran baju [S/M] : ')

if kode_baju == "SP" or kode_baju == "sp":
    merek="superDry"
    if ukuran == "M" or ukuran == "m":
        harga=450000
    elif ukuran == "S" or ukuran == "s":
        harga=500000
    else : 
        harga=0
elif kode_baju =="AD" or kode_baju == "ad":
    merek="adidas"
    if ukuran == "M" or ukuran == "m":
        harga=650000
    elif ukuran == "S" or ukuran == "s":
        harga=700000
    else : 
        harga=0
else:
    merek="merek tidak ada"
    harga=0


print('==========================')
print('merek baju : ', merek)
print('harga baju : Rp. ', str(harga))
