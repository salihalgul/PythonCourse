"""
4- Template Strings

* 'string' modülü altında Template class'ı ile kullanılır
* $ işareti ile değişken yerleştirilir
"""

from string import Template

# Örnek 1:
ad = 'Bruce Wayne'
kahraman = 'Batman'

sablon = Template("$k'ın asıl adı $a")
print(sablon.substitute(a=ad, k=kahraman))

# Örnek 2:
sayi_1 = 5
sayi_2 = 8
sonuc = sayi_1 * sayi_2
sablon = Template("$a * $b = $c")
print(sablon.substitute(a=sayi_1, b=sayi_2, c=sonuc))


# direk chain'leyerek de kullanabilirdik
print(Template("Zincir ile: $a * $b = $c").substitute(a=sayi_1, b=sayi_2, c=sonuc))