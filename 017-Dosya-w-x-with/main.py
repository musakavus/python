import os

# dosya işlemleri
"""
bir dosya işlemi herhangi bir uygulamanın önemli bir parçasıdır.
bu zamana kadar programlarımızda kullanıcyla etkileşime geçtiğimiz zaman bir değeri
değişkenlere atayıp kullanabiliyorduk. Ama bu program kapanana kadardı. Program
kapanınca bilgi de kayboluyordu.
Ama biz dosya işlemleri sayesinde bu değerleri dosyalarda tutup, bu değerleri okuyarak
çeşitli işlemler yapabiliriz. Yani bilgilerimizi geçici hafızadan kalıcı hafızalara taşımış oluruz
"""
# w modu: Write --> Yeni dosya yazma/oluşturma modu--> Eğer aynı isimde dosya mevcutsa o dosyasyı silip yenisini açar
# open('deneme.txt', 'w')  # path belirtmezsen bulunduğun dizini baz alır
# open('C:/Users/M/Desktop/FullStackk/Python/017-Dosya/deneme.txt', 'w') # bu şekilde path ve yanına da modu yazarsın

try:
    open('C:/Users/M/Desktop/FullStackk/Python/017-Dosya/deneme.txt', 'w')

except FileNotFoundError as err:
    print(err)
    print('Böyle bir dosya yolu yok')

# temelde open fonksiyonu iki paramtre alır. İlk parametre dizin,ikincisi de hangi işlemi yapazağımız.(ikiside str tipi

open('../metinbelgesi.txt', 'w')  # burda .. işareti bir üst klasöre çık demek

# x modu
"""
x modu da yeni bir dosya oluşturur. eğer aynı isimde dosya varsa yeni dosya açmaz hata verir
"""

# open('deneme.txt', 'x')
# aynı isimde dosya bulunduğu için file exist hatası aldık

# şimdi de bu hataya try except ile yön verelim

print('------------------')
try:
    open('deneme.txt', 'x')
except FileExistsError as err:
    print('dosya zaten mevcut')
    print(err)
else:
    print('Dosya oluşturuldu')

# w moduyla yazma

s = 'Hello worlds'
f = open('asd.txt', 'w')
f.write(s)
f.write('\n' + s)
# \n koymazsan imlec aşağı inmez
f.close()  # mümkün olduğunca kullan. Bazen  python tampon bellekten dolayı değişiklikleri anında işlemez
# ayrıca bizim işimiz bittiğinde dosyaları kapatmalıyız. yoksa arkaplanda çalıştığı için çok fazla bellek yer

# burası önemli
# amacımız sadece dosya oluşturmaksa x modülünü kullanırız
# amacımız dosya oluşturup içine bir şeyler yazmaksa w modülünü kullanırız

# bazen bir dosya oluşturma esnasında hata ile karşılaşabiliyoruz. dolayısıyla açtığımız dosya kapanmadığı için
# bellekten yiyebiliyor. O yüzden bu hatayı yönetebilmek ve gidermek için hata yönetimi yapmamız gerekebilir

print('----------------------------')
try:
    f = open('asd.txt', 'r')  # mesela kod burda patlayacak x kullandığımız için. Çünkü dosya zaten var
    # hata alacağımız için f.close() deyimi çalışmayabailir
    f.write('merhaba')
    f.close()
except Exception as err:
    print(err)

print('--------')

# dolayısıyla daha kesin çözüm için f.close() yi finally bloğunda yazmalıyız

try:
    f = open('asd.txt', 'x')  # mesela kod burda patlayacak x kullandığımız için. Çünkü dosya zaten var
    # hata alacağımız için f.close() deyimi çalışmayabailir
    f.write('merhaba')

except OSError as err:  # os kütüphanesi dosya işlemleri ile iligli genel hata kütüphanesidir
    print(err)
finally:  # böylelikle program hata verse de vermese de dosyamız kapatılmış oluyor
    f.close()

# Şimdi ikincive daha kısa yol olarak with deyimi de kullanılabilir. Yukarıdaki try except kullanmak yerine

with open('asd.txt', 'w') as f:
    # with deyimi sayesinde işimiz bittikten sonra dosya kendini kapatmış oluyor otomatik olarak
    # dolaysııyla f.close() kullanmamıza gerek yoktur
    f.write('hello world2')

# şimdi hangisini kullanmamız gerek diye soracak olursan-->
# hata yönetimi yapacaksak try except kullanmalıyız
# amacımız bu değilse with deyimini kullanmalıyız


