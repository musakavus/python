class Users:
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

    def info(self):
        print('Welcome User!')


class Customers(Users):
    def __init__(self, _username, _password, _budget):
        super().__init__(_username, _password)
        self.budget = _budget

    def info(self):
        print(self.username + ' logged in! You are a customer')


class Moderators(Customers, Users):
    def __init__(self, _username, _password, _budget, _editing_status):
        super().__init__(_username, _password, _budget)
        self.editing_status = _editing_status

    def info(self):
        print(self.username + ' logged in! You are a Moderator.'
              + ' Editing Status: ', self.editing_status)


class Administrators(Moderators, Customers, Users):
    def __init__(self, _username, _password, _budget, _editing_status, _deleting_status):
        super().__init__(_username, _password, _budget, _editing_status)
        self.deleting_Status = _deleting_status

    def info(self):
        print(self.username + ' logged in! You are a administrator!'
              + ' Editing Status: ', self.editing_status, ' Deleting Status: ', self.deleting_Status)


u1 = Users('ruin_user', '****')
u1.info()

c1 = Customers('ruin_customer', '*****', 9999)
c1.info()

m1 = Moderators('ruin_moderator', '****', 9998, True)
m1.info()

a1 = Administrators('ruin_admin', '****', 9999, True, True)
a1.info()

# MRO sıralamasına dikkat. child->dad->granddad-> ... etc ÖNEMLİ
# Misal admin için -> Moderators -> Customers -> Users
# admin bir moderatördüe, aynı zamanda bir customerdir aynı zamanda bir userdir

print(Administrators.__mro__)
# output-> (<class '__main__.Administrators'>, <class '__main__.Moderators'>, <class '__main__.Customers'>,
# <class '__main__.Users'>, <class 'object'>)
# Bu fonksiyon sayesinde sıralamayı görebiliriz


"""
multi level inheritance de mantık şu->
Administrator class'ı Moderatör classını miras aldığına göre
Moderatör sınıfı da Customers ve USers sınıfını miras aldığına göre-->

Mantıken administrator classı, Customers ve Users sınıfını da mmiras almış olur


Aslında bir classın bu kadar çok miras alması tavsiye edilmez. 
Aslında bir programlama dilinde kalıtım çok fazla gerekli olmadığı sürece kullanımı pek tavsiye edilmez. 
->Çünkü Kalıtım, programın mantıksal karmaşıklığını 
artırabilir. Alt sınıflar, üst sınıfların özelliklerini ve davranışlarını miras aldığı için 
kodun anlaşılması ve bakımı zorlaşabilir.

->Alt sınıflar, üst sınıfların özelliklerini doğrudan miras alırken, gereksiz özellikleri veya davranışları da miras 
alabilir. Bu durumda, alt sınıfların esnek olmaması ve bağımlılıkların artması söz konusu olabilir.
"""


class Animal:
    def __init__(self, _name):
        self.name = _name

    def info(self):
        print('You are an animal', self.name)


class Cat(Animal):
    pass


class Tiger(Cat):
    pass


class RedTiger(Tiger):
    pass


"""
burda red_tiger Tiger class'ını miras aldığı için
tiger classı da cat classını miras aldığı için
Cat classıda Animal classını miras aldığı için -->
RedTiger classı Animal classını da miras almış sayılır
"""

rt1 = RedTiger('Gnar')  # görüldüğü üzere paramtre olarak name istiyor
rt1.info()  # ve görüldüğü üzere info() metodu çalışıyor
