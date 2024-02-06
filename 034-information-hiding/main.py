"""
Encapsullation
"""


#
# class User(object):  # bu sınıfın parent olduğunu geliştiriciler bildirmek için object ifadesini kullanırız
#     def __init__(self, _username, _password):
#         self.username = _username
#         self.password = _password
#
#     def login(self):
#         print(f'{self.username} logged in user method')
#
#
# class Moderator(User):
#     def __init__(self, _username, _password, _permission):
#         User.__init__(self, _username, _password)  # super fonksitonunu bir nevi böylede bildirebiliriz.
#         # Tabi ekstra oalrak self ifadesi de parametre olarak eklenmelidir sınıf temsiliyeti için
#         # super().__init__(_username, _password)
#         self.permission = _permission
#
#     def login(self):
#         print(f'{self.username} logged in with mederation method')
#
#
# u1 = User('ruin', '****')
# u1.login()
# u1.password = 123123
# print(u1.password)  # bu işlem böyle kolay olmamalı. Çünkü ben kullanıcının parolasını istediğim gibi
# # görebiliyorum değiştirebiliyorum. Yani bu bir nevi nilgi kaçırmak anlamına geliyor
# # bizim bu bilgileri saklamamız lazım. Çünkü bunlar öenmli bilgiler. Dolayısıyla böyle kolay değiştilmemeliler
#
# print('*' * 45)
# m1 = Moderator('admin', '*****', True)
# m1.login()


# class User(object):
#     def __init__(self, username, password):
#         self._username = username  # protected --> miras alınan sınıf üzerinden ulaşılabilir
#         self._password = password
#
#     def info(self):
#         print(f'{self._username} logged in with user method')
#
#
# class Moderation(User):
#     def __init__(self, username, password):
#         super().__init__(username, password)
#
#     def info(self):
#         print(
#             f'{self._username} logged in with user method')
#         # görüldüğü gibi username base classta protected olarak bildirildiği için child classta ulaşabildim
#
#
# u1 = User('user', '121123')
# m1 = Moderation('moderator', '****')
# u1.info()
# try:
#     print(u1.username)  # burda hata alırım
# except AttributeError as err:
#     print(err)  # -> output--> 'User' object has no attribute 'username'
#
# m1.info()  # hata almadım. Çünkü child class üzerinden ulaşabiliyorum
# print(m1.username)  # vefakat m1 üzerinden ulaşım sağlayabilmeme rağmen her şeyi yapamam.
# # misal bu şekil direk print fonksiyonunu kullanamam. Yada m1.username = '' üzerinden değişiklik yapamam


class Users(object):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def info(self):
        print(f'welcome {self.__username} and you are a user')


class Moderators(Users):
    def __init__(self, username, password, permission):
        super().__init__(username, password)
        self.__permission = permission

    def __info(self):  # private method
        print(f'welcome {self.__username} and your permission status: {self.__permission}')

    def info2(self):
        print(f'your permission status: {self.__permission}')


u1 = Users('ruin_user', '****')
u1.info()  # çalışır
# print(u1.__username)  # hata --> değişkenlere ulaşamazsın
# u1.__username = 'admin' # hata --> değişiklik yapamazsın. Çünkü priavte değişkenlerdir

m1 = Moderators('admin', '****', True)
m1.info()  # burada hata almadım. Çünkü her ne kadar child class içindei metod private olsa bile,
# parent classta public olduğu için sorunsuzca ulaşabildim
m1.__info()  # hata. Private metoda ulaşılamaz
m1.info2()
"""
Private metoda sadece içinde bulunduğu sınıf tarafından ulaşılabilir. Inheritance yoluyla da bu mümkün değil
OOP ETİĞİNE VE MANTIĞINA HİÇ BİR ŞEKİLDE PRİVATE BİR DEĞİŞKENE YADA METODA DIŞARIDAN ERİŞİLEMEZ
GENEL KULLANIM METODLARIN PUBLIC OLUP DEĞIŞKENLERIN PRIVATE OLMASIDIR
"""
