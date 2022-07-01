"""
Python'da PDF dosyaları ile çalışacağız bu bölümde.

1- PDF özelliklerini okuma
2- PDF'ten text (sayfa) okuma
3- PDF'ten sayfa alma (extract)
4- PDF'leri birleştirme
5- PDF'i döndürme

Bu işlemleri yaparken yeni bir Python paketleri kullanacağız:
* PyPDF2
    * https://pypi.org/project/PyPDF2/
* pdfplumber
    * https://pypi.org/project/pdfplumber/

Bu paketler Python içinde direk olarak gelmiyor.
Dolayısı ile dışarıdan yüklememiz lazım.

Python paketleri dünyada merkezi yerlerde open-source olarak depolanır.
Herkes paketleri buradan yükler.

Python'da paket yüklemek için: pip
'pip' Python'un paket yöneticisidir.
Yani Python içine paketleri yüklemenizi veya kaldırmanızı sağlar.
Python içinde pip, direk olarak 'pypi.org' sitesine bağlıdır.
"The Python Package Index (PyPI) is a repository of software for the
Python programming language."
https://pypi.org/

https://packaging.python.org/tutorials/installing-packages/
Command Prompt -> cmd
pip --version
pip install PyPDF2
"""

"""
Kullanacağımız pdf direk Python'un yaratıcısı Guido van Rossum, tarafından hazırlanmış
* Python Tutorial (release 3.9.1) January 12, 2021 
:)
"""

import os
import PyPDF2
import pdfplumber

# önce pdf dosyamızın yolunu oluşturalım
proje_yolu = os.getcwd()
pdf_path = os.path.join(proje_yolu, 'pdf', 'tutorial.pdf')


# -----------------  1- PDF Özelliklerini Okuma ------------------ #
def pdf_ozellikleri_okuma():
    # pdf'i oku
    pdf = PyPDF2.PdfFileReader(pdf_path)
    print(pdf_path)
    print(pdf)

    # sayfa sayısı
    sayfa_sayisi = pdf.getNumPages()
    print(f"sayfa sayısı: {sayfa_sayisi}")

    # şimdi dokuman bilgileri
    dokuman_bilgileri = pdf.documentInfo

    for key, value in dict(dokuman_bilgileri).items():
        print(f'{key}: {value}')


# -----------------  2- PDF'ten Text (Sayfa) Okuma ------------------ #
# Tek Sayfa
def pdf_sayfa_oku(sayfa_no=0):
    # pdfplumber normal open metodu gibi çalışır
    with pdfplumber.open(pdf_path) as pdf:
        sayfa = pdf.pages[sayfa_no]
        icerik = sayfa.extract_text()
        print(icerik)


# Çok Sayfa
def pdf_sayfalar_oku(ilk_sayfa=0, son_sayfa=1):
    # pdfplumber normal open metodu gibi çalışır
    with pdfplumber.open(pdf_path) as pdf:
        for i in range(ilk_sayfa, son_sayfa + 1):
            print(f'-----------{i}. sayfa başı -----------')
            sayfa = pdf.pages[i]
            icerik = sayfa.extract_text()
            print(icerik)
            print(f'-----------{i}. sayfa sonu -----------')


# -----------------  3- PDF'ten Sayfa Alma (Extract) ------------------ #

# TEK SAYFA AL
def sayfa_al(sayfa_no=0):
    # tek seferde import
    from PyPDF2 import PdfFileReader, PdfFileWriter
    new_pdf_path = os.path.join(proje_yolu, 'pdf', 'yeni_pdf_' + str(sayfa_no) + '.pdf')

    # Önce PDF'i alalım
    pdf = PdfFileReader(pdf_path)

    # PDF'ten sayfa alalım
    sayfa = pdf.getPage(sayfa_no)

    # şimdi yeni bir PDF oluşturalım
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(sayfa)

    # şimdi oluşturduğumuz bu sayfanın içini doldur
    # wb -> write binary
    with open(new_pdf_path, 'wb') as sonuc:
        pdf_writer.write(sonuc)


# ÇOK SAYFA AL
def sayfalar_al(ilk_sayfa=0, son_sayfa=1):
    # tek seferde import
    from PyPDF2 import PdfFileReader, PdfFileWriter
    new_pdf_path = os.path.join(proje_yolu, 'pdf', 'tutorial_parcasi.pdf')

    # Önce PDF'i alalım
    pdf = PdfFileReader(pdf_path)

    # şimdi yeni bir PDF oluşturalım
    pdf_writer = PdfFileWriter()

    # şimdi sayfaları döngü içinde al
    for i in range(ilk_sayfa, son_sayfa + 1):
        # sayfamızı alalım
        sayfa = pdf.getPage(i)

        # sayfayı pdf_writer'a ekleyelim
        pdf_writer.addPage(sayfa)

    # şimdi oluşturduğumuz bu sayfanın içini doldur
    # wb -> write binary
    with open(new_pdf_path, 'wb') as sonuc:
        pdf_writer.write(sonuc)


# -----------------  4- PDF'leri Birleştirme  ------------------ #

def pdf_birlestir(*args):
    # merge edecek (birleştirecek) class
    from PyPDF2 import PdfFileMerger

    # bir merger nesnesi
    pdf_merger = PdfFileMerger()

    # şimdi *args içinde gelen tüm sayfaları ekleyelim
    for arg in args:
        pdf_merger.append(arg)

    # pdf_merger nesnemiz doldu, şimdi onu bir pdf olarak kaydet
    birlesmis_pdf = os.path.join(proje_yolu, 'pdf', 'birlesik.pdf')

    with open(birlesmis_pdf, 'wb') as birlesecek:
        pdf_merger.write(birlesecek)


# -----------------  5- PDF'i Döndürme  ------------------ #
# .rotateClockwise() ve .rotateCounterClockswise()

def pdf_dondur(derece):
    # 90 derecenin katı olmalı

    from PyPDF2 import PdfFileReader, PdfFileWriter

    # birlesik.pdf'i okuyalım
    birlesik_pdf = PdfFileReader('pdf/birlesik.pdf')

    # yazacağımız yeni PDFFileWriter nesnesini yarat
    pdf_writer = PdfFileWriter()

    # birlesik.pdf içindeki tüm sayfaları döneceğiz
    for i in range(birlesik_pdf.getNumPages()):
        # sayfayı alalım
        sayfa = birlesik_pdf.getPage(i)

        # saat yönünde döndür
        sayfa.rotateClockwise(derece)

        # yazıcıya verelim
        pdf_writer.addPage(sayfa)

    # tüm sayfları döndürüp yazıcıya verdik -> PDF oluştur
    with open('pdf/birlesik_dondurulmus.pdf', 'wb') as birlesik_dondurulmus:
        pdf_writer.write(birlesik_dondurulmus)










