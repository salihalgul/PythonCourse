"""
Dosya: file, byte dizisidir
"""

"""
Dosya Tipleri:
1- Binary Tipi
    * pdf, doc, jpg, png
    
2- Text Tipi
    * txt, xml, html, .py, .java
"""

"""
Encoding: Verinin byte yapısıdır -> nasıl tutulduğu

İki yaygın encoding şekli:
1- ASCII (128 karakter)
2- UNICODE (1.114.112 karakter)
"""

# Python'da dosya açmak için -> open()

# encoding vermeden
# file = open('kelimeler.txt')
# print(file.read())

# encoding vermedik -> ü : Ã¼
# encoding ile
# file = open('kelimeler.txt', encoding='utf-8')
# print(file.read())

# ÖNEMLİ: Açılmış bir dosya kapanmalıdır. -> close()
# file.close()



# Dosya Yoksa -> hata : FileNotFoundError
# file = open("kelimelersss.txt", encoding='utf-8')

# hata yönetimi
# try:
#     file = open("kelimeler.txt", encoding='utf-8')
# except:
#     print("Dosya bulunamadı")
# else:
#     print(file.read())
#     file.close()

"""
with
Context Manager
Dosya açma, okuma ve kapatma işlemlerini otomatik yapar
"""

# with open("kelimeler.txt", encoding='utf-8') as file:
#     icerik = file.read()
#     print(icerik)

# Eğer dosya yoksa -> with FileNotFoundError
# try:
#     with open("kelimelerss.txt", encoding='utf-8') as file:
#         icerik = file.read()
#         print(icerik)
# except:
#     print('Dosya bulunamadı...')


"""
Dosya Açma Şekilleri (Modlar):
* r: okuma (read)
* w: yazma (write)
* a: ekleme (append)
* x: yaratma (create)
* t: text dosyası formatında
* b: binary dosyası formatında
* +: update modu (read + write)
"""

# Örnek:
# r -> okuma
# with open('kelimeler.txt', mode='rt') as file:
#     data = file.read()
#     print(data)


# şimdi binary dosyası okuma
with open('python_logo.png', mode='rb') as resim:
    data = resim.read()
    print(data)


