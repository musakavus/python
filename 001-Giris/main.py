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

# \n --> newline
# \t --> tab kadar boşluk
# \a --> alarm

print('Merhaba \'python\'')
print('Merhaba "Python"')

print(1 + 2j)  # komplex türde sayı

k = 5 + 2j
print(type(k))  # output: <class 'complex'>
# int 32bit yada 64 bit kadar yer kaplar
# float 64 bit
# python 3 ile birlikte integerlardaki karakter sınırlandırması kaldırılmıştır

print(1_000_000)  # 1.000.000 şeklindeki yazım için

print(type(1e6))  # e

a_string = 'a'
print(type(a_string))

# statik diller type bakımından daha güvenilirdir
# statik diller daha hızlıdır daha verimlidr
# dynamic diller ekstra hafıza yüküne sahiptir

# dynimic diller daha esnek yapılar
# gelen verilerin tipini bilmediğimiz zamanlarda dinamik diller daha esnektir

data: str = '5'
print(data)

# bu sadece bir çözüm önerisidir. Mesela aşağıdaki kod hata vermez
data2: int = 'a string'
print(data2)
print(type(data2))
a_string2 = 'Hi world'
print(len(a_string))
print(len('Hi world'))
print()
a_list = [1, 2, 3, 4, 'hellow', 'world']
print(len(a_list))

# len ve type fonskiyonlarına sadece 1 tane parametre verilebilir


