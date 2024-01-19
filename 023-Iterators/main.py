"""
Bir nesnenin "iterable" olması, üzerinde döngü işlemleri yapılabilir olduğu anlamına gelir.
Yani, bu nesneler üzerinde eleman eleman dolaşmak mümkündür.
List, tupple, set, dict

iterable = Gezilebilen nesne
iterator = Sayılabilen sayıda değer içeren nesne

Yani for döngüsünde gezebiliyorsak bu for döngüsü sayesinde oluyor

iki tane fonskiyon kullanırız
1-> iter fonksiyonu --> Nesnelere iterasyon özelliği sağlar
2-> next fonksiyonu --> next fonksiyonu sayesinde de, bu iterasyon özelliğine sahip nesneleri tek tek gezebiliyoruz
"""

my_list = [1, 2, 3, 4, 5]
for value in my_list:
    print(value)

data = iter(my_list)
print(type(data))  # <class 'list_iterator'>

# eğer --> print(next(my_list)) --> dersem hata almış olurum. Çünkü my_list iteratör değildir. Çünkü next deyimi
# sadece iteratör özelliğine sahip yapılarda çalışır
# Atama yaptığım my_list'i iter fonksiyonu ile tanımladığım data değişkeni iterdir
try:
    print(next(my_list))
except TypeError as err:
    print(err)
    # output--> 'list' object is not an iterator
finally:
    print(next(data))  # output: 1
    print(next(data))  # output: 1
    print(next(data))  # output: 1
    print(next(data))  # output: 1
    print(next(data))  # output: 1
    # Aslında hali hazırda bu işlemin aynısını for döngüsü de yapıyor.
    # print(next(data))  # eleman sayısı aştığımız için hata verir

print('----------')
my_cars = {'car': 'bmw', 'vitesse': 'auto', 'type': '4*4'}
my_cars_data = iter(my_cars)
while True:
    try:
        print(next(my_cars_data))

    except StopIteration as e:
        # burda hata metni yazılmaz. çünkü Python döngüdeki StopIteration hatasını otomatik olarak ele alır
        # ve döngüyü sonlandırır.
        break
