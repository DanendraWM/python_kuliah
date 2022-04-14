# latihan 4
gaji=5000000
produk_terjual=int(input('produk terjual : '))
harga_satuan=int(input('harga satuan : '))
omset=produk_terjual*harga_satuan
if produk_terjual > 100:
    bonus=int(omset*0.2)
    total=int(gaji+bonus)
else:
    bonus=int(omset*0.1)
    total=int(gaji+bonus)

print('produk yang terjual '+str(produk_terjual))
print('harga satuan '+str(harga_satuan))
print('bonus salesman '+str(bonus))
print('Gaji salesman '+str(gaji))
print('Total Gaji salesman '+str(total))
