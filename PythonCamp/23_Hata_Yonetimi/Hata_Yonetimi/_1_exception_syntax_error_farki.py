"""
1 - Exception ile Syntax Error Farkı:

Bir Python programı, bir hata ile karşılaştığında durur.
İşte, bu durma işleminin nasıl olacağına Exception Handling (Hata Yönetimi).

Python'da hata (error) iki türlü olur:
 * Syntax Error (Yazım Hatası)
 * Exception (uygulama hatası)
"""

"""
Syntax Error (Sözdizimi Hatası):

Python Parser'ı (kod oluşturucu) yazım şekli Python kurallarına uymuyorsa, "Syntax Error" üretir.

Hata tipi: SyntaxError
"""

# Örnek:
#print(4 / 12))
# SyntaxError: unmatched ')'


# Örnek:
# a = "12'
# print(a)
# SyntaxError: EOL while scanning string literal


# Örnek:
# SyntaxError: invalid syntax
def myFunc():
    print('A')


"""
Exception: Syntax'ı doğru olan, ama Python Interpreter'ın çalışırken (run-time) aldığı hatalardır.
"""

# Örnek:
# a = 7 / 0
# ZeroDivisionError: division by zero

# Örnek:
# print(t)
# NameError: name 't' is not defined

# Örnek:
a = 12
b = 'B'
# print(a + b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

