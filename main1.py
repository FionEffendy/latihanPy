def ganjil (a,b):
        for i in range (a,b+1):
            if i%2 == 1:
                print(i)
def genap (a,b):
        for i in range (a,b+1):
            if i%2 == 0:
                print(i)
while True:

    print("Menu Pilihan")
    print("1. Angka Ganjil")
    print("2. Angka Genap")
    print("3. Keluar")
    print("\nSilahkan Pilih Angka 1/2/3")

    masukkan =  int(input('\nMasukkan Angka : '))

    if masukkan == 1:
        a = int(input('masukkan angka awal : '))
        b = int(input('masukkan angka akhir : '))

        ganjil(a,b)
        print('\n')
    
    elif masukkan == 2:
        a = int(input('masukkan angka awal : '))
        b = int(input('masukkan angka akhir : '))

        genap(a,b)
        print('\n')

    elif masukkan == 3:
        exit("Menutup")

    else:
        print('Input tidak ada silahkan pilih angka 1/2/3')