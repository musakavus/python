"""
Overriding
overriding ezmek iptal etmek ağır basmak anlamına gelir
"""


class Users:
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

    def info(self):  # aynı isimde ve aynı değerlerde olacak. SAdece içeriği değişecek
        print(self.username + ' logged in')


class Moderator(Users):
    def __init__(self, _username, _password, _permission):
        super().__init__(_username, _password)
        self.permission = _permission

    def info(self):
        super().info()  # eğer base classtaki metodu da çalıştırmak istiyorsak super funcu kullanabiliriz
        # yani super metodu sadece init fonksiyonlarda değil instance metodlarda da kullanılabilir
        print(self.username + ' logged in and he has ' + str(self.permission))


u1 = Users('user', 'chain')
u1.info()
print('*' * 45)
m1 = Moderator('admin', 'admin', True)
m1.info()

# super metodu sadece child classlarda çalışır
# dikkat edilmesi gereken bir konuda şu super metodu sürekli en üste yazılmalıdır metodun
# fakat python bu esnekliğe izin veriyor ama sen yine de genel kaideye uy


"""
Şurası önemli çalışma mantığı açısından-->
sub classdan nesne üretip çalıştırdığın zaman python önce info diye bir method var mı bakıyor
varsa child classdaki o methodu çalıştırıyor. Base class'a bakmıyor 

şayet info methodu child classında yoksa gidip base class'a bakıyor. Ordakini çalıştıyır

Kısaca overriding ezme mantığı böyledir
"""

# __bases__ dunder methodu ile bir chiild classın base classını öğrenebiliriz
print(Moderator.__bases__)
