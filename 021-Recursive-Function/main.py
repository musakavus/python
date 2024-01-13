# Recursive fonksiyon
"""
Recursive function--> Fonksiyon içinde kendini sürekli tekrar eden ve fonksiyonda kendini döndüren fonksiyonlardır.
Bir nevi döngü gibi düşünebilirsin. Ve eğer döngülerdeki gibi bu fonksiyonlara da döndürücü bir yöntem uygulamazsak
sonsuza dek çalışmaya devam eder. Ve eğer durdurulmazsa çok fazla kaynak tüketimine sebep olur
"""


# n! = n*(n-1)*(n-2)
def factorial(num) -> int:
    result = 1

    def calculate():
        result = num * result

    return result


num = int(input())
result = factorial(num=num)
