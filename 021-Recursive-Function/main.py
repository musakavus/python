# Recursive fonksiyon
"""
Recursive function--> Fonksiyon içinde kendini sürekli tekrar eden ve fonksiyonda kendini döndüren fonksiyonlardır.
Bir nevi döngü gibi düşünebilirsin. Ve eğer döngülerdeki gibi bu fonksiyonlara da döndürücü bir yöntem uygulamazsak
sonsuza dek çalışmaya devam eder. Ve eğer durdurulmazsa çok fazla kaynak tüketimine sebep olur
"""


def calculate(num):
    if num == 1:
        return 1
    else:
        return num * calculate(num - 1)


print(calculate(6))

"""
num = 6 iken
return = 6 * calculate(5) --> 6 * 120 = 720

num = 5 iken  
return = 5 * calculate(4) --> 5 * 24

num = 4
return 4 * calculate(3) --> 4 *  6

num = 3
return 3 * calculate(2) -->  3 * 2

num = 2
return 2 * calculate(1) --> 2 * 1

num = 1
return = 1  !! şimdi de yukarıya doğru yerleştiriyoruz 1 cevabını

 
 aşağıdan yukarıya doğru sağfaki commetnleri oku
"""

"""
haliyle recursive fonksiyonlar çok fazla kaynak tüketimine neden oluyor. Sonucu bulmak için 
6 defa fonksiyonu çalıştırdık. Daha sonra bu değerleri hesaplayabailmek için ileri geldiğimiz gibi 
tekrar geri gidiyoruz yerine koya koya. dolayısıyla çok fazla kaynak harcıyor
"""
