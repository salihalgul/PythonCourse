"""
 Exception Handling (Hata Yönetimi) ile ilgili QUIZ - 10 Soru
"""
# --------------------------------------------------------------------------------------#

# Soru 1:
"""
Parametre olarak bir liste alan bir fonksiyon yazın. Adı "liste_mi" olsun.
Fonksiyonunuz gelen parametrenin list tipinde olup olmadığını kontrol etsin.
Eğer list tipinde değilse:
"Verilen parametre list tipinde değil" diye Exception fırlatsın.
Eğer list tipinde ise bir listeyi print etsin ve sonra pass geçsin.

İpuçları:
* assert
* pass
* try-except kullanmayın
"""

# Çözüm 1:



# liste_mi(('a', 'b', 'c'))
# liste_mi(['a', 'b', 'c'])

# --------------------------------------------------------------------------------------#

# Soru 2:
"""
Parametre olarak bir liste alan bir fonksiyon yazın. Adı "liste_toplami" olsun.
Fonksiyonunuz listenin içindeki sayıları toplasın.

Eğer toplama işleminde bir hata alırsa, kullanıcıya hatayı dönsün.
Eğer bir hata almazsa, toplam sonucunu kullanıcıya dönsün.

İpuçları:
* try-except
"""


# Çözüm 2:



# print(liste_toplami([1, 'b', 3]))
# print(liste_toplami([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Soru 3:
"""
Parametre olarak bir liste alan bir fonksiyon yazın. Adı "liste_toplami" olsun.
Fonksiyonunuz listenin içindeki sayıları toplasın.

Eğer toplama işleminde bir hata alırsa, kullanıcıya hatayı dönsün.
Eğer bir hata almazsa, toplam sonucunu kullanıcıya dönsün.

İpuçları:
* try-except-else
"""


# Çözüm 3:



# print(liste_toplami([1, 'b', 3]))
# print(liste_toplami([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Soru 4:
"""
Parametre olarak bir liste alan bir fonksiyon yazın.
Fonksiyonunuz listenin içindeki sayıları toplasın.
Eğer liste elemanı sayı değilse o elemanı toplama dahil etmesin.
Ama ekrana şu şekilde not düşsün:
"'x' elemanı sayı değil"

Fonksiyonunuzun adı "listedeki_sayilar_toplami" olsun, ve toplam sonucunu kullanıcıya dönsün.

İpuçları:
* try-except-else
* assert
* pass

Örnek Çağırma:
listedeki_sayilar_toplami([1, 'a', 'b', 3])

Beklenen Sonuç:
a elemanı sayı değil
b elemanı sayı değil
4
"""


# Çözüm 4:



# bu sefer her eleman için ayrı ayrı bakacağımız için try yapısını for döngüsünün içine koyacağız

# print(listedeki_sayilar_toplami([1, 'a', 'b', 3]))
# print(listedeki_sayilar_toplami([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Soru 5:
"""
Aşağıda gördüğünüz "toplam_like" fonksiyonu blog_yazilari listesi içindeki,
her bir blog yazısında (dict) yer alan Like değerlerini toplayacak. 
Ve toplam like sayısını dönecek.

Fakat bu fonksiyonda bir sorun var.
Eğer fonksiyonu bu haliyle çalıştırırsanız, hata verdiğini görürsünüz.

try-except-else yapısı kullanarak bu sorunu ortadan kaldırın ve fonksiyonunuz düzgün çalışsın.

İpucu:
* her bir blog dict'ini dikkatli inceleyin.


def toplam_like():
    blog_yazilari = [{'Resim': 4, 'Like': 20, 'Yorum': 12},
                     {'Like': 15, 'Yorum': 8, 'Paylaşma': 10},
                     {'Resim': 7, 'Yorum': 16, 'Paylaşma': 37},
                     {'Resim': 6, 'Like': 10, 'Yorum': 9}]

    toplam_like = 0

    for blog in blog_yazilari:
        toplam_like = toplam_like + blog['Like']

    return toplam_like

toplam_like_adedi = toplam_like()
print(toplam_like_adedi)
"""


# Çözüm 5:



# toplam_like_adedi = toplam_like()
# print(toplam_like_adedi)

# --------------------------------------------------------------------------------------#

# Soru 6:
"""
Bir fonksiyon yazın adı 'hesap_makinesi' olsun.
Kullanıcıdan bir işlem isteyen bir fonksiyon yazın.
Şu şekilde bir işlem olacak örneğin: 6 * 5

Sizin fonksiyonunuz verilen sayılara ve aradaki işleme göre, hesaplama yapsın ve şu şekilde dönsün.
6 * 5 = 30

Aradaki matematiksel işlem sadece 4 işlemden biri olabilir: +, -, *, / 

Fonksiyonunuz çalışırken olabilecek hatalar:
1- Kullanıcı araya boşluk koyarak 3 eleman vermemiş olabilir. 
    - Toplam eleman sayısını kontrol etmelisiniz.
2- Kullanıcı aradaki işlemi 4 işlemden başka bir sembol olarak girmiş olabilir.
    - İşlem sembölünü kontrol etmelisiniz
3- 1. ve 3. eleman birer sayı (float) olmak zorunda. En azından float olarak dönüşebilmeli.
    - 1. ve 3. eleman için float kontrolü yapmlasınız
4- Aradaki işlem bölme ise (/) o zaman 3. eleman sıfır (0) olmamalı
    - 3. eleman için 0 kontrolü yapmalısınız
    
Bu olasıklıları göz önünde bulundururak try-except-else yapısı ile hesap_makinesi fonksiyonunu yazınız.
"""


# Çözüm 6:



# sonuc = hesap_makinesi()
# print(sonuc)

# --------------------------------------------------------------------------------------#

# Soru 7:
"""
Bir fonksiyon yazın adı, 'bir_karakter_ver' olsun.
Kullanıcıdan klavyede bir karaktere basmasını isteyiniz.
Kullanıcının bastığı karakter:
    1- eğer bir sayı ise karesini dönün
    2- eğer bir harf ise büyük harfini dönün
    3- eğer harf ya da sayı değilse, karakterin kendisini dönün
    
try-except-else-finally yapısı kullanarak bu fonksiyonu yazın.
"""


# Çözüm 7:



# bir_karakter_ver()

# --------------------------------------------------------------------------------------#

# Soru 8:
"""
Parametre olarak bir liste ve bir index alan bir fonksiyon yazın. Adı 'indexteki_eleman' olsun.

Fonksiyonunuz bu index'teki elemanı liste içinde arasın.
Eğer bulamazsa, geriye IndexError exeption tipinin standart hatasını dönsün. (sadece raise etsin yani)
Eğer bulursa bulduğu elemanı dönsün.

try-except-else yapısı ile bu fonksiyonu yazın.
"""


# Çözüm 8:



# listem = ['x', 'y', 'z', 't']
# ind = 7
# sonuc = indexteki_eleman(listem, ind)
# print(sonuc)

# --------------------------------------------------------------------------------------#

# Soru 9:
"""
Dosya okuyan bir fonksiyon yazın. Adı 'dosya_oku' olsun. 
Parametre olarak dosya yolunu alsın.
Eğer dosya yoksa, hata dönsün. Hata türü standart hata olsun.
Eğer dosya varsa, okuyup ekrana yazsın.
Her durumda (finally) dosyayı kapatsın.

try-except-else-finally yapısı ile bu fonksiyonu yazın.

İpuçları:
* finally içerisinde, dosya kapatırken, hata almamak ek bir kontrol yazmanız gerekiyor.

Örnek Çağırma:
dosya_oku('dizler.txt')

Sonuc:
FileNotFoundError: [Errno 2] No such file or directory: 'dizler.txt'
"""


# Çözüm 9:



# olmayan bir dosya yolu ile çağıralım
# path = "dizler.txt"
# dosya_oku(path)

# olan bir dosya yolu ile çağıralım
# path = "diziler.txt"
# dosya_oku(path)

# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Elimizde, içinde diziler ve sezon sayıları olan bir dictionary olsun.

diziler = {
    'Game of Thrones ': 8,
    'Fargo': 4,
    'Dark': 3,
    'True Detective': 3,
    'Dogs of Berlin': 1,
    'The Crown': 6    
}

Bu sözlüğü kullanan ve adı 'dizi_iskencesi' olan bir fonksiyon yazın.
Kullanıcıdan bir dizi adı isteyesin. Eğer dizi bizim sözlüğümüzde yoksa, 
"Bu dizi yok. Lütfen tekrar dene."
diye hata dönsün ve tekrar tekrar sorsun.
Kullanıcı var olan bir dizi adı girmediği sürece program tamamlanmasın.

while döngüsü ve try-except-else-finally yapılarını kullanarak bu fonksiyonu yazın.
Kullanıcı döngüden kurtulduysa, şöyle yazın son olarak:
"Tebrikler. Kurtuldunuz :)"

İpucu:
Bilerek ve isteyerek sonsuz bir döngü kurun.
"""


# Çözüm 10:



# dizi_iskencesi()

# --------------------------------------------------------------------------------------#
