"""
Bu paket örnek amaçlıdır.

İçinde iki adet modul vardır:
* mod_1
* mod_2

"""

# yanlış import şekli -> absolute import
# import mod_1
# import mod_2


# doğru import
# relative import -> olduğumuz yerde var
# olduğumuz yer -> .
from . import mod_1
from . import mod_2


