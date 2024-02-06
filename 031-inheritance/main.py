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


