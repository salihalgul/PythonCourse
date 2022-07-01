"""
CSV: Comma Seperated Values
Virgül (noktali virgül) ile ayrılmış değerler tutar.
"""

# Python'da CSV okuma işlemleri -> csv paketi ile yapılır

import csv

film_yolu = 'data/movies.csv'
film_yolu_noktali_virgul = 'data/movies_noktali_virgul.csv'

# ----------------- CSV OKUMA --------------------#

# delimiter = ayıraç : ,
def csv_oku():
    with open(film_yolu, 'r') as dosya:
        # önce bir csv reader alalım
        filmler = csv.reader(dosya, delimiter=',')

        # csv.reader() geriye bir iterator döner -> üzerinde döngü
        for film in filmler:
            # her bir satır bir film, bir list olarak döner
            print(film)


# delimiter = ayıraç : ;
def csv_oku_noktali_virgul():
    with open(film_yolu_noktali_virgul, 'r') as dosya:
        # önce bir csv reader alalım
        filmler = csv.reader(dosya, delimiter=';')

        # csv.reader() geriye bir iterator döner -> üzerinde döngü
        for film in filmler:
            # her bir satır bir film, bir list olarak döner
            print(film)

"""
Dialect ile okuma formatını düzenleme
"""

def csv_oku_dialect():
    csv.register_dialect('normal_okuma',
                         delimiter=',',
                         quoting=csv.QUOTE_MINIMAL)

    with open(film_yolu, 'r') as dosya:
        # önce bir csv reader alalım
        filmler = csv.reader(dosya, dialect='normal_okuma')
        for film in filmler:
            # her bir satır bir film, bir list olarak döner
            print(film)


# reader() çalışabilir mi? hangi ayıraç?
def csv_sniffer(yol):
    with open(yol, 'r') as dosya:
        icerik = dosya.read()
        has_reader = csv.Sniffer().has_header(icerik)
        print(has_reader)

        dialect = csv.Sniffer().sniff(icerik)
        print('ayıraç:', dialect.delimiter)



# ----------------- CSV YAZMA --------------------#

# NOT:mode='w' ile değil, mode='a' ile yazacağız

eklenecek_film = ["250","Slumdog Millionaire","2008","R","25 Dec 2008","120 min","Drama","Danny Boyle, Loveleen Tandan",
                  "Simon Beaufoy (screenplay), Vikas Swarup (novel)","Dev Patel, Saurabh Shukla, Anil Kapoor, Raj Zutshi",
                  "A Mumbai teen reflects on his upbringing in the slums when he is accused of cheating on the Indian Version of Who Wants to be a Millionaire?",
                  "English, Hindi, French","UK, France, USA","Won 8 Oscars. Another 144 wins & 126 nominations.",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NTA5NzI0N15BMl5BanBnXkFtZTcwMjUxMjYxMg@@._V1_SX300.jpg",
                  "Internet Movie Database","8.0/10","86","8.0","679,975","tt1010048",
                  "movie","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A",
                  "http://www.rottentomatoes.com/m/slumdog_millionaire/","31 Mar 2009","$141,243,551",
                  "Fox Searchlight Pictures","http://www.foxsearchlight.com/slumdogmillionaire/","True"]

def csv_yazma():
    with open(film_yolu, 'a', newline='') as dosya:
        writer = csv.writer(dosya, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(eklenecek_film)




# Aynı anda 2 Dosya'da nasıl işlem yapabiliriz
def csv_kopyala():
    yeni_film_yolu = 'data/movies_csv_kopya.csv'

    # yen dosyayı yaratalım
    open(yeni_film_yolu, 'x')

    # aynı anda 2 dosya açma
    with open(film_yolu, 'r') as movies, open(yeni_film_yolu, 'a', newline='') as movies_c:
        filmler = csv.reader(movies)
        writer = csv.writer(movies_c, quoting=csv.QUOTE_ALL)

        for film in filmler:
            writer.writerow(film)



