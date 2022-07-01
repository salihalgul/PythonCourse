"""
ARŞİV DOSYASI AÇMA
zipfile ile yapılır
"""

import zipfile
import os
import shutil

# for d in os.listdir():
#     print(d)

# hadi bu arsiv.zip dosyasını açalım
# arsiv = zipfile.ZipFile('arsiv.zip', 'r')
# print(arsiv)

# extract etmeden önce, içinde ne var bakalım
# süpriz :)
# for d in arsiv.filelist:
#     print(d.filename)

# şimdi extract edelim
# arsiv.extractall()

# arsiv'i kapat
# arsiv.close()


# ARŞİV DOSYASI YARATMA
# shutil.make_archive()
shutil.make_archive('yen_arsiv', 'zip', 'arsiv')

