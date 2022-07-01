"""
Python Paketleri -> aslında birer klasör'dür
* tek farkı -> içinde "__init__.py" adında bir python dosyası vardır.

Paketler:
* kodu organize ederler
* taşınabilir
* modulleri birleştirir

Paket altındaki module erişmek:
* pak1.mod1
* pak2.mod2.mod21..
"""

"""
Paket Yaratmak:

* __init__.py içinde:
    * alt paketler ve moduller için importlar
    * global değişkenler
    * dokümanatasyonlar
"""

# -------------------- pak paketini import edelim ------------------------#
# yanlış -> direk erişilemez (paket altında)
# import mod_1

# önce paketi import et
import pak

# absolute import ->
# import mod_1
# import mod_2

# paketin altındaki modul ->
pak.mod_1.print_mod_1()




