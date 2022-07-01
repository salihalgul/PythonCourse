"""
Şimdiye kadar şunları gördük:

    try:
        <---- kod ---->
    except:
        <---- hata ---->
    else:
        <---- hatasız işleme ---->
    finally:
        <----- ne olursa olsun ----->
"""

# Örnek:
def bolme(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('sonuc:', result)
    finally:
        print('İşlem tamamlandı.')

# hatalı çağırma
# bolme(5, 0)

# hatasız çağırma
# bolme(8, 2)


# Örnek:

def dosya_ac(path):
    try:
        file = open(path, encoding='utf-8')
    except Exception as ext:
        print(ext)
    else:
        print(file.read())
    finally:
        # burada file.close() demeden -> file var mı -> try
        try:
            file.close()
        except:
            pass


dosya_ac('örnek.txt')
