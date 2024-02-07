"""
Çok biçimlilik

Polymorphism farklı durumlarda farklı türleri farklı yapıları temsil etmek için tek bir ifade kullanma biçimidir
Yani bir operatörün, nesnenin ya da fonksiyonun farklı biçimlerde ortaya çıkma durumudur. 4 türde kullanılır

1-> Fonksiyonlar
2-> Operatörler
3-> Sınıflar ve metodlar
4-> Kalıtım
"""

# fonksiyon

v1 = len('Merhaba')
v2 = len([1, 2, 3, 4])
v3 = len((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
v4 = len({'data1': 'kitap', 'data2': 'kalem'})

print(v1)  # len fonksiyonu polymorphizme bir örnektir
print(v2)
print(v3)
print(v4)

# operator
k1 = 'Merhaba'  # + operatörü hem toplama işlemi yapar hem string birleşimi yapar. Polymorpihzme örnektir
k2 = ' Python'
k3 = 10
k4 = 20
print(k1 + k2)
print(k3 + k4)

print('-' * 45)


# sınıflar metodlar
class Trendyol:
    def __init__(self, p_name, p_price):
        self.__p_name = p_name
        self.__p_price = p_price

    def info(self):
        print(f'Product name: {self.__p_name}\nProduct Price: {self.__p_price}')

    def get_p_name(self):
        return self.__p_name

    def get_p_price(self):
        return self.__p_price

    def set_p_name(self, value):
        self.__p_name = value

    def set_p_price(self, value):
        self.__p_price = value

    def __repr__(self):
        return f'data showed!'


class HepsiBurada:
    def __init__(self, p_name, p_price):
        self.__p_name = p_name
        self.__p_price = p_price

    def info(self):
        print(f'Product name: {self.__p_name}\nProduct Price: {self.__p_price}')

    def get_p_name(self):
        return self.__p_name

    def get_p_price(self):
        return self.__p_price

    def set_p_name(self, value):
        self.__p_name = value

    def set_p_price(self, value):
        self.__p_price = value

    p_name = property(get_p_name, set_p_name)
    p_price = property(get_p_price, set_p_price)

    def __repr__(self):
        return f'data showed!'


t1 = Trendyol('iPhone', 9999)
h1 = Trendyol('Samsung', 7999)

for element in (t1, h1):  # ince t1'i geziyor. sonra h1'i geziyor
    element.info()  # bunlar overriding işlemi değildir. Karıştırmayalım. Çünkü overriding inheritance varsa olur
    print(t1)
    t1.p_name = 'Lenovo'
    print(t1.p_name)

print('-' * 45)


class Users(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f'{self.username} user olarak giriş yaptı')


class Moderators(Users):
    def __init__(self, username, password):
        Users.__init__(self, username, password)

    def login(self):
        print(f'{self.username} moderator olarak giriş yaptı')


class Admins(Users):
    def __init__(self, username, password):
        super().__init__(username, password)

    def login(self):
        print(f'{self.username} admin olarak giriş yaptı')


u1 = Users('a_user', '123214')
m1 = Moderators('a_moderator', '123214')
a1 = Admins('an_admin', '123214')
my_list = [u1, m1, a1]  # for döngüsününde bu listeyi kullanarak da aynı işlemi gerçekleştirebilirsin

for element in (u1, m1, a1):  # burda overriding işlemi oldu. Polymoprhism inheritanceda da geçerlidir
    element.login()
