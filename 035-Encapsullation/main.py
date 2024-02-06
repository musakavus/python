class Users(object):
    counter = 0

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self, a_user):
        # bu şekilde yaparmak info hiding yapılan bir elemente gğvenli yollardan erişsmiş oluyoruz
        print(f'{a_user} kullanıcısı görüntülendi')
        self.counter = self.counter + 1
        return self.__username

    def get_password(self):
        return self.__password

    def set_username(self, value):  # set işlemiyle private değişkenler üzerinde değişiklikler yapabiliriz
        self.__username = value

    def set_password(self, value):
        if len(value) >= 5:
            self.__password = value
            print('Parola başarıyla güncellendi.')
        else:
            print(f'Parola güncellenemedi!')

    def __str__(self):
        return f'Toplam profil görüntülenmesi: {self.counter}'


class Moderators(Users):
    pass


u1 = Users('ruin', 'chain')
username_data = u1.get_username('Musa')
print(username_data)

u1.set_username('a_username')
u1.set_password('*****')
new_username = u1.get_username('Ramazan')
new_password = u1.get_password()
print(f'Yeni kullanıcı adı: {new_username}\nYeni parola: {new_password}')

print(u1)  # = print(u1.__str__())  output-> Toplam profil görüntülenmesi: 2
"""
Kısaca 
info hiding --> değişkenleri ve metodları gizleme
encapsullation --> bu private elementlere güvenli biçimde dışarıdan erişbeilme'yi sağlar

ee şimdi soracaksın--> Madem değişiklik ,güncelleme, okunabilir yapabiliyoruz o zaman neden gizliyoruz->
Cevap oldukça basit: -> çünkü bu değişiklikler bizim kontrolümüz altında gerçekleşiyor

Ayrıca okunabilir yapmak istemiyorsak get kullanmak zorunda değiliz. Sadece set metodu da yapabiliriz. 
"""
