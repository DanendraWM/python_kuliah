bilangan=int(input('masukan bilangan prima : '))

for i in range(2,bilangan):
    if bilangan % i == 0 :
        print('bukan bilangan prima')
        break
    else :
        print('bilangan prima')