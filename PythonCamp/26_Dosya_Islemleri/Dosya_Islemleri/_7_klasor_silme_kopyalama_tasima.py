"""
1- Klasör Silme
2- Dosya ve Klasör Kopyalama
3- Dosya ve Klasör Taşıma
4- Klasörü Yeniden Adlandırma
"""

import shutil
import os
import pathlib


# 1- KLASÖR SİLME
"""
* os.rmdir() -> tek klasör siler (klasör BOŞ ise)
* pathlib.Path.rmdir() -> tek klasör siler (klasör BOŞ ise)
* shutil.rmtree() -> tüm klasör ağacını siler
"""

# önce silinecek klasor yarat
# os.mkdir('silinecek_klasor')

# silinecek_klasor boş olduğu için -> os.rmdir() bunu silebilir
# os.rmdir('silinecek_klasor')

# boş değilse -> OSError: [WinError 145] Dizin boş değil: 'silinecek_klasor'

# dolu klasör silmeyi -> shutil
# shutil.rmtree('silinecek_klasor')


# 2- DOSYA ve KLASÖR KOPYALAMA
# Dosya Kopayalama
# shutil.copy()
# shutil.copy2()
# Source -> Destination
# src = 'kaynak_klasor/k1.txt'
# dst = 'hedef_klasor/h1.txt'
# shutil.copy(src, dst)

# Klasör Kopyalama
# shutil.copytree()
# shutil.copytree('kaynak_klasor', 'kaynak_klasor_kopyasi')


# 3 - DOSYA ve KLASÖR TAŞIMA
# shutil.move(kaynak, hedef)
# shutil.move('kaynak_klasor/k1.txt', 'hedef_klasor')
# shutil.move('kaynak_klasor_kopyasi', 'hedef_klasor')


# 4- KLASÖRÜ YENİDEN ADLANDIRMA
os.rename('kaynak_klasor', 'final_klasoru')




