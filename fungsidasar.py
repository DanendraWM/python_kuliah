def sapa(nama):
    print(f"halo {nama}, Apa kabar ? ")

sapa("danendra")

def print_string( nama,usia ):
    print(nama)
    print(usia)


print_string(nama="wwwww",usia="15")


def default_param(nama,lokasi='jakarta'):
    print(nama)
    print(lokasi)

default_param("udin")

def penjumlahan(a,b):
    hasil=a+b
    return hasil

print(penjumlahan(100,100))