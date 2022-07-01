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



# rasgele_liste()

# --------------------------------------------------------------------------------------#

# Soru 3:
"""
os modülü aracılığıyla şu anda Python'un içinde çalıştığı klasör yolunu ekrana yazdırınız.

İpuçları:
* getcwd()
"""

# Çözüm 3:



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



# --------------------------------------------------------------------------------------#

# Soru 5:
"""
sys modülü aracılığıyla, Python'un modülleri ararken baktığı yerler yani search path'i print edin.
Print ederken, liste ile içinde dönün ve tek tek satır olarak print edin.

İpuçları:
* path
"""

# Çözüm 5:



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



metin = 'Bir berber bir berbere bre berber ... /@*-'
# sessizler = sessiz.sessiz_harfler(metin)
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



metin = 'Bir berber bir berbere bre berber ... /@*-'
# sesliler = sesli.sesli_harfler(metin)
# print(sesliler)

# --------------------------------------------------------------------------------------#

# Soru 8:
"""
İçinde bulunduğunuz proje içerisinde 'quiz_paketleri' adlı bir Python Paketi yaratın.
Bu paket içinde Soru 6'da yarattığınız 'sessiz', ve Soru 7'e yarattığınız 'sesli' modülleri olsun.
Bu porje içinden o paketi çağırın ve iki modül içindeki iki fonksiyonu (sessiz_harfler, sesli_harfler) çağırıp kullanın.

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



metin = 'Bir berber bir berbere bre berber ... /@*-'
# sessiz_harfler = quiz_paketleri.sessiz.sessiz_harfler(metin)
# print(sessiz_harfler)

# from quiz_paketleri import sesli
# sesli_harfler = sesli.sesli_harfler(metin)
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



metin = 'Bir berber bir berbere bre berber ... /@*-'
# sesli_harfler = sesli_sessiz_harfler.sesli.sesli_harfler(metin)
# print(sesli_harfler)

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



# --------------------------------------------------------------------------------------#
