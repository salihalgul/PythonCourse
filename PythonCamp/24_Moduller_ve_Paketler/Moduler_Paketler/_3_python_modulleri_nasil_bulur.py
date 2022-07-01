"""
import <modul_adi>

Python Modulleri 3 şekilde arar:
1- Bu kodun çalıştığı klasörlerde arar (aynı seviyede)
2- PYTHONPATH environment variable -> tanımlı
3- Python'un kurulu olduğu klasörlerde arar (virtul env'lerde)

sys.path -> arama klasörlerini gösterir
"""

# Search Path'i görelim
import sys

python_search_path = sys.path
# print(python_search_path)
# tek tek yazdır
for path in python_search_path:
    print(path)

# Örnek:
# moduller\girdi_islemleri_modul

# bu şekilde gelmez -> direk bu klasör seviyesinde değil
# import girdi_islemleri_modul

# klasör yolu ile alabildik
import moduller.girdi_islemleri_modul as girdi
# metin = girdi.string_al()
# print(metin)

"""
Klasör yolu ile modullere erişim edilmez -> klasör adı değişebilir, klasör yer değiştirebilir
"""

"""
Bu proje içinden herkes erişebilir:
Lokal Erişim: Moduler_Paketler\venv\lib\site-packages
"""

# Örnek:
# import girdi
# sayi = girdi.tamsayi_al()
# print(sayi)


"""
Bu makina üzerinde bütün Python kodlarının erişebileceği yapı:
Global Erişim:
...\Python\Python38\lib

"""
import global_girdi

ondalik = global_girdi.ondalik_sayi_al()
print(ondalik)
