"""
Abstraction -> Soyutlama
Soyutlama dediğimizde bir sınıfı soyut hale getirmek ve bu sınıf içerisinde en az bir tane soyut metod tanımlamaktır

biz neden abstarct sınıflara ihtiyac duyarız
Çünkü soyut sınıflar şablon sınıflar olarak nitelendirilir. YANI NESNE ÜRETILEMEZ. Dolayısıyla bellekte yer işgal etmez

Şimdi soru??
Biz bu abstract classlardan nesne üretmeyeceksek neden kullanıyoruz bu sınıfları niye tanımlıyoruz
Bunun cevabı: Soyut sınıflar, başka sınıflar tarafından miras alınarak belli başlı işlemleri o sınıflara
yaptırmaya mecbur bırakırlar

Örneğin soyut vir sınıfta tanımlanan soyur bir metodu, eğer herhangi bir sınıf bir miras olarak alıyorsa,
burada tanımlanan metodu kendisi override etmek zorundadır.

Gerçek hayattan örnek verirsek
solunum nedir --> nefes alıp vermek --> abstract class görevi
bu konuda ayrıntıya girmek, akciğer, damar vs bunlar ise diğer sınıfların görevi

Yazılıma çevirirsek bunu-->
Büyük bir projeyi düşün. Onlarca sınıfta kullanılan onlarca ortak bir metod var diyelim.
O metodu o sınıfların kullanmasını şart koşmak istiyorsak, bunun soyut sınıf içerisine yazarız.
Bu soyut sınıftan miras alan child classlar bu metodu
override etmek zorunda kalır. dolayısıyla olası bir eksikliğin veya hatanın önüne geçmiş oluruz.

O metodları kullanmayı unutmayız. Çünkü o metodları kullanmayı zorunlu hale getiriyoruz.
Büyük bir ekipte buradaki tüm sınıfların aklımızda tutmanın zor olduğu bir kod tabanında
bize oldukça fayda sağlayacaktır

EN ÖNEMLİ FAYDASI "UNUTMAK" DİYE BİR KAVRAMI HAYATIMIZDAN ÇIKARIYOR
"""

# pythonda bir abstract belirtmenin doğrudan bir yolu yok. Mesela javada abstract ifadesi ile bu yapılır
# pythonda ise hazır bir modülü import etmemiz lazım. import abc

from abc import ABC, abstractmethod


class Phone(ABC):  # ABC sınıfından miras aldık
    # bir soyut sınıfın oluşturulabilmesi için mutlaka en az bir methoda ihtiyacı vardır
    @abstractmethod  # bunun bir abstract metod olduğunu bildirmek için @abstractmethod yazdık
    def send_message(self, message):
        pass  # içini doldurmuyorum. Çünkü ayrıntısı benim için önemli değil. O bunu miras alan sınıfın problemi

    @abstractmethod
    def call_someone(self):
        pass

    def islem(self):  # abstract sınıflarda abstract olmayan normal metodlard aolabilir. Ama çok kullanılmaz
        print('Herhangi bir şey')

    def __str__(self):
        return 'i am str method'

    def __repr__(self):
        return 'i am repr method'


class Iphone(Phone):
    def __init__(self, model, price, caller):
        self.__model = model
        self.__price = price
        self.__caller = caller

    def send_message(self, message):  # abstract metodun içindekinin aynısı olmalıdır.Metod ismi ve paramtre aynı olmalı
        print('Message: ', message)  # bir parametreyi sadece çağırıldığı fonksiyondan kullanacaksna self kullanma

    def call_someone(self):
        print(self.__caller, 'is calling...', )


class Redmi:
    pass


# i1 = Iphone() # hata --> output-->
# Can't instantiate abstract class Iphone without an implementation for abstract methods 'call_someone', 'send_message'
# Çünkü bu esnada Iphone classı içerisinde o metodlar yoktu
# p1 = Phone() # hata --> abstract classlardan nesne üretilemez

i2 = Iphone('Xs-Max', 19999, 'Ramazan İkinci')
print(i2)  # str metodu çalıştı repr çalışmadı. Çünkü varsayılan str metodu, ikiside kullanılmışsa
i2.send_message('hi i am message text')
i2.call_someone()
# UNUTMA. CHILD CLASS, ABSTRACT CLASSDAKI METODLARI OVERRIDE EDER. EZER ONLARI

i2.islem()  # child classta bu metodu oluşturmama rağmen bu referans üzerinden ulaşabildim. Çünkü inheritance
# parent classdan bir metodu child classta rahatlıkla kullanabiliyordum hatırla.
# Fakat bir fark var. Override işlemi gerçekleşmedi. Çünkü abstract method olarak tanımlamadık
"""
repr ve str metodu abstractta oluşturduk ama miras alan sınıflarda oluşturmadık. Peki neden hata almadık.
Çünkü python bu str ve repr sınıflarını bizim için arkaplanda oluşturuyor
"""

"""
SOYUT BIR SINIFIN SOYUT YÖNTEMLERINI MIRAS ALAN ALT SINIFLARDA AYNI IMZAYA SAHIP OLMASI GEREKLIDIR. 
YANI, ALT SINIFTA SOYUT YÖNTEMI AYNI ISIMLE VE AYNI PARAMETRELERLE UYGULAMAK ZORUNDASINIZ.
"""

"""
class MyClass:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"MyClass instance with x={self.x}"

    def __repr__(self):
        return f"MyClass({self.x})"

obj = MyClass(5)

# str ve repr metodları birlikte kullanılabilir
print(str(obj))  # MyClass instance with x=5
print(repr(obj)) # MyClass(5)

peki print(obj) dediğim zaman str metodu mu çalışır yoksa repr metodu mu
print(obj) ifadesi çalıştığında, Python varsayılan olarak repr metodu yerine str metodu çalıştırır. 
Bu, print fonksiyonunun daha teknik bir çıktı üretmesini sağlar ve bu çıktının daha fazla bilgi sağlamasınaolanak tanır.

Eğer __str__ metodu tanımlanmışsa ve __repr__ tanımlanmamışsa, print(obj) çağrıldığında __str__ metodunun sonucu 
gösterilir. Ancak, hem __str__ hem de __repr__ metodu tanımlanmışsa, 
print(obj) çağrıldığında varsayılan olarak __str__ metodu çalışır.

Ayrıca repr ve str metodları muhakkak bir return değeri almak zorunda
"""
# dipnot abstract sınıflar başka sınıfları da kendine miras alabilir. Fakat yine de bunu yapmayalım. Çünkü
# ismi üzerinde şablon sınıf. Ne gerek var başka sınıflardan da miras almaya. Miras versin yeter
# yada abstract classdan miras alan bir child class, başka sınıfları da miras alabilir. Multi lvl ve multi inheritance
# hatırla
