nama=input('nama anda : ')
jumlah_tiket=int(input('jumlah tiket yang di beli : '))
no_hp=int(input('masukan nomor telepon anda : '))
kode_jurusan=input('masukan kode jurusan : ')

if kode_jurusan=="SBY" or kode_jurusan=="sby":
    harga=300000
    nama_kota="surabaya"
elif kode_jurusan=="BL" or kode_jurusan=="bl":
    harga=350000
    nama_kota="bali"
elif kode_jurusan=="LMP" or kode_jurusan=="lmp":
    harga=500000
    nama_kota="lampung"
else :
    harga=0
    nama_kota="kota tidak di temukan"

if jumlah_tiket >= 3:
    potongan=int((harga*jumlah_tiket)*0.1)
else:
    potongan=0

total=int((harga*jumlah_tiket)-potongan)
print('---------------------------------------------------')
print('                PENJUALAN TIKET BUS')
print('                          XYZ')
print('---------------------------------------------------')
print('nama pembeli ', nama)
print('no Handphone ', no_hp)
print('kode jurusan yang di pilih ', kode_jurusan)
print('nama kota tujuan ',nama_kota)
print('harga ' ,harga)
print('jumlah beli ' , jumlah_tiket)
print('potongan yang di dapat ', potongan)
print('Total bayar ' ,total)
ubay=int(input('masukan uang bayar : '))
uli=ubay-total
print('uang kembali : ',uli)









