"""
İki yol:
* String Metodları -> startswith, endswith, find
* fnmatch modülü
"""

import os
from pathlib import Path
import fnmatch

# Örnek
# String Metodları

# Arama Klasörü
# stringlerin içinde \ karakter varsa -> başına r harfi -> raw string
arama_klasoru = r'C:\Windows'

# önce bu dizinin içini görelim
# for k in os.listdir(arama_klasoru):
#     print(k)

# şimdi .exe olan dosyaları bulalım
# with Path(arama_klasoru) as klasor:
#     # klasor içindeki nesneler
#     for dosya in klasor.iterdir():
#         # tipi file mi? ve sonu .exe mi?
#         if dosya.is_file() and dosya.name.endswith('.exe'):
#             print(dosya.name)




# fnmatch modülü
# önerilen yöntem

desen = '*.exe'
with Path(arama_klasoru) as klasor:
    for dosya in klasor.iterdir():
        if dosya.is_file() and fnmatch.fnmatch(dosya.name, desen):
            print(dosya.name)




