# Python'da bir liste, köşeli parantezler içinde virgülle ayrılmış öğelerden oluşur.
my_list = [1, 2, 3, 4, 5]

# boş liste
empty_list = []

# Liste elemanlarına sıfır tabanlı index kullanarak erişebilirsiniz.
first_element = my_list[0]
print(first_element)

# Liste elemanlarını index kullanarak güncelleyebilirsiniz.
my_list[0] = 0
first_element = my_list[0]
print(first_element)

# len() fonksiyonu ile listenin uzunluğunu öğrenebilirsiniz.
list_count = len(my_list)
print(list_count)

"""
append(): Listenin sonuna eleman ekler.
insert(): Belirtilen index'e eleman ekler.
"""
my_list.append(6)
print(my_list)
my_list.insert(3, 9)
print(my_list)

"""
remove(): Belirli bir değeri siler.
pop(): Belirli bir index'teki elemanı siler ve sildiği elemanı döndürür.
del: Belirli bir index'teki elemanı siler.
"""

my_list.remove(0)  # indisi değil dizideki elemanı belirtmek lazım
print(my_list)
popped_element = my_list.pop(4)
print(my_list)
print(popped_element)
del my_list[1]
print(my_list)
# pop fonksiyonunun del'den farkı pop fonksiyonu değer döndürür

"""
For Döngüsü ile Liste Gezme:
Listedeki her elemanı döngü ile gezebilirsiniz.
"""

my_list2 = ['new york', 3, 'paris', 'dusseldorf', 'Batman', 'musa']
for elements in my_list2:
    print(elements, end=" ")

squared_numbers = [x ** 2 for x in my_list]
print(my_list)

my_list = [1, 2, 4, 5, 6]
squared_even_numbers = [x ** 2 for x in my_list if x % 2 == 0]
"""
Bu ifade, orijinal listenin elemanları içinde sadece çift olanları seçer ve bu çift sayıların 
karelerinden oluşan yeni bir liste oluşturur.
"""
"""
List Comprehension, karmaşık döngüler veya filtreleme işlemleri için 
okunabilir ve sade bir şekilde kullanılabilir. Ancak, çok karmaşık hale 
geldiğinde anlaşılabilirliği azalabilir, bu nedenle dengeli bir kullanım 
önemlidir.
"""

"""
Bir listenin referansını başka bir değişkene atamak, orijinal listeyi 
değiştirmenize neden olabilir.
"""
new_list = my_list2
print(my_list2)
new_list[0] = 100  # my_list'teki ilk eleman da değişir
print(my_list2)

"""
copy() metodu ile orijinal listeyi değiştirmeyen bir kopya alabilirsiniz.
"""
new_list = my_list2.copy()  # aynı şekilde -> new_list2 = my_list2[:]
print(new_list)

"""
NumPy, Python'da bilimsel hesaplamalar için oldukça yaygın bir kütüphanedir. 
Özellikle çok boyutlu dizilerle çalışmak ve matematiksel işlemler yapmak için 
kullanılır. NumPy dizileri, Python listelerinden daha etkili ve hızlıdır.
NumPy, lineer cebir, istatistiksel analiz ve diğer bilimsel hesaplamalar için bir dizi işlevsellik sunar.

Ancak, bu kütüphanenin yaygın kullanım alanları daha spesifik ve genel 
bir liste işlemleri için gerekliliği düşük olabilir. Yine de, projenizin 
ihtiyaçlarına bağlı olarak NumPy ve benzeri kütüphaneleri 
değerlendirebilirsiniz.
"""
