"""
% Operatoru
- %s -> string
- %d -> integer
- %f -> float
    - %.<n>f -> sıfırdan sonra n hane
"""

import math

gun = 'Pazartesi'
print('Bugün günlerden %s' % gun)

sayi = 28
print("Euclid'e göre %d bir mükemmel sayıdır." % sayi)

pi = math.pi
metin = "pi sayısı: %.4f" % pi
print(metin)

# birden fazla % operatoru
bilgi = "Python, ilk olarak %d'de yayınlandı ve %.2f yıldan fazladır kullanılıyor" % (1991, 30)
print(bilgi)

# Tuple olarak % operatörü kullanılır
veri = ("Peter", "Parker", 28)
soru = 'Selam %s %s. Senin yaşın, %d, değil mi?'
print(soru % veri)

# Dictionary ile
dosya = {
    "path": "./com/pyt",
    "version": 1.8,
    "author": "Joker"
}
bilgi = "Adres'i '%(path)s' olan, %(version).1f versiyonlu dosyayı %(author)s yazmıştır." % dosya
print(bilgi)




















