harga_telur=int(input('harga telur per kg : '))
berat_telur=int(input('beli telur per kg : '))
harga_angkot=int(input('harga naik angkot : '))
uang_ibu=int(input('uang ibu : '))

total_harga_telur=berat_telur*harga_telur
transport=harga_angkot * 2
total=total_harga_telur+transport
sisa_uang=uang_ibu-total
print('sisa uang ibu adalah '+str(sisa_uang))