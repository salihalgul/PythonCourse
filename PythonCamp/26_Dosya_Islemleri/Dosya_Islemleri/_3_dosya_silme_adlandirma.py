"""
Python'da dosyaları:
* yeniden adlandırma (rename)
* silme
* yaratma

os modülü ile yapılır
"""

import os

# YENİDEN ADLANDIRMA -> rename()
# Örnek
# os.rename('silinecek.txt', 'silinmeden_once_rename.txt')

# dosya yoksa -> FileNotFoundError
# try:
#     os.rename('silinecek.txt', 'silinmeden_once_rename.txt')
# except:
#     print('dosya bulunamadı...')


# SİLME -> remove(), unlink()
# os.remove('silinmeden_once_rename.txt')

# dosya yoksa -> FileNotFoundError

# os.unlink('silinecek_unlink.txt')


# YARATMA -> open(...., mode='x')

# with open('silinecek_yanlis_encoding.txt', mode='x') as dosya:
#     dosya.write("Bu dosya open(mode='x') ile yaratıldı....")

# with open('silinecek.txt') as dosya:
#     print(dosya.read())

"""
Encoding:
cp1254 -> Windows'un Türkçe Encoding formatı

OS encoding'leri ile uğraşmamak için -> open() işlemlerinde -> encoding='utf-8'
"""

with open('silinecek_dogru_encoding.txt', mode='x', encoding='utf-8') as dosya:
    dosya.write("Bu dosya open(mode='x') ile yaratıldı....")



