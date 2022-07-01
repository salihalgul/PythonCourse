"""

try:
    ......
    ......
    ......

except Ex1:
    .....
    .....

except Ex2:
    .....

else:
    ......


Kod try içinde çalışırken, hata alırsa ilgili except bloğuna gelir.
Hata almazsa, (varsa) else bloğuna gelir.
"""

# Örnek

def dosya_ac(yol):
    try:
        dosya = open(yol, encoding='utf-8')
    except FileNotFoundError:
        print('Dosya bulunamadı...')
    else:
        print(dosya.read())

# yol = 'ornek.txt'
# dosya_ac(yol)



"""
Örnek:
Hata yakalandığında hata metni için -> standart hata metni (hatanın kendi metni)

except Exception as <degisken_adi>:

"""

def dosya_ac_standart_hata(yol):
    try:
        dosya = open(yol, encoding='utf-8')
    except FileNotFoundError as ex:
        print(ex)
    else:
        print(dosya.read())

yol = 'orneksss.txt'
# dosya_ac_standart_hata(yol)

"""
pass

Bazı durumlarda kodun hiçbirşey yapmadan devam etmesini isteriz -> pass

"""

# Örnek:
# exception anında hiçbir şey yapmasın
def dosya_ac_pass(yol):
    try:
        dosya = open(yol, encoding='utf-8')
    except FileNotFoundError as ex:
        pass
    else:
        print(dosya.read())

yol = 'orneksss.txt'
dosya_ac_pass(yol)
