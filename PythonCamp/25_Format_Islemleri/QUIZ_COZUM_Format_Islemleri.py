"""
 Format İşlemleri ile ilgili QUIZ - 10 Soru
"""

#--------------------------------------------------------------------------------------#

# Soru 1:
"""
Adı gun_adi olan bir fonksiyon yazın.
Fonksiyon kullanıcıdan bir gün istesin ve bu günün adını ve harf sayısını Tuple olarak dönsün:
Ör: ('Pazartesi, 9)

Bu fonksiyondan veriyi alıp, % operatorünü kullanarak şu şekilde ekrana yazdırın:
'Pazartesi gününün harf sayısı: 9'
"""

# Çözüm 1:
def gun_adi():
    gun = input("Lütfen bir gün adı giriniz: ")
    return (gun, len(gun))


# gun, harf_sayisi = gun_adi()
# print("%s gününün harf sayısı: %d" % (gun, harf_sayisi))

#--------------------------------------------------------------------------------------#

# Soru 2:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu str.format() fonksiyonunu kullanarak şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5' 
"""

# Çözüm 2:
# (gun, harf_sayisi) = gun_adi()
# print('gün: {0}, uzunluk: {1}'.format(gun, harf_sayisi))

#--------------------------------------------------------------------------------------#

# Soru3:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu f-strings kullanarak şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5'
"""

# Çözüm 3:
# (gun, harf_sayisi) = gun_adi()
# print(f"gun: {gun}, uzunluk: {harf_sayisi}")


#--------------------------------------------------------------------------------------#

# Soru 4:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu Template Strings ile şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5'
"""

# Çözüm 4:
from string import Template

# (gun, harf_sayisi) = gun_adi()
# sablon = Template("gun: $g, harf sayısı: $h")
# print(sablon.substitute(g=gun, h=harf_sayisi))

#--------------------------------------------------------------------------------------#

# Soru 5, 6, 7, 8, 9, 10 için aşağıdaki sözlüğü (dict) kullanınız:
baskent = {
    'Türkiye': 'Ankara',
    'Almanya': 'Berlin',
    'İngiltere': 'Londra',
    'ABD': 'Washington'
}

#--------------------------------------------------------------------------------------#

# Soru 5:
"""
baskent sözlüğünü ve % operatorünü kullanarak ekrana şu şekilde yazdırın:
"Türkiye'nin başkenti Ankara'dır"
Türkiye kelimesi sabit, Ankara değişken olacak.
"""
# Çözüm 5:
# s = "Türkiye'nin başkenti %(Türkiye)s dır." % baskent
# print(s)

#--------------------------------------------------------------------------------------#

# Soru 6:
"""
baskent sözlüğünü ve str.format() fonksiyonunu kullanarak ekrana şu şekilde yazdırın:
"Almanya'nın başkenti Berlin'dir"
Almanya ve Berlin kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 6:
# ulke = 'Almanya'
# s = "{0}'nın başkenti {1}'dir".format(ulke, baskent[ulke])
# print(s)

#--------------------------------------------------------------------------------------#

# Soru 7:
"""
baskent sözlüğünü ve f-strings kullanarak ekrana şu şekilde yazdırın:
"İngiltere'nin başkenti Londra'dır"
İngiltere ve Londra kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 7:
# ulke = 'İngiltere'
# s = f"{ulke}'nin başlenti {baskent[ulke]} dir."
# print(s)


#--------------------------------------------------------------------------------------#

# Soru 8:
"""
baskent sözlüğünü ve Template Strings kullanarak ekrana şu şekilde yazdırın:
"ABD'nin başkenti Washington'dır"
ABD ve Washington kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 8:
from string import Template

# ulke = 'ABD'
# s = Template("$u nun başkenti $b dir")
# print(s.substitute(u=ulke, b=baskent[ulke]))


#--------------------------------------------------------------------------------------#

# Soru 9:
"""
for döngüsü ve f-strings kullanarak baskent sözlüğü içindeki ülke-başkent ikililerini
şu şekilde ekrana yazdırın:
<başkent>, <ülke>nin başkentidir.

Ör: Ankara, Türkiye'nin başkentidir.
"""
# Çözüm 9:
# for ulke, sehir in baskent.items():
#     print(f"{sehir}, {ulke} nin başkentidir.")

# --------------------------------------------------------------------------------------#

# Soru 10:
"""
comprehension ve f-strings kullanarak baskent sözlüğü içindeki ülke-başkent ikililerini
şu şekilde ekrana yazdırın:
<başkent>, <ülke>nin başkentidir.

Ör: Ankara, Türkiye'nin başkentidir.
"""
# Çözüm 10:
print("--- Comprehension ---")
[
    print(f"{sehir}, {ulke} nin başkentidir.")
    for ulke, sehir in baskent.items()
]


# --------------------------------------------------------------------------------------#

