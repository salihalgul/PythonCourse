"""
Ne kadar uğraşırsak uğraşalım,
kendimize "bu kod nerede patlar?" diye ne kadar sorarsak soralım,
Kodumuz patlayacak ve Exception hataya çıkacaktır.
Eğer bu gibi durumları öngörmezsek programımız aniden duracak (çökecek) ve istenmeyen sonuçlar olacaktır.

O zaman bir hata olması durumunda ne yapmalıyız.
Öncelikle kodumuzun bu hataya uygun Exception fırlatmasını sağlamamız lazım.

Uygun hata, hem sizin kodu iyileştirip düzeltmeniz, hem de sizin programınızı kullanan başka sistemlerin,
bu hatalara göre gerekli adımları atmasını kolaylaştırır.

İşte, ortaya bir hata çıktığında yapacağımız işlem -> Exception Fırlatmaktır (Raise)
"""

""" 
----  Raise  ---- 
"""

""" 
Örnek:
Daha önce yaptığımız bir işlem vardı, kullanıcıdan bir sayı istiyorduk
Yani ayınısını yapalım ve eğer kullanıcı sayı girmezse hata fırlatalım
"""

def hata_firlat():
    girdi = input("Lütfen bir sayı giriniz: ")

    # eğer biz bu olası hatayı düşünmezsek -> crach
    if not girdi.isdigit():
        raise Exception('Sayı girmedeniz...')

    sayi = int(girdi)
    print(sayi)

# fonksiyonu çağır
# hata_firlat()
# ValueError: invalid literal for int() with base 10: 'abc'

def tanimli_hata_firlat():
    girdi = input("Lütfen bir sayı giriniz: ")

    # eğer biz bu olası hatayı düşünmezsek -> crach
    if not girdi.isdigit():
        raise ValueError('Sayı girmedeniz...')

    sayi = int(girdi)
    print(sayi)

# tanimli_hata_firlat()

"""
Şimdi eğer, kullanıcı sayı değil de alfanumerik bir değer girerse ortaya ValueError çıkacağını bildiğimize
göre artık jenerik Exception fırlatmak yerine direk ValueError tipinde bir hata fırlatabiliriz
"""


""" 
----  assert  ---- 
"""

"""
Yukarıda yaptığımız if kontrolü aslında bir assertion (doğrulama) işlemi idi.
Yani eğer o kod bloğu doğrulanmadı ise (assert olmadı ise) devam etme dedik Python'a.
Python'da eğer sadece doğrulama amaçlı bir kod yazacaksanız if yerine bunun için özel yazılmış bir komut var:
'assert' komutu.
assert <kontrol ifadesi>
şeklide kullanırız ve eğer <kontrol ifadesi> doğrulanmazsa, kod burada durur istediğiniz hatayı fırlatır.
Genellikle debug işlemleri için çok kullanılır.
"""

""" 
Örnek:
yukuarıdaki işlemi bir daha yapalım
"""

def girdi_dogrula():
    girdi = input("Lütfen bir sayı giriniz: ")

    assert int(girdi), ValueError('Sayı girmediniz...')

    sayi = int(girdi)
    print(sayi)

# girdi_dogrula()






""" 
Örnek:
Diyelim ki bölme işlemi yapan bir fonksiyonunuz var.
Bölme deyince aklınıza ilk olarak olası 'Sıfıra Bölme' hatası gelmeli :)
Sıfıra Bölme hatasına takılmamak için bölen'in 0 olup olmadığını assert etmemiz lazım
"""

def bolme(n1, n2):

    # assert ile doğrula
    assert n2 != 0, 'Sıfıra bölme yapılamaz...'
    # AssertionError: Sıfıra bölme yapılamaz...

    print(n1 / n2)


# hatasız çağırma
# bolme(10, 2)

# hatalı çağırma
bolme(10, 0)
