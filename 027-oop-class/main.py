# ctrl + shift + u --> capitalize
"""
Nesneye yöneli̇mli̇ programlama bi̇r programlama di̇li̇ deği̇li̇dr
Python programlama dili 3 programlama paradigmasını destekler:
(Programlama paradigması bir programa yaklaşım bakış açısıydı ve yaklaşım biçimiydi

1-> Prosedürel Programlama: Python, prosedürel programlamayı destekler. Bu paradigmada, programlar sıralı adımlar
halinde çalışır ve işlevsel bloklar içerir.

2-> Nesne Yönelimli Programlama (OOP):
Python, nesne yönelimli programlamaya da uygun bir dil olarak tasarlanmıştır. Bu paradigmada, programlar objeler ve
sınıflar üzerine kuruludur. Python'da nesne yönelimli programlama sayesinde kodun düzeni ve
tekrar kullanılabilirliği artırılır.

3-> Fonksiyonel Programlama:
Python, fonksiyonel programlamaya da destek verir. Bu paradigmada, fonksiyonlar birinci sınıf nesnelerdir ve programlar
genellikle matematiksel fonksiyonların kombinasyonları olarak ifade edilir.

4->Bildirimci (Event-Driven) Programlama:
Python, olay (event) tabanlı programlamayı da destekler.
Bu paradigmada, programlar belirli olaylara tepki verir ve bu olaylar doğrultusunda çalışırlar.

Çok Paradigmalı Programlama: Python, çok paradigmalı bir dil olduğu için, gerekirse birden fazla programlama
paradigmını aynı program içinde kullanabilirsiniz. Bu, programcılara esneklik ve kodun ihtiyaçlarına uygunluğu sağlar.
"""

"""
NEDEN OOP:

1-> Modülerlik ve Kolay Bakım:
OOP, programı sınıflara ve nesnelere ayırarak modüler bir yapı oluşturmayı sağlar. 
Araba örneğinde, her araba bir nesne ve bu nesneler bir sınıf içinde tanımlanır. 
Bu modüler yapı, kodun daha düzenli ve bakımı daha kolay hale gelmesini sağlar. 
Örneğin, bir araba özelliklerini güncellemek veya yeni bir özellik eklemek istediğinizde sadece ilgili 
sınıfı düzenlemeniz yeterlidir

2-> Gerçek Dünya Modelleme:
OOP, gerçek dünyadaki nesneleri programlamak için doğrudan bir yol sunar. 
Araba örneğinde, her araba bir nesnedir ve araba özellikleri ile davranışları bir arada bulundurur. 
Bu, gerçek dünyadaki nesneleri daha iyi modellemeyi sağlar.

3->Veri Gizleme (Encapsulation):
Sınıflar, veri gizleme prensibini destekler. Bu, bir nesnenin içindeki verilere sadece o nesnenin metodları 
aracılığıyla erişilebileceği anlamına gelir. Örneğin, araba hızını değiştirmek istediğinizde, 
bunu araba nesnesinin metodları aracılığıyla yaparsınız, 
bu da hızın kontrolünü sağlar ve doğrudan dışarıdan müdahale edilmesini engeller.

4->
Kalıtım (Inheritance):
OOP'de kalıtım sayesinde bir sınıf, başka bir sınıftan özellikleri ve davranışları miras alabilir. 
Araba örneğinde, farklı tipteki arabaları temsil eden alt sınıflar oluşturabilir ve 
genel araba özelliklerini temsil eden ana sınıftan bu özellikleri miras alabilirsiniz.

5->Polimorfizm:
Polimorfizm, aynı isimdeki metodların farklı şekillerde davranabilmesini sağlar. 
Araba örneğinde, farklı marka veya modeldeki arabaların aynı metodları 
farklı şekillerde uygulamasına izin veren polimorfizmi kullanabilirsiniz.
"""
my_tuple = (1, 2, 2, 3)
print(type(my_tuple))  # output-> <class 'tuple'>


# yani pythondaki herhangi bir veri türü aslında arkaplanda class olarak yazılmıştır. Yani bir sınıftır
# sınıflar soyut varlıklardır. Kullanılmadığı takdirde bellekte yer tutmazlar
# my_tuple oluşturduğumuz için yer kapladı mesela.
# classlar sadece şablon oluşturmaya yararlar. Yani tanımlama işlemi yaparlar


class Car:  # CamelCase yapısı. Her kelimenin ilk harfi büyük
    # burdaki her değişken bu sınıfın bir ortak özelliğidir. Yani class attributesidir
    name = 'BMW'
    model = ''
    year = 0


print(Car)  # output-> <class '__main__.Car'> # insan bir class ama heniz yer tutmayan bir insan
print(Car())  # output-> <__main__.Car "OBJECT" at 0x0000028845> artık bellekte yer tutan bir insan.Ve de artık bir obje
# yani Car ve de Car() şeklinde yazmanın farkı var. Biri sınıfı temsil ediyor diğeri o sınıfın bir objesini
# yani nesne
# nesne = obje
Car()  # Obje = nesne
# classlar soyuttur Car, Ama nesneler car1 soyut değildir. Yer kaplarlar
car1 = Car()  # instance = referans
car2 = Car()
print(car1)  # output-> <__main__.Car object at 0x0000013F4F69C7D0>
print(car2)  # output-> <__main__.Car object at 0x0000013F4F69C740>

"""
peki neden instance yaratırız. Çüknü üretilen her nesnenin adresi farklı yerde olur
yukarıda gördüğün gibi her nesnenin yeri farklı oldu. Dolayısıyla biz ayırt etme işlemi yapmış oluruz
Bir değer faydası ben bu instancelerı kullanarak classdaki propertylere erişebilirim
"""

print(car1.name)
# eriştiğim gibi o sınıfın değerlerini de değiştirebilirim. Fakat sadece o nesne için değiştirebilirm

car1.name = 'AUDI'
print(car1.name)  # output -> AUDI
print(car2.name)  # output -> BMW -> Görüldüğü üzere şablonun name değeri değişmemiş.
# yapılan her değişiklik o nesne için geçerlidir


print(car1 == car2)  # false

# classlar sadece nesne üretmek için oluşturulurlar
