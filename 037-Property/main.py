"""
PROPERTY
"""


class Users(object):
    def __init__(self, username, password):
        self.__username = username
        self.set_password(
            password)  # burda bir kontrol işlemi gerçekleştirmek istedik ve setpass metodunu çalıştırdık
        # böyle kontroller için önerilen yapıda budur. Bu ifadede doğru sıkıntı yok self.__password = password
        # sadece maksat init fonksiyonunda bu kontrolü sağlamak. bu daha mantıklı. Kafan karışabilir. Sağlam kafayla

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_username(self, value):
        self.__username = value

    def set_password(self, value):
        if len(value) >= 7:
            self.__password = value
        else:
            raise ValueError('Parola 6 karakterden fazla olmalıdır!')

    def info(self):
        print(f'Username: {self.__username}\nPassword: ' + '*' * len(self.__password))

    username = property(get_username, set_username)  # prop bunları ilgili metodlara yönlendiriyor
    password = property(get_password, set_password)  # aynı şekilde. Fonksiyon şeklinde yazmıyorsun. Parantez yok Dikkat


class Moderator:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password  # burdaki atama işlemi üsttekinden farklı.Farketmez.zaten direk propa yönlendirliyor

    @property  # bu da yine bir başka prop yöntemi
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @username.deleter
    def username(self):
        del self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 7:
            self.__password = value
        else:
            raise ValueError('Parola 6 karakterden fazla olmalıdır!')

    @password.deleter
    def password(self):
        del self.__password


u1 = Users('admin', '12sasadsa')
u1.info()
u1.set_username('admin2')
u1.info()
print('-' * 45)
u1.username = 'Ahmet'
u1.info()
print('-' * 45)
u1.password = '784sadsaasdsadsadsadsadsa'  # atama işlemi yapılabilir böyle --> diğer türlü u1.set_password('sfsagoksg')
# burda set işlemi yaptığımız için propertyde sadece set özelliği çalışıyor

print(u1.password)  # burada görme işlemi yaptığımız için propertyde sadece get özelliğği çalışıyor

"""
Ancak her ne kadar böyle bir kullanım yapsak da ve tüm dünyada get ve set metodları böyle kullanılsa da
PYTHON'da böyle bir kullanım tavsiye edilmez. Onun yerine property'ler kullanılır.

Görüldüğü üzere referans ve atama işlemlerinde daha az kod yazdık.
"""

m1 = Moderator('ramazan', 'ikincii')
m1.username = 'Musa'
print(m1.username)
m1.password = 'sadsadsadsadsa'
print(m1.password)
