"""
3. f-strings (String Interpolation)

* f-strings Python 3 ile geldi (yeni)
* f' ...string...' şeklinde string'in başına f harfi konur
* str.format() gibi çalışır ama daha dinamiktir
* {} süslü parantez ile kullanılır
"""

x = 2
y = 3

carpim = x * y
print(f"{x} * {y} = {carpim}")

# direk {} içinden de işlem yapılabilir (ifade çalıştırılabilir)
print(f"{x} * {y} = {x * y}")

veri = ['Klark Kent', 'Metropolis', 'Daily Planet']
print(f'{veri[0]}, yani Superman, kurgusal {veri[1]} şehrinde, {veri[2]} gazetesinde çalışır.')

# Önemli Not:
# f-strings Python 3.6 ile geldi.

