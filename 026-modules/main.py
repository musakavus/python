# modüler python
"""
pythonda neden modül kullanırız
çünkü büyük pragramları küçük ve yönetilebilir hale getirmek isteriz. Organizasyonları daha kolay hale gelir
Bu yüzden ayrı ayrı py dosyalarına yazarız. İhtiyacımız olduğu zamanda çağırıp kullanırız.
Ayrıca DRY dont repeat yourself mantığına da uygundur

Pythonda kullanılan 3 tür modül vardır

1-> Bizim kendimizin projemiizde oluşturduğu modüller
2-> Python kurulumu ile gelen hazır modüller
3-> Python geliştiricilerin ürettiği pypi modülleri

import calculate  # as deyimi ile lakap takabilirim
from calculate import * # bütün her şeyi import et
bu ikisi arasındaki fark şudur. İkiside her şeyi import ediyor
Ama birincisini tanımlarsan fonksiyonu çağırırken calculate. kullanmalısın
İkincisinde modül ismi yazmana gerek yok direk fonksiyon ismini yazman yeterlidir
"""
import calculate
import calculate as calc  # as deyimi ile lakap takabilirim
from calculate import *  # bütün her şeyi import et
from calculate import divi  # böyle bir yapıda var. Bu demek oluyor ki sadece divi kullanmak istiyorum
from calculate import divi as divar  # yada bu
from calculate import mult, summ  # yada bu

while True:
    try:
        number1 = float(input('Enter number 1: '))
        number2 = float(input('Enter number 2: '))

    except ValueError as err:
        print(err, 'Try again')

    except KeyboardInterrupt as err:
        print('\nProgram cancelled')
        print(err)

    else:
        result = calc.summ(a=number1, b=number2)
        result2 = calc.subs(a=number1, b=number2)
        result3 = calc.mult(a=number1, b=number2)
        result4 = calc.divi(a=number1, b=number2)
        print(f'Addition: {result}\nSubstraction: {result2}\nMultiplication: {result3}\nDivision: {result4}')
        break

data = calc.__doc__  # modülün açıklamasını gösterir
print(data)
data = calc.__name__  # modülün ismini yazar
print(data)
data = calc.__file__  # dizin belirtir
print(data)

print(divi(3, 1))  # from calculate import divi

print(summ(3, 5.9))  # from calculate import *


# misal burda summ aynı isimde bir func oluşturdun. O zaman ne olur

def summ(a, b):
    return 'main summdan  gelen return'


print(summ(5, 7))  # hangisi çalışır. Burdaki mi yoksa diğer modüldeki mi???
# cevap oldukça basit. Python yukarıdan aşağıya doğru çalışır. Dolayısıyla hangisi daha altta ise
# en son o derleneceği için o çalışır


# STANDART MODULE NEDİR
"""
Python dosyasını bilgisayarımıza kurduğumuza zaman pythonun yüklendiği yerde
lib diye klaösr var. Bu lib dosyası içinde bulunan modüllere standart modül denir
"""

# STANDART OLMAYAN MODULE NEDİR
"""
pythonla beraber gelmeyen, bizim pypi ile manuel eklediğimiz modüllerdir.
pypi.org sitesinde bu modüllere ulaşılabilir.
Örneğin numpy kütüphanesini yüklemek için pip install numpy -> kaldırmak için pip uninstall numpy
indirdikten sonra bu modül venv-> lib--> site-packages dizininde bulur
"""

import sys

print(dir(sys))  # dir fonksiyonu bir modülün veya yapının sahip olduğu fonksiyonların tümünü gösterir
"""
örneğin burda sys modülünün sahip olduğu fonksiyonları görüyoruz
#sys kütüphanesi->
sys.exit() -> Programı sonlandırmak için kullanılır. Belirli bir çıkış durumuyla birlikte kullanılabilir.

stdin, stdout, stderr--> Standart giriş, çıkış ve hata akışlarını temsil eden nesneleri sağlar.
read, readline, readlines, write, writeline, writelines
-->read(size=-1): Bu metod, standart girişten belirli bir boyuttaki veriyi okur. 
Eğer size belirtilmez veya -1 olarak ayarlanırsa, tüm girişi okur.
--> readline(size=-1): Bu metod, standart girişten bir satır okur. 
Eğer size belirtilirse, en fazla belirtilen boyutta bir satır okur.
-->readlines(hint=-1): Bu metod, standart girişten bir dize listesi olarak satırları okur. 
Eğer hint belirtilirse, en fazla belirtilen bayt sayısında veri okur.
version: Python yürütülen sürüm bilgisini içerir.

 Python'ın modül arama yolu olan sys.path listesini içerir.
"""
data = sys.stdin.readline()  # Örneğin, stdin'den veri okuma  -> data = input()
sys.stdout.write(data)  # print(data)  --> line zaten c# hatırlayacağın üzere alt satıra in
sys.stderr.write('this is a error message')  # -->

print(sys.version)  # python versiyonunu öğrenmek için

sys_path = [value for value in sys.path]
for value in sys_path:  # yada kısaca print([value + '\n' for value in sys.path])
    print(value)

mylist = [1, 2, 3, 4, 5]
print(mylist)  # output -> [1, 2, 3, 4, 5]
print(*mylist)  # output  -> 1 2 3 4 5  --> böyle bir şey var ÖNEMLİ ->printle çalışıyor


"""
şimdi şöyle bir şey var. Programlarımızda 3 tür modülü de kullanabiliriz
Ama uymamız zorunlu olmasa da bazı pep8 kuralları vardır. Ve buna uysak iyi olur
modülleri en üstte yazarken en üstte
1- standar kütüphaneler --> pythonun kurulu olduğu yerde. Her python projesinde zaten otomatik olarak yüklüdür
Çünkü python kurulumu ile ortam değişkenleri otomatik eklenir. 
2- Bizim yüklediğimiz modüller
3- pip ile yüklediğimiz modüller

Örnek kod yazılımı şöyledir: Araların boşul bırak ve sıralamaya diikat

import sys -> standart modüller
import math
import os

import calculate -> bizim modül

import numpy -> 3.part modüller

modül ve kütüphane kavramı aynı olmakla beraber aralarında ufak bir fark vardır. Modül tek bir dosya barındırır
kütüphane birden fazla

Örneğin sys modülü tek dosyadan oluşur
ama pqt bir kütüphanedir. Çünkü içinde birden fazla dosya bulunduruyor. Kısaca kütüphane daha gelişmiş bir yapıdır
"""