"""
Okuma - Yazma

Okuma Metodları:
* read() -> tüm dosyayı tek seferde oku
* readline() -> sadece tek satır okur, bir alt satıra geçer, bekler
* readlines() -> kalan tüm satırları okur
"""

# Okuma Örnekleri

# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     yazi = lorem.read()
#     print(yazi)

# ilk 50 karakter okuyalım
# with open('lorem_ipsum.txt', mode='r', encoding='utf-8') as lorem:
#     yazi_50 = lorem.read(50)
#     print(yazi_50)

# lorem ipsum dosyasını satır satır oku
# with open('lorem_ipsum.txt') as lorem:
#     satir_1 = lorem.readline()
#     print(satir_1)

# ilk iki satır oku
# with open('lorem_ipsum.txt') as lorem:
#     print(lorem.readline())   # 1. satır
#     print(lorem.readline())   # 2. satır  -> Ctrl + d

# bütün dosyayı satır satır readline ile oku
# with open('lorem_ipsum.txt') as lorem:
#     for satir in lorem:
#         print(satir)
#
# with open('lorem_ipsum.txt') as lorem:
#     for satir in lorem:
#         print(satir.split())  # \n karakterinden parçalar, sonra da ' ' karakterleri


"""
Yazma İşlemleri:
* w -> write : boş dosya olarak açar (dikkat)
* a -> append : mevcut dosyaya ekleme yapar
"""

# w ile aç
# with open('lorem_ipsum.txt', mode='w') as lorem:
#     lorem.write('yeni satır')

# a ile aç
# with open('lorem_ipsum.txt', mode='a') as lorem:
#     lorem.write('yeni satır')

# yeni satır \n ile ekle
# with open('lorem_ipsum.txt', mode='a') as lorem:
#     lorem.write('\nyeni satır 2222')

# tek seferde birden fazla satır ekle
with open('lorem_ipsum.txt', mode='a') as lorem:
    eklenecek_satirlar = ['\nEk Satır 1', '\nEk Satır 2', '\nEk Satır 3']
    lorem.writelines(eklenecek_satirlar)

