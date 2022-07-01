"""
2- String.format

süslü {} ile string formatlama
"""

# index vermeden
selam = 'Selam sana {} {}'
print(selam.format('Peter', 'Parker'))

# index vererek
ifade = "{0} kelimesinin {1} adet harfi var."
print(ifade.format("Python", len('Python')))

# isim vererek
adi_nereden_gelir = "{ad} ismi {kaynak}"

print(adi_nereden_gelir.format(ad="Python", kaynak="Monthy Python dizisinden gelir."))

print(adi_nereden_gelir.format(ad='Java', kaynak="Endonezya'daki Java kahve türünden gelir."))


