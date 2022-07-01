"""
Standart Moduller
"""

"""
Moduler Programlama:
1- Kod tekraranı önler
2- Organizasyon (web, db, api...)
3- Bakımını ve Yönetimini
"""

"""
Modul: .py ile biten Ptyhon dosyalarına
Paket: Birçok modülü içeren Python klasörleridir
"""

"""
'import' edilerek kullanılır
"""

import math

# pi sayısı
pi_sayisi = math.pi
# print(pi_sayisi)

# import -> Python Interpreter sizin için o dosyayı buraya getirir

# Örnek
# random
import random

# random.random() -> 0 ile 1 arasında olaslık verir
olasilik = random.random()
# print(olasilik)

# 10 ile 50 arasında rasgele
rasgele_sayi = random.randint(10, 50)
# print(rasgele_sayi)

# liste'den rasgele eleman
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
eleman = random.choice(liste)
# print(eleman)

# örneklem almak istesek
orneklem = random.sample(liste, 3)
# print(orneklem)


"""
platform modülü
"""

import platform
# print('platform:', platform)
#
# # platform türü
# print('platform türü:', platform.platform())
#
# # platform mimarisi
# print('platform mimarisi:', platform.architecture())
#
# # makine tipi
# print('makine tipi:', platform.machine())
#
# # OS
# print('İşletim Sistemi:', platform.system())


"""
os
"""

import os

# print('os modulu:', os)
#
# # şu anda Python'un çalıştığı klasör
# print('mevcut klasör:', os.getcwd())
#
# print('kullanıcı:', os.getlogin())


"""
sys modülü
"""

import sys

# path değişkeni
# print('path:', sys.path)

yollar = sys.path

# for yol in yollar:
#     print(yol)

# sys.path -> Python'un modül ararken kullandığı sys.path

"""
bir modül import ederken adını değiştirmek isteyebiliriz.
alise
"""

import random as rnd

# print(rnd.random())

"""
tek seferde import
import a, b, c
"""

import random, sys, os


"""
Bir modülün bir parçasını import etmek:

from <modul_adi> import <modul_parcasi>

"""

from sys import modules
#print('hazır moduller:', modules)



# hem parçalı hem de alise edilmiş import
from math import sqrt as karakok

print('4 ün karakökü:', karakok(4))


"""
* ile import -> önerilmez
"""
from random import *
# name clash -> isim karşısı
















