"""
INHERITANCE
"""

"""
users
moderator
"""


# miras alınan sınıf, parent class, base class
class Customer:
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

    def login(self):
        return f"User {self.username}'s user logged in!"


# miras alan sınıf, alt sınıf, child class, subclass
class Moderators(Customer):  # burda diyoruz ki bir nevi-> yönetici de bir müşteridir
    pass


c1 = Customer('ruin', 'chain')
print(c1.login())  # output--> User ruin's user logged in!

m1 = Moderators('admin', '1231213')
print(m1.login())  # outpur --> User admin's user logged in!
"""
Unutulmaması gereken şu. Base classtaki tüm özellikleri child classta kullanabiliriz.

inheritance bağlantısı kurarken şu soruyu sorman lazım. Her moderatör bir kullanıcı mıdır? 
Her moderatör, kullanıcıların tüm özelliklerini karşılar mı??

Eğer base classda oluşturulan herhangi bir özelliği child class kullanmayacaksa, KESİNLİKLE INHERİTANCE YAPILMAZ
(elbette bunu bazı yolları vardır ama oop mantığına terstir
"""

"""
Super() fonksiyonu
"""


class Animal:
    def __init__(self, _name, _type, _action):
        self.name = _name
        self.type = _type
        self.action = _action

    def register(self):
        print(self.name + ' added')

    def __repr__(self):
        return f'Name: {self.name}, Type: {self.type}, Action: {self.action}'


class Cats(Animal):
    def __init__(self, _name, _type, _action, _jumping):
        super().__init__(_name, _type, _action)  # super metodu miras alınan sınıfın özelliklerine erişmemizi sağlıyor
        self.jumping = _jumping

    def __str__(self):
        return f'Jumping: {self.jumping}'


a1 = Animal('Tiger', 'Cat', True)
a1.register()
print(a1)
print('*' * 45)
c1 = Cats('Tiger', 'Cat', True, True)
print(c1.__repr__())
c1.register()
print(c1)

# unutma base classta olulturulan her değişkeni her metodu child classta kullnabilirsin
