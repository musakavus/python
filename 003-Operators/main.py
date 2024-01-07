import operator
from operator import lt, le, eq, gt, ge, ne

# Operators
a = 5
b = 7
c = 6
summary = a + b
substraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
power = a ** b

if a > b:
    print(a, 'bigger than', b)

else:
    print(a, 'smaller than', b)

if a == b:
    print('a equal b')

else:
    print('a not equal b')

if a != b:
    print('a not equal b')
else:
    print('a equal b')

if a >= b:
    print('a bigger than b')
else:
    print('b bigger than a')

if a <= b:
    print('a smaller than b')
else:
    print('b smaller than a')

if a < b and b > c:
    print('a smaller than b and b bigger than c')

if a < b & b > c:
    print('a smaller than b and b bigger than c')

if a < b | b > c:
    print('a smaller than b and b bigger than c')

y = 5
z = 7
x = y + z

# it is same
x = x + y
x += y

# it is same
x = x - y
x -= y

# is it same
x = x / y
x /= y

# it is same
x = x * y
x *= y

print(1 + 2)
print('Ruin' + 'Chain')
print(3 * 4)
print('Ruin' * 4)

"""
Herhangi bir true değeri var mı? Varsa True döndürür. Liste demet set'lerde de geçerli
"""
numbers = ['Batman', 'Superman', True, '1', '1.9']
result = any(numbers)
print(result)

print(any([False, False, False, False]))
print(any([True, False, False, False]))

list1 = []
list2 = []

for i in range(1, 11):
    list1.append(4 * i)

for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print(any(list2))

"""
all() fonksiyonu, bir iterable içindeki tüm değerlerin True olup olmadığını kontrol eder.
Eğer iterable içindeki tüm değerler True ise, all() fonksiyonu True döner; aksi takdirde, False döner.
"""

list3 = [True, True, True, True]

result2 = all(list3)
print(result2)

list4 = [True, False, True, True]

result3 = all(list4)
print(result3)

c = 5
print(c == 5)

a = 4
b = 3

print(operator.add(a, b))
print(operator.sub(a, b))
print(operator.mul(a, b))
print(operator.floordiv(a, b))
print(operator.truediv(a, b))
print(operator.pow(a, b))
print(operator.mod(a, b))

"""
lt fonksiyonu, bir değerin başka bir değerden küçük olup olmadığını kontrol eder.
le fonksiyonu, bir değerin başka bir değere eşit veya küçük olup olmadığını kontrol eder.
eq fonksiyonu, bir değerin başka bir değere tam olarak eşit olup olmadığını kontrol eder.
gt fonksiyonu, bir değerin başka bir değerden büyük olup olmadığını kontrol eder.
ge fonksiyonu, bir değerin başka bir değere eşit veya büyük olup olmadığını kontrol eder.


'ne()' fonksiyonu, bir değerin başka bir değere eşit olup olmadığını kontrol etmez; tam tersine, 
eşit olup olmadığını kontrol etmek yerine eşit olup olmadığını kontrol eder. Eşitlik olmamasını 
doğruluyor kısaca
"""

result = lt(5, 10)  # 5, 10'dan küçük mü?
print(result)
result = le(5, 10)
print(result)
result = eq(5, 10)
print(result)
result = gt(7, 9)
print(result)
result = ge(7, 9)
print(result)
a, b = 7, 9
result = ne(a, b)
print(result)

# in, not in
my_list3 = [5, 10, 15, 25, 35, 60]
a_number = 8
second_number = 10

if a_number in my_list3:
    print('number in list')
else:
    print('number not in list ')

if second_number not in my_list3:
    print('Second number not in list')
else:
    print('Second number in list')

"""
setitem fonksiyonu, bir nesnenin belirli bir pozisyondaki elemanını belirtilen değerle değiştirmek için kullanılır.
return yapmaz
"""
my_list4 = [3, 6, 9]
my_list5 = [2, 4, 6]
my_list6 = [5, 10, 15]

operator.setitem(my_list4, 0, 0)
print(my_list4)

"""
getitem fonksiyonu, bir nesnenin belirli bir pozisyondaki elemanını getirmek için kullanılır.
return yapabilir
"""
k = operator.getitem(my_list5, 0)
print(k)

"""
delitem fonksiyonu, bir nesnenin belirli bir pozisyondaki elemanını silmek için kullanılır.
"""

operator.delitem(my_list6, 2)
print(my_list6)

"""
Python'daki slice() fonksiyonu, dilimleme (slicing) işlemlerini gerçekleştirmek için kullanılır. 
slice() fonksiyonu, bir dilim (slice) nesnesi oluşturarak, bir iterable'ın belirli bir alt dizisini 
seçmeye ve işlemeye olanak tanır.

slice(start, stop, step) şeklinde kullanılır, burada:
start: Dilimin başlangıç indeksi. İlk elemanın indeksi 0'dan başlar.
stop: Dilimin bitiş indeksi. Bu indeks hariç alınacaktır.
step: Dilimleme adımları arasındaki mesafe. Varsayılan değeri 1'dir.

slice(start, stop) şeklinde kullanılır, burada:
start: Dilimin başlangıç indeksi. İlk elemanın indeksi 0'dan başlar.
stop: Dilimin bitiş indeksi. Bu indeks hariç alınacaktır.

"""

word = "PYTHONPROGRAMMING"
my_slice = slice(2, 15, 3)
# 2. indexten başla 14 adım ekle, 3er 3 er ilerle
# t h o n p r o g r a m m i n
# t n o a i
result = word[my_slice]
print(result)

my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
my_slice = slice(1, 8, 2)
# 1. indexten başla. 7 eleman ekle. 2 şer ilerle
# 10 15 20 25 30 35 40
# 10 20 30 40
result = my_list[my_slice]
print(result)

li = [1, 5, 6, 7, 8]

# Orjinal listeyi yazdırma
print("Orijinal liste: ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

# 15678

print("\r")

# slice() fonksiyonunu kullanarak 1. indeksten başlayarak 4. indekse kadar olan elemanları [2, 3, 4] ile değiştirme
operator.setitem(li, slice(1, 4), [2, 3, 4])

# Değiştirilmiş listeyi yazdırma
print("Değiştirilmiş liste: ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")
