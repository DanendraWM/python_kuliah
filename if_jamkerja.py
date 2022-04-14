gaji_pokok=int(input('masukan gaji pokok : '))
jam_kerja=int(input('masukan jam kerja : '))
tunjangan=0.2
pajak =0.1

if jam_kerja > 200:
    lembur= (jam_kerja - 200) * 20000
    tunjangan=int(gaji_pokok*tunjangan)
    pajak=int((gaji_pokok+tunjangan+lembur)*pajak)
    gaji=int(gaji_pokok+tunjangan+lembur-pajak)

else:
    lembur=0
    tunjangan=int(gaji_pokok*tunjangan)
    pajak=int((gaji_pokok+tunjangan+lembur)*pajak)
    gaji=int(gaji_pokok+tunjangan+lembur-pajak)


print('gaji pokok anda adalah ',str(gaji_pokok))
if lembur != 0 :
    print('lemburan anda : ',str(lembur))
print('jam kerja anda adalah : ',str(jam_kerja))
print('tunjangan anda adalah : ',str(tunjangan))
print('pajak anda adalah : ',str(pajak))
print('total keseluruhan yang anda dapatkan adalah : ',str(gaji))

