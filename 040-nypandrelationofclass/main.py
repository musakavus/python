"""
OOP presinpleri ve sınıflar arası ilişkiler
"""
"""
OOP 4 prensip
1-> inheritance
2--> polymorpihizm (çok biçimlilik)
3--> Encapsulation
4--> Abstract Soyutlama
"""

"""
biz sınıflar arasındaki bu ilişkiyi neden kuraruz
1-> bir kodun yeniden kullanılabilirliğini artırmak
2-> kodun tekrar etmesini önlemek
3-> sınıflar bir birleri ile ilişki kurarken olabilidğince esneklik sağlamalıdır.
4-> bir sınıf diğer sınıfa bağımlı olmamamlıdır
    Biz sınıflar arasında bu ilişkiyi kurarken kalıtım kullanmıştık. Kalıtımın bazı dezavantajları vardır bu yüzden
    kalıtım kullandığımızda, üst sınıFIN ÖZELLİKLERİ VE METODLARI CHİLD CLASSTA YER ALMAYA DEVAM EDER
    Dolayısıyla kalıtım bize esnek bir yapı sunmaz. Çünkü bir sınıfa tamamen bağımlı olmak demek
    Bir sınıfta yapılan değişiklik, bütün sınıflara etki eder

"""


class User(object):
    def __init__(self, username, password):  # kalıtımın en büyük problemi şudur.
        # Parent sınıfta bir değişiklik yapıldığı zaman bu değişiklik tüm sınıflara yansır
        # mesela init metoduna yeni bir değişken ekledik. Gidip bunu chiild classların hepsine uygulamamız lazım
        self._username = username
        self._password = password

    def login(self):
        print(self._username, ' logged in')


class Moderator(User):  # misal password değişkeni parentta var ama moderator classında hiç kullanmamışız.
    # parola değişkenini kullanmadığımız zaman burda hata olmaz ama modelleme olarak hata vardır.
    # OOP prensibine pek uymaz
    # kalıtım kullanımı kolay görüldüğü için oop'ye yeni başlayanlarbu bunun gibi hataları her yerde yapıyor
    def __init__(self, username, password, editable):
        User.__init__(self, username, password)
        self._editable = editable

    def login(self):
        print(self._username, ' logged in')


class Admin(Moderator, User):
    def __init__(self, username, password, editable, deletable):
        super().__init__(username, password, editable)
        self.deletable = deletable


"""
şimdi kalıtımı kullanabilmek için alt sınıfın, bir üst sınıftaki tüm özellikleri temsil ediyor olması lazım.
Zorunlu değil ama modelleme açısından en doğrusu budur
"""


# diyelim ki cat ve dog sınıfında name, age değişkenlerini kullanmak istiyorum.
# Ama bunu kalıtım oolmadan yapmak istiyorum
# peki kalıtım olmadan nasıl yapacaz.Değişkenleri baştan mı yazacaz. Hayır. OOP de amaç kendini tekrarın önüne geçme
# HOP ASSOCIATION devreye giriyor
class Cat:
    pass


class Dog:
    pass


"""
Association: Bir sınıfın bir şekilde başka bir sınıfı sahiplendiği ve has-a ilişkisini kullandığı türdür.
Bir sınıfın özelliklerini kullanmak için kalıtım yapmak şart değildir. Çeşitli ilişkiler sayesinde vir veya daha fazla
sınıfın özelliklerini kullanabiliriz.
Association, nesneleri üretilen iki ayrı sınıfın arasındaki bağlantıdır. Bu bağlantı sayesinde bir sınıfın başka
bir sınıf hakkında ne kadar bilgi sahibi olduğunu öğrenebiliriz.
4 ilişki çeşidi vardır.
1-> One to one --> bir insan bir kimliğe sahiptir. bir kimlik sadece bir insana aittir. Kimlik ve insan verilerini
iki ayrı nesne olarak düşündüğümüzde aralarında böyle bir ilişki vardır
2-> one to many --> Bir bankanın birden fazla personeli olabilir. Ama bir personelin çalıştığı tek bir banka vardır
3-> many to one --> Bir çok şehrin sadece bir ülkesi vardır.Ama her şehrin bir ülkesi vardır
4-> many to many --> Bir bankanın birden fazla müşterisi olabilir. Veya her müşterinin birden fazla bankası olabilir
a-> Aggregation
b-> Composition
"""


