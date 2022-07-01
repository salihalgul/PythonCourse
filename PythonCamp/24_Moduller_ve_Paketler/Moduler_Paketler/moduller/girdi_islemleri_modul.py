"""
Bu modül, kullanıcıdan bir girdi ister.
İstenen sonuç tipi ne ise ona göre sonuç döner.
"""


def girdi_iste(tip='metin'):
    return input("Lütfen bir {0} giriniz: ".format(tip))


def string_al():
    """
    Kullanıcıdan bir metin ister ve bu metni döner.
    :return: str tipinde girdi metni
    """

    girdi = girdi_iste()
    return girdi


def tamsayi_al():
    """
    Kullanıcıdan bir tam ister.
    :return: int tipinde sayi
    """
    # tam sayı alana kadar istemeye devam eder
    while True:
        try:
            girdi = girdi_iste(tip='tamsayı')
            sayi = int(girdi)
        except ValueError:
            continue
        else:
            return sayi


def ondalik_sayi_al():
    """
    Kullanıcıdan bir ondalık ister.
    :return: float tipinde sayi
    """
    # ondalık sayı alana kadar istemeye devam eder
    while True:
        try:
            girdi = girdi_iste(tip='ondalık sayı')
            ondalik_sayi = float(girdi)
        except ValueError:
            continue
        else:
            return ondalik_sayi


