# Yapıcı metodlar
"""
init medodu başlangıç sınıf nitelikleri vermez. Başlangıç nesne niteliklerini verir.
her nesne oluşturulup çağırıldığı zaman aslında init fonkyionu çalışır sen oluşturmamış olsan bile
python arkaplanda senin için boş bir tane oluşturuyor
    def __init__(self):
        pass


nesne çalıştırıldığı zaman çalışan ilk metod init metodur
"""


class Car:
    # burdaki değerlr başlangıç "sınıf nitelikleridir."
    name = 'Ford'
    model = 'Focus'
    year = 2001

    def __init__(self, _name, _model, _year):  # nesne niteliğini temsil eder.
        self.name = _name
        self.model = _model
        self.year = _year

    def show_info(self):
        print(f'Car name: {self.name}  \nCar model: {self.model} \nCar year: {self.year}')


class Welcome:
    def __init__(self):
        print('Welcome to Sixt Rent a Car')


while True:
    try:
        name = input('name: ')
        model = input('model: ')
        year = int(input('year: '))

    except ValueError as err:
        print(err)
        print('you can put string type.! Try again!')

    else:
        name = name.upper()
        model = model.upper()
        Welcome()  # init metodu referans  oluşturulmadan da kullanılabilir
        c1 = Car(name, model, year)
        break

c1.show_info()

Car.name = 'Mercedes'  # sınıftaki niteliği değiştirir

# Welcome() -> bu bir nesnedir ama referans değildir. Her referans bir nesnedir. Ama her nesne bir referans değildir

print('*' * 45)


class MyClass:
    def __init__(self, name=None):
        if name is None:
            print('Default constructor called')
        else:
            self.name = name
            print('Parameterized constructor called with name ', self.name)

    def method(self):
        if hasattr(self, 'name'):
            print('Method called with name: ', self.name)
        else:
            print('Method called without a name')


obj1 = MyClass()
obj1.method()
print('*' * 45)

obj2 = MyClass('Ruin')
obj2.method()


class Student:
    name = None  # CLASS ATTRIBUTE
    surname = None
    width = 0
    height = 0

    def __init__(self, n1, s1, w1, h1):
        self.name = n1  # burda parametre eşitliği yapılıyor. sol taraf normal bildiğin pythondaki atama işlemi gibi
        self.surname = s1  # INSTANCE ATTRIBUTE
        self.width = w1
        self.height = h1


Student.height = 175
print(Student.height)  # output --> 175
st1 = Student('Timur', 'Taylan', 78, 180)
print(st1.height)  # output --> 180
st1.height = 190
print(st1.height)  # output --> 190 --> contsructor değerleri class atritubutlerini o nesne için değiştirdi
print(Student.height)  # output --> 175
"""
class attributelerde bütün ensnelerde ortak olarak tanımlanmıştır.
Yani siz bir sınıftan nesne ürettiğinizde bu özellikler tüm nesnelerde aynıdır. İsim nonedir surname none vs

ancak instance attribute nesneden nesneye değişir. Zaten burdada self'in kullanım amacı ortaya çıkıyor
"""

"""
Eğer yapmak istediğimiz özellik ve değeri bütün sınıflarda ortak olmasını istiyorsak, biz bunu class attributesi
olarak tanımlamamı gerekiyor

Fakat her nesneden nesneye değişsin istiyorsak instance attribute olarak tanımlamamız gerekiyor. (init)

Mesela son yaptığımız örnekte isim soyisim width height tüm insanlarda vardır. Class attribute
ama insandan insana değişir. # instance attribute
Mantık bu

Dolayısıyla bu değişkenleri instance attribute olarak kullanmamız lazım SADECE
"""

print('*' * 45)

"""
self ifadesi hangi metodda kullanılırsa kullanılsın, o sınıfa ait nivknameyi taşıdığı için global değişken
işlevi görür. Dolayısıyla
"""


class Login:
    type = 'user'  # bütün giriş işlemi yapanlar user sayıldığı için bunu class attributesi şeklinde yazmak daha

    # mantıklıdır

    def __init__(self, _name, _password):
        self.name = _name
        self.password = _password

    def show_info(self):
        return self.password  # görüldüğü üzere self deyimi sayesinde password değişkenine ulaşabildim


l1 = Login('ruin', 'chain')
print(l1.name)
print(l1.show_info())

# class attrübutesi bütün nesnelerde ortaktır.
# ama instance attributesi nesneden nesye değişir
