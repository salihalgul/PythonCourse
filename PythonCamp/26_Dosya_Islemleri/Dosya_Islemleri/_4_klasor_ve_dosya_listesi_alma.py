"""
Bir klasör içindeki tüm dosya ve klasörleri os modülü ile okuruz.
Bunların tipi:
 * dosya
 * klasör
"""

# ------- Tüm Klasör İçerini Okuma --------- #

# 1. Yol -> os.listdir()
import os

# okunacak klasör ->
dosya_yolu = os.getcwd()

icerik = os.listdir(dosya_yolu)
# print(icerik)
# for ic in icerik:
#     print(ic)


# 2. Yol -> os.scandir()
folder = os.scandir(dosya_yolu)
# for eleman in folder:
#     print(eleman)


# 3. Yöntem -> pathlib.Path.iterdir()
from pathlib import Path

icerik = Path(dosya_yolu)
# for ic_eleman in icerik.iterdir():
#     print(ic_eleman)


# ------- Klasör İçerideki Dosyaları Okuma --------- #

# 1. Yol -> os.listdir()
import os
icerik = os.listdir(dosya_yolu)
# for ic in icerik:
#     if os.path.isfile(ic):
#         print(ic)


# 2. Yol -> os.scandir()
# with os.scandir(dosya_yolu) as scans:
#     for scan in scans:
#         if scan.is_file():
#             print(scan)

# folder = os.scandir(dosya_yolu)
# for eleman in folder:
#     if eleman.is_file():
#         print(eleman)

# 3. Yöntem -> pathlib.Path.iterdir()
# from pathlib import Path
# ana_dosya = Path(dosya_yolu)
# dosya_icerigi = ana_dosya.iterdir()
#
# for dos in dosya_icerigi:
#     if dos.is_file():
#         print(dos)


# ------- Klasör İçerideki Klasörleri Okuma --------- #

# 1. Yol -> os.listdir()
# import os
# icerik = os.listdir(dosya_yolu)
# for ic in icerik:
#     if os.path.isdir(ic):
#         print(ic)

# 2. Yol -> os.scandir()
# with os.scandir(dosya_yolu) as scans:
#     for scan in scans:
#         if scan.is_dir():
#             print(scan)

# folder = os.scandir(dosya_yolu)
# for eleman in folder:
#     if eleman.is_dir():
#         print(eleman)

# 3. Yöntem -> pathlib.Path.iterdir()
from pathlib import Path
ana_dosya = Path(dosya_yolu)
dosya_icerigi = ana_dosya.iterdir()

for dos in dosya_icerigi:
    if dos.is_dir():
        print(dos)