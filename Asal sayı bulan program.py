print("""
Şimdi asal mı fonksiyonunu while döngüsünün içinde kullanarak asal sayı bulan programı oluşturacağız.

""")


def asalmi (sayi):
    if  sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = int(input("Sayı Giriniz:"))
    if (asalmi (sayi)):
        print(sayi,"Asaldır")
    else:
        print(sayi,"Asal Değildir")
