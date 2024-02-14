"""
constructor: Yapıcı metodlar -> (__new__) # nesne bellekte ilk yer tutmaktır
initializer function -> başlatıcı metod (__init__) -> işlevi, nesneye ilk değerleri vermektir. initialization görevi


biz bunca zamandır init fonksiyonuna constructor metod diyorduk. Ama aslında initialization metoddur.
Nesneye ilk değerleri verme metodudur. Bu yüzden python bu yapısıyla dğer dillerden ayrılır biraz.

new fonskiyonun amacı ise nesneye bellekte yer ayırmaktır. Sınıftan nesne üretildiğinde ilk olarak nesne için
yer ayırılması gerekiyor. new metodu bu işe yaraıyor. Ayrıca nesneleri denetlememize yardımcı olur

Nesnelerin yaşam döngüsü --> constructor --> initialization --> destruction
"""


class Person:
    def __new__(cls):  # classı temsil ettiği için cls alır
        print('New metodu çalıştı')

    def __init__(self):
        print('init fonksiyonu çalıştı')


p1 = Person()  # output -> New metodu çalıştı

# init fonksiyonu çalışmadı dikkat ettiysen. Öncelik new metodunun
# biz yazmasak bile new metodu aslında çalışıyor. Ama none olduğu için çıktı vermiyor ve init çalışıyor
# fakat new fonksiyonu yazarsak, overriding işlemi gerçekleştiği için çalışıyor ve sonuç veriyor

print('*' * 45)


class Animal:  # biz yazsak da yazmasak da animal sınıfı pythondaki object classından miras almıştır
    # dolayısıyla class Aanimal = class Animal() = class Animal(object)
    def __new__(cls, *args, **kwargs):  # varsayılan yazımı böyledir ayrıca
        print('I am new function')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('I am init function')


a1 = Animal()
"""
output:
I am new function
I am init function

artık her iki metodda çalıştı bu sayede. Fakat yine de ilk new function çalışır. Çünkü yaşam döngüsü
"""

"""
ilk olarak new çalışır. Çünkü nesne için yer ayırılır.
İkinci olarak init çalışır. ilk değerleri yani instance attributelere değer vermek için
üçüncü olarak destruction kullanılır. O sonraki zamanların konusu
"""

"""
NEW METODUNU SADECE BİLGİ AMAÇLI ÖĞRENDİK. NORMALDE BUNLARLA Bİ İŞİMİZ YOK
hatta kafa karıştırır. Çünkü-->
new metodunun arkaplandaki orjinal hali budur
    def __new__(cls, *args, **kwargs):  # varsayılan yazımı böyledir ayrıca
        return super().__new__(cls, *args, **kwargs)
ve bu içerik sayesinde init fonksiyonu çalıştırılır.

Ama biz new metodu oluşturup varsayılan içeriğini değiştirirsek override işlemi yapmış oluruz. 
dolayısıyla init fonksiyonu çalışmaz. Ve bizde instance değer ataması yapamayız
"""
