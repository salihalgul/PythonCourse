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


# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Bu proje içindeki 'quiz_dosyalari' klasöründen bir zip (arşiv) dosyası yapalım.
Arşiv dosyamızın adı 'quiz_dosyalari_arsivi.zip' olsun.

İpuçları:
* shutil.make_archive()
"""

# Çözüm 10:


# --------------------------------------------------------------------------------------#