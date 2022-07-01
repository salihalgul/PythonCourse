"""
try - except

try:
    ....
    ...............................
    ....
    ....
    ....
    ....
except:
    ...
    ...


try:
    - kodu çalıştırmaya çalışır
    - hata yoksa, try'in sonuna kadar gelir
    - hata varsa, kod try'dan çıkar
except:
    - eğer try içinde hata alınmışsa, except'e gelir
    - derleyici hata olan yereden except içine atlar
    - yani hatanın yakalandığı yer except bloğudur.
"""

# Örnek:

# hatanın yönetilmediği durum
def karesini_al():
    girdi = input("Lütfen bir tam sayı giriniz: ")
    sayi = int(girdi)
    print(sayi**2)

# karesini_al()


def karesini_hesapla_try():
    try:
        girdi = input("Lütfen bir tam sayı giriniz: ")
        sayi = int(girdi)
        print(sayi**2)
    except:
        print('Sayı girmediniz...')

# karesini_hesapla_try()


# kullanıcı sayı girmediği sürece, sayı istemeye devam et
def karesini_hesapla_try_again():
    try:
        girdi = input("Lütfen bir tam sayı giriniz: ")
        sayi = int(girdi)
        print(sayi**2)
    except:
        print('Sayı girmediniz...')
        karesini_hesapla_try_again()

# karesini_hesapla_try_again()




# Örnek:
# Olmayan bir dosya açmaya çalışalım
def dosya_ac(dosya_yolu):
    # dosya aç -> open()
    dosya = open(dosya_yolu)

    # satır satır
    for satir in dosya:
        print(satir.split())

# aynı klasör (dizin) içindeki bir dosyayı okumak için:
yol = 'diziler.txt'
# dosya_ac(yol)


# hata yönetimi ile dosya açma
def dosya_ac(dosya_yolu):
    try:
        # dosya aç -> open()
        dosya = open(dosya_yolu)

        # satır satır
        for satir in dosya:
            print(satir.split())
    except:
        print("Maalesef dosya bulunamadı...")


yol = 'dizilerrr.txt'
# dosya_ac(yol)

"""
Birden fazla hata olması durumu:
 * birden fazla except bloğu ile
"""

# Örnek:

def bolme_try():
    try:
        bolunen = int(input("Bölünen giriniz: "))
        bolen = int(input('Bölen giriniz: '))

        bolum = bolunen / bolen
        print(bolum)

    except ValueError:
        print('Tamsayı girmediniz...')

    except ZeroDivisionError:
        print('Bölen 0 olmamalı...')


bolme_try()
