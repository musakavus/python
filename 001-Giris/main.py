"""
Değişken İsimlendirme
Değişken isimler küçük harfle başlamalıdır
birden fazla kelimeden oluşuyorsa aralarına _
# İyi isimlendirilmiş değişken
user_age = 25

# Kaçınması gereken isimlendirme
a = 25


Fonksiyon İsimlendirme
Değişken isimler küçük harfle başlamalıdır
birden fazla kelimeden oluşuyorsa aralarına _
Fonksiyonlar, ne yaptıklarını anlatabilecek şekilde isimlendirilmelidir.

# İyi isimlendirilmiş fonksiyon
def calculate_square_area(side_length):
    return side_length ** 2
# Kaçınması gereken isimlendirme
def calc(x):
    return x ** 2

Sınıf isimlendirme
CamelCase: Büyük harfle başlayan kelimenin ardından yine büyük harf
# İyi isimlendirilmiş sınıf
class MyCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Kaçınması gereken isimlendirme
class myCar:
    def __init__(self, m, mdl):
        self.m = m
        self.mdl = mdl

Modül ve Paket isimlendirme
küçük harfle başlayıp aralarına _
# İyi isimlendirilmiş modül
import my_module

# Kaçınması gereken isimlendirme
import myModule

Sabit İsimlendirme
Sabitler, genellikle büyük harfle yazılmalıdır.
Kelimeler arasında alt çizgi _ kullanılabilir.
MAX_SIZE = 100

# Kaçınması gereken isimlendirme
maxsize = 100
"""

# Local and Global Scope
"""
Global Scope: Bir değişkenin global kapsamda tanımlandığı durumdur.
Bu değişken, programın herhangi bir yerinde erişilebilir.

Local Scope: Bir değişkenin bir fonksiyon veya blok içinde tanımlandığı durumdur.
Bu değişken sadece tanımlandığı yerde erişilebilir.
"""
global_variable = 10  # global scope


def my_function():
    print(global_variable)


my_function()


def my_function():
    local_variable = 20  # local variable
    print(local_variable)


my_function()

"""
Indentation (Girinti):

Python'da kod blokları girintilerle belirlenir. Diğer programlama dillerinde olduğu gibi süslü parantez {} kullanılmaz. 
Girintiler, kodun hangi bloğa ait olduğunu belirtir.
Genellikle 4 boşluk veya bir tab karakteri kullanılır. Ancak birisi seçildikten sonra diğerini karıştırmamak önemlidir.
if True:
    print("Bu kod bloğu doğru şart altında çalışır.")
else:
    print("Bu kod bloğu yanlış şart altında çalışır.")

"""

# Assigning multiple values in single line

a, b, c = "geeks", "for", "geeks"
print(a + b + c)

a = 1 if 20 > 10 else 0

# Printing value of a
print("The value of a is: ", str(a))