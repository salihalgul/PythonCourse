"""
 Dosya İşlemleri ile ilgili QUIZ - 10 Soru
"""

# --------------------------------------------------------------------------------------#

# Soru 1:
"""
Bu proje içinde 'quiz_dosyalari/flower_names.txt' dosyasını, Python ile açın, 
ve içindeki İngilizce çiçek isimlerini ekrana yazdırın.

İpuçları:
* os
* okuma modunda açın ('r')
"""

# Çözüm 1:
import os
yol = 'quiz_dosyalari/flower_names.txt'

# 1. Yol
# with open(yol) as dosya:
#     cicekler = dosya.read()
#     print(cicekler)

# 2. Yol
# with open(yol, mode='r') as dosya:
#     for cicek in dosya:
#         # \n yerine end=''
#         print(cicek, end='')

# --------------------------------------------------------------------------------------#

# Soru 2:
"""
Bu proje içinde 'quiz_dosyalari/flower_names.txt' dosyasını, Python ile açın,
ve içindeki İngilizce çiçek isimlerine aşağıdaki ismi de ekleyin.
Sonra da tüm içeriği ekrana yazdırın.

'Z: Zinnia elegans'

İpuçları:
* os
* append (ekleme) modunda açın ('a')
"""

# Çözüm 2:
import os
yol = 'quiz_dosyalari/flower_names.txt'
yeni_cicek = 'Z: Zinnia elegans'

# with open(yol, mode='a') as dosya:
#     # önce boş satır yaz
#     dosya.write('\n')
#
#     # şimdi yeni çiçeği ekle
#     dosya.write(yeni_cicek)

# --------------------------------------------------------------------------------------#

# Soru 3:
"""
Bu proje içinde 'quiz_dosyalari/quiz_silinecek.txt' adında bir dosya yaratın.
Ve bu dosyanın içine:
'bu dosya quiz içinde silienecek.' 
şeklinde bir satır ekleyin.

İpuçları:
* os
* yaratmak için -> mode='x'
* encoding
"""

# Çözüm 3:
import os
yol = 'quiz_dosyalari/quiz_silinecek.txt'

# with open(yol, mode='x', encoding='utf-8') as dosya:
#     dosya.write('bu dosya quiz içinde silienecek.')
#     print(dosya)

# --------------------------------------------------------------------------------------#

# Soru 4:
"""
Soru 3'te yarattığınız 'quiz_dosyalari/quiz_silinecek.txt' adındaki dosyayı Python ile silin.
Eğer dosya yoksa, hata verecektir. O yüzden bunu da Exception Handling ile yönetin.

İpuçları:
* os
* try-except
* silmek için -> os.remove()
"""

# Çözüm 4:
import os
yol = 'quiz_dosyalari/quiz_silinecek.txt'

# try:
#     os.remove(yol)
# except:
#     print('Böyle bir dosya yok...')


# --------------------------------------------------------------------------------------#

# Soru 5:
"""
Bu proje dosyası içindeki tüm nesnelerin (klasör, dosya vb.) listesini 
(sadece adları yeterli) aşağıdaki 3 yöntemle alın:
1- os.listdir()
2- os.scandir()
3- pathlib.Path.iterdir()

İpuçları:
* os
* pathlib
"""

# Çözüm 5:
import os
from pathlib import Path

# 1. Yol
# for icerik in os.listdir():
#     print(icerik)

# 2. Yol
# for icerik in os.scandir():
#     print(icerik.name)

# 3. Yol
# for icerik in Path('.').iterdir():
#     print(icerik.name)


# --------------------------------------------------------------------------------------#

# Soru 6:
"""
Bu proje içindeki 'quiz_dosyalari' klasörü altında aşağıdaki klasör ağacını yaratın:

- quiz_dosyalari
    - alt klasör 1
        - en alt klasör 1
        - en alt klasör 2
    - alt klasör 2
    - alt klasör 3
        - en alt klasör 3

Hepsini teker teker os.mkdir() ile yaratın.

İpuçları:
* os
* os.mkdir()
"""

# Çözüm 6:
import os

# os.mkdir('quiz_dosyalari/alt klasör 1')
# os.mkdir('quiz_dosyalari/alt klasör 1/en alt klasör 1')
# os.mkdir('quiz_dosyalari/alt klasör 1/en alt klasör 2')
#
# os.mkdir('quiz_dosyalari/alt klasör 2')
#
# os.mkdir('quiz_dosyalari/alt klasör 3')
# os.mkdir('quiz_dosyalari/alt klasör 3/en alt klasör 3')


# --------------------------------------------------------------------------------------#

# Soru 7:
"""
Bu proje içindeki 'quiz_dosyalari' klasörü altında aşağıdaki klasör ağacını yaratın:

Klasörleri üzerlerinde parantez içinde yazılı yöntemlerle yaratın.

- quiz_dosyalari

    (os.makedirs)
    - alt klasör 10
        - en alt klasör 10
        - en alt klasör 20
    
    (pathlib.Path.mkdir)
    - alt klasör 20
    
    (pathlib.Path.mkdir)
    - alt klasör 30
        - en alt klasör 30
        
Eğer klasör önceden varsa 'FileExistsError' hatası vermesin.

İpuçları:
* os
* os.makedirs()
* pathlib.Path.mkdir()
* exist_ok=True
"""

# Çözüm 7:
import os
from pathlib import Path

# os.makedirs('quiz_dosyalari/alt klasör 10/en alt klasör 10', exist_ok=True)
# os.makedirs('quiz_dosyalari/alt klasör 10/en alt klasör 20', exist_ok=True)
#
# # Path().mkdir()
# Path('quiz_dosyalari/alt klasör 20').mkdir(exist_ok=True)
# Path('quiz_dosyalari/alt klasör 30/en alt klasör 30').mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------------------#

# Soru 8:
"""
Bu proje klasörü içinde ismi '*a*d*.py' desenine uyan tüm dosyaları (file) bulunuz.
Hem dosya listesini alırken hem de yazdırırken, for döngüsü yerine comprehension kullanınız.

İpuçları:
* os
* os.scandir()
* os.getcwd()
* fnmatch
"""

# Çözüm 8:
import os
import fnmatch

desen = '*a*d*.py'

# dosyalar = [dosya.name
#             for dosya in os.scandir()
#             if dosya.is_file() and fnmatch.fnmatch(dosya.name, desen)]
#
# # print(dosyalar)
#
# [print(d) for d in dosyalar]

# --------------------------------------------------------------------------------------#

# Soru 9:
"""
Bu proje içindeki 'quiz_dosyalari' klasörü içinde adında '1' rakamı geçen,
tüm dosya ve klasörleri siliniz.

Projenin ana klasör yolu ile (os.getcwd) ile 'quiz_dosyalari' adını birleştirip (os.path.join),
arama yapacağınız yolu oluşturun.

Bulma ve silme işlemini tek comprehension içinde yapınız.

İpuçları:
* shutil.rmtree()
* os.getcwd()
* os.path.join()
"""

# Çözüm 9:
import shutil

proje_klasoru = os.getcwd()

arama_klasoru = os.path.join(proje_klasoru, 'quiz_dosyalari')
# print(arama_klasoru)

desen = '*1*'

# önce desene uyanları bul
# [print(icerik.name)
#     for icerik in os.scandir(arama_klasoru)
#     if fnmatch.fnmatch(icerik.name, desen)]
#
# # comprehension içinde shutil ile sil
# [shutil.rmtree(icerik)
#     for icerik in os.scandir(arama_klasoru)
#     if fnmatch.fnmatch(icerik.name, desen)]

# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Bu proje içindeki 'quiz_dosyalari' klasöründen bir zip (arşiv) dosyası yapalım.
Arşiv dosyamızın adı 'quiz_dosyalari_arsivi.zip' olsun.

İpuçları:
* shutil.make_archive()
"""

# Çözüm 10:
import shutil

shutil.make_archive('quiz_dosyalari_arsivi', 'zip', 'quiz_dosyalari')


# --------------------------------------------------------------------------------------#