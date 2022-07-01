"""
Klasör Yaratma:
1- os.mkdir()
    * mkdir() -> tek klasör yaratır
    * makedirs() -> birden fazla klasör yaratır

2. path.Path.mkdir() -> hem tekli hem de çoklu klasör yaratır.
"""

# TEKLİ KLASÖR YARATMA
import os
from pathlib import Path

# ana klasör yolu
ana_klasor_yolu = os.getcwd()

# Örnek:

# 1. Yol -> os.mkdir()

# dosya zaten var -> FileExistsError
# os.mkdir('ornek_klasor_1')

# os.mkdir('ornek_klasor_2')


# 2. Yol -> pathlib.Path.mkdir()
# p = Path('path_klasoru_1')
# p.mkdir()

# try:
#     p2 = Path('path_klasoru_2')
#     p2.mkdir()
# except FileExistsError as dosya_var_hatasi:
#     print(dosya_var_hatasi)


# BİRDEN FAZLA KLASÖR YARATMA
"""
 - seviye 1
    - seviye 2
        - seviye 3
"""

# 1. Yol -> os.makedirs()

# exist_ok
os.makedirs('seviye_1/seviye_2/seviye_3', exist_ok=True)

# 2. Yol -> pathlib.Path.mkdir()

# parents=True
p3 = Path('path_seviye_1/path_seviye_2/path_seviye_3')
# p3.mkdir(parents=True)

# exist_ok
p3.mkdir(parents=True, exist_ok=True)
