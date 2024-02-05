import datetime

"""
Dunder" kelimesi, "double underscore"ın kısaltmasıdır ve Python'da özel (special) metodları ifade eder.
Bu metodlar, bir nesnenin özel davranışlarını kontrol etmek için kullanılır.
Dunder metodları çift alt çizgi ile başlar ve biter.
"D"ouble "UNDER" --> çift alt çizgi
"""

"""
__init__(self, ...): Bir sınıf örneği oluşturulduğunda otomatik olarak çağrılan inşa (constructor) metodudur. 
Nesne başlatma işlemleri için kullanılır.
"""

"""
__str__(self): str() fonksiyonu çağrıldığında çalışan metod. Objenin "okunabilir" bir dize temsilini döndürür.
"""


class Car:
    """
    This is a class Documentation
    This class for keeping Car attributes.
    """
    type = 'Car'

    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return f'Car name: {self.name}'


c1 = Car('BMW')
print(c1)
print(dir(c1))
print(c1.__doc__)  # İlk yorum satırı """xxx""". Genellikle class ve fonksiyonların işlevlerini öğrenmek için kullanılır
print(c1.__class__)  # output--> <class '__main__.Car'>  --> referansın bağlı olduğu classı gösterir
print(c1)
print('*' * 45)

my_list = [1, 2, 3, 4]
print(dir(my_list))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
'pop', 'remove', 'reverse', 'sort']
__add__ __class__ __class_getitem__ __contains__ __delattr__
"""

now = datetime.datetime.now()
print(now)  # output --> 2024-02-05 15:18:39.165157
print(type(now))  # output --> <class 'datetime.datetime'>
print('*' * 45)
now2 = now.__str__()
print(now2)  # output --> 2024-02-05 15:21:10.447988
print(type(now2))  # <class 'str'>
print('*' * 45)
now3 = now.__repr__()  # str den farkı makinanın anlayacağı dilden yazıyor
print(now3)  # output --> datetime.datetime(2024, 2, 5, 15, 22, 15, 457349)
print(type(now3))  # output --> <class 'str'>
print('*' * 45)
a_list = [1, 9, 15]
print(a_list)
print(type(a_list))  # <class 'list'>

print(type(a_list.__str__()))  # <class 'str'>
print(type(a_list.__repr__()))  # <class 'str'>


class Trendyol:
    type = 'users'

    def __init__(self):
        pass


# biz oluştursak da oluşturmasak da python makinesi arkaplanda bizim için bir repr ve str dunderı oluşturuyor
t1 = Trendyol()
# oluşturmamam rağmen bellekte yer ayırılmış
print(t1.__str__())  # <__main__.Trendyol object at 0x000001E730689AF0>
print(t1.__repr__())  # <__main__.Trendyol object at 0x000001E730689AF0>


class Login:
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

    def __str__(self):
        return f'username: {self.username}' + '\nPassword: ' + ('*' * len(self.password))


# nesnemizi string türüne dönüştürdük
l1 = Login('ruin', 'chain')
print(l1)

# __str__ --> toString()
"""
Return değeri olarak string döndürür
 genellikle hata ayıklama, kullanıcı dostu çıktılar veya nesnelerin temsilini anlamak için kullanıcılar ve diğer 
 geliştiriciler için faydalı olabilir.
"""

print('*' * 45)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print('hi user!')
        return f"Point({self.x}, {self.y})"


p1 = Point(3, 6)
print(p1)  # hi user! Point(3, 6)
"""
print() Fonksiyonu İle Kullanım: __str__ metodunu tanımladığınızda, 
sınıf örneklerini print() fonksiyonu ile doğrudan yazdırabilirsiniz.

Bu metodun kullanılması tamamen isteğe bağlıdır ve özellikle sınıfın anlaşılabilir bir temsilini sağlamak 
istiyorsanız faydalı olabilir. Eğer __str__ metodu tanımlanmazsa, varsayılan olarak object sınıfından miras alınan bir 
temsil sağlanır, ancak bu genellikle sınıfın özelliklerini açıklayıcı bir şekilde temsil etmez.
"""

"""
Repr de aynı şekilde
"""
