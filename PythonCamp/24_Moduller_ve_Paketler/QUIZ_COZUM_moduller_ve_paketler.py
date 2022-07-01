"""
 Modüller ve Paketler ile ilgili QUIZ - 10 Soru
"""
# --------------------------------------------------------------------------------------#

# Soru 1:
"""
rasgele adında bir fonksiyon yaratın ve bu fonksiyon içinde random modülünü import edin.
Random modülü aracılığıyla 100 ile 200 arasında rasgele bir sayı yazdırın.

İpuçları:
* randint()
"""

# Çözüm 1:
def rasgele():
    import random
    rasgele_sayi = random.randint(100, 200)
    print(rasgele_sayi)

# rasgele()

# fonksiyon içinde import yaptığımız için dışarıda kullanamayız
# hata verir
# random.randint(100, 200)

# --------------------------------------------------------------------------------------#

# Soru 2:
"""
rasgele_liste adında bir fonksiyon yaratın ve bu fonksiyon içinde random modülünü 'rnd' adıyla import edin.
Fonksiyonunuz 10 elemanlı bir liste yaratsın.
Bu listenin elemanları random modülü aracılığıyla oluşturulsun ve değerleri 100 ile 200 arasında rasgele sayılar olsun.
Bu listeyi tek seferde print etsin.

Sonra yine random modülü aracılığyla bu sayılardan 4 tanesini rasgele olarak seçip print etsin.

İpuçları:
* randint()
* sample()
"""

# Çözüm 2:
def rasgele_liste():
    import random as rnd
    liste = []
    for i in range(10):
        rasgele_sayi = rnd.randint(100, 200)
        liste.append(rasgele_sayi)

    print(liste)

    secilenler = rnd.sample(liste, k=4)
    print(secilenler)


# rasgele_liste()

# --------------------------------------------------------------------------------------#

# Soru 3:
"""
os modülü aracılığıyla şu anda Python'un içinde çalıştığı klasör yolunu ekrana yazdırınız.

İpuçları:
* getcwd()
"""

# Çözüm 3:
import os

yol = os.getcwd()
# print(yol)


# --------------------------------------------------------------------------------------#

# Soru 4:
"""
Standart Python modüllerini kullanarak bilgisayarınızın
* İşletimi Sistemini
* İşlemcisini
ekrana yazdırın.

İpuçları:
* platform
"""

# Çözüm 4:
import platform

# OS
# print('İşletim Sistemi:', platform.system())

# İşlemci Adı
# print('İşlemci Adı:', platform.processor())


# --------------------------------------------------------------------------------------#

# Soru 5:
"""
sys modülü aracılığıyla, Python'un modülleri ararken baktığı yerler yani search path'i print edin.
Print ederken, liste ile içinde dönün ve tek tek satır olarak print edin.

İpuçları:
* path
"""

# Çözüm 5:
import sys

search_path = sys.path

# for path in search_path:
#     print(path)


# --------------------------------------------------------------------------------------#

# Soru 6:
"""
İçinde bulunduğunuz proje içerisinde 'sessiz' adında bir modül yaratın.
Bu modülün içinde 'sessiz_harfler' adında bir fonksiyon olsun.
Bu fonksiyon parametre olarak aldığı metin (str) içersindeki sessiz harfleri Set (küme) olarak geri dönsün.
Siz de bu sessiz harfler kümesini ekrana yazdırın.

İpuçları:
* modülünüz geriye bir hata dönmemek için kendi exception handling'ini (hata yönetimini) kendisi yapsın.

Örnek Çağrılma:
'Bir berber bir berbere bre berber ... /@*-'

Sonuc:
{'b', 'r', 'B'}
"""

# Çözüm 6:
# önce modülümüzü yaratalım -> sessiz.py
# import edelim

import sessiz

metin = 'Bir berber bir berbere bre berber ... /@*-'
sessizler = sessiz.sessiz_harfler(metin)
# print(sessizler)

# --------------------------------------------------------------------------------------#

# Soru 7:
"""
İçinde bulunduğunuz proje içerisinde 'quiz_modulleri' adlı bir klasör (folder) yaratın.
Bu klasör içinde adı 'sesli' olan bir modül olsun.
Bu modülün içinde 'sesli_harfler' adında bir fonksiyon olsun.
Bu fonksiyon parametre olarak aldığı metin (str) içersindeki sesli harfleri Set (küme) olarak geri dönsün.
Siz de bu sesli harfler kümesini ekrana yazdırın.

İpuçları:
* modülünüz geriye bir hata dönmemek için kendi exception handling'ini (hata yönetimini) kendisi yapsın.
* sys.path'i inceleyin

Örnek Çağrılma:
'Bir berber bir berbere bre berber ... /@*-'

Sonuc:
{'e', 'i'}
"""

# Çözüm 7:
# önce klasörümüzü ve modülümüzü yaratalım -> sesli.py

# direk erişemem -> ModuleNotFoundError: No module named 'sesli'
# import sesli

# import sys
# for path in sys.path:
#     print(path)

# Moduler_Paketler\venv\lib\site-packages içinde 'sesli.py' modülümüzü yerleştirelim
import sesli

metin = 'Bir berber bir berbere bre berber ... /@*-'
sesliler = sesli.sesli_harfler(metin)
# print(sesliler)

# --------------------------------------------------------------------------------------#

# Soru 8:
"""
İçinde bulunduğunuz proje içerisinde 'quiz_paketleri' adlı bir Python Paketi yaratın.
Bu paket içinde Soru 6'da yarattığınız 'sessiz', ve Soru 7'e yarattığınız 'sesli' modülleri olsun.
Bu proje içinden o paketi çağırın ve iki modül içindeki iki fonksiyonu (sessiz_harfler, sesli_harfler) çağırıp kullanın.

İpuçları:
* Python'da paket yaratma (__init__.py)
* ortak kullanılan yapıları global değişken olarak tek yerde yazma

Örnek Çağrılma:
'Bir berber bir berbere bre berber ... /@*-'

Sonuc:
sessiz_harfler('Bir berber bir berbere bre berber ... /@*-') -> {'b', 'r', 'B'}
sesli_harfler('Bir berber bir berbere bre berber ... /@*-') -> {'e', 'i'}
"""

# Çözüm 8:
# paketimizi yaratalım
# sessiz ve sesli modüllerini içine kopyalayalım

# şimdi import edelim
import quiz_paketleri


metin = 'Bir berber bir berbere bre berber ... /@*-'
sessiz_harfler = quiz_paketleri.sessiz.sessiz_harfler(metin)
# print(sessiz_harfler)

from quiz_paketleri import sesli
sesli_harfler = sesli.sesli_harfler(metin)
# print(sesli_harfler)

# --------------------------------------------------------------------------------------#

# Soru 9:
"""
Soru 8'de oluşturduğumuz 'quiz_paketleri' isimli paketimizi kopyalayalım ve 
bu bilgisayardaki tüm Python ortamlarının erişebileceği bir hale getirelim.
Yeni paketimizin adı 'sesli_sessiz_harfler' olsun.

İpuçları:
* Python'da paketi tüm Python ortamı için ortak hale getirme
* sys.path ile search path'i inceleyin
* eğer Python'un bilgisayarınızda nerede kurulu olduğunu bilmiyorsanız 
    * command prompt (cmd) -> where python
      bu komut size Python'un nerede kurulu olduğunu gösterir.  

Örnek Çağrılma:
'Bir berber bir berbere bre berber ... /@*-'

Sonuc:
sessiz_harfler('Bir berber bir berbere bre berber ... /@*-') -> {'b', 'r', 'B'}
sesli_harfler('Bir berber bir berbere bre berber ... /@*-') -> {'e', 'i'}
"""

# Çözüm 9:

# from sys import path
# for p in path:
#     print(p)

import sesli_sessiz_harfler

metin = 'Bir berber bir berbere bre berber ... /@*-'
sesli_harfler = sesli_sessiz_harfler.sesli.sesli_harfler(metin)
print(sesli_harfler)

# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Python Modülleri ile ilgili aşağıdakilerden hangisi yanlıştır:

A- Python'da modül, .py ile biten sıradan bir Python dosyasıdır.
B- Python modülleri import anahtar kelimesi ile içeri alınırlar.
C- Python'da içinde birçok modül bulunan yapılara paket adı verilir
D- Python'da paket ile klasör birebir aynı şeydir. Bir Python paketi yaratmak için yeni bir klasör yaratmak yeterlidir.
"""

# Çözüm 10:
# Cevap D şıkkıdır.
# Python paketleri, standart klasörlere bezerler ama içlerinde __init__.py dosyası bulundururlar.
# Pyhon 3.3 öncesinde __init__.py mecburi
# 3.3'ten sonra artık mecburi değil.


# --------------------------------------------------------------------------------------#
