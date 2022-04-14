nama=input('masukan nama karyawan : ')
golongan=input('masukan golongan jabatan [1/2/3] : ')
pendidikan=input('masukan pendidikan karyawan [SMA/D1/D3/S1] : ')
jam_kerja=int(input('masukan jam kerja karyawan : '))
gaji_pokok=int(input('masukan gaji karyawan : '))
if golongan == '1':
    tunjangan_jabatan = 0.05
elif golongan =='2':
    tunjangan_jabatan = 0.1
elif golongan=='3':
    tunjangan_jabatan = 0.15
else :
    tunjangan_jabatan = 0

if pendidikan == 'SMA':
    tunjangan_pendidikan = 0.025
elif pendidikan =='D1':
    tunjangan_pendidikan = 0.05
elif pendidikan=='D3':
    tunjangan_pendidikan = 0.2
elif pendidikan=='S1':
    tunjangan_pendidikan = 0.3
else :
    tunjangan_pendidikan = 0

if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else :
    lembur = 0
tunjangan_jabatan*=gaji_pokok
tunjangan_pendidikan*=gaji_pokok

total =int(gaji_pokok+tunjangan_jabatan+tunjangan_pendidikan+lembur)
print('karyawan bernama '+nama)
print('tunjangan jabatan Rp. '+str(tunjangan_jabatan))
print('tunjangan pendidikan Rp. '+str(tunjangan_pendidikan))
print('tunjangan Lembur Rp. '+str(lembur))
print('total gaji seluruh nya adalah Rp. '+str(total))

