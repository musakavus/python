"""
for var in iterable:
    # statements
"""

my_list = [1, 2, 3, 4, 5]

for num in my_list:
    print(num)

# range() fonksiyonunu kullanarak belirli bir aralıkta dolaşmak da yaygın bir kullanımdır:

for number in range(10):
    print(number, end=' ')

my_list2 = (1, 'istanbul', '3', True, 5, 9)

for element in range(len(my_list2)):
    print('element: ', my_list2[element])

my_dict = {1: 'istanbul', 2: 'Galatasaray', 3: 'Musa'}
for dict_element in my_dict:
    print(my_dict[dict_element])

for number2 in range(0, 10, 2):  # başlangıç indisi, bitiş indisi, adım sayısı
    print(number2)
a_string = "musakavus"
for word in range(0, len(a_string), 2):
    print(a_string[word], end=' ')

# Python For Loop with Zip()
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'green']

print()
for fruit, color in zip(fruits, colors):
    print(fruit, ' ', color)

tuple_of_tuples = ((1, 2), (3, 4), (5, 6))

for a, b in tuple_of_tuples:
    print(a, b)  # Bir nevi iç içe tupledaki iç tupleyi unpacking ediyorsun.

"""
continue ifadesi, döngü içinde bulunduğu anda kontrolü döngünün başına geri gönderir.
Yani, continue ifadesi çalıştığında, 
döngü içindeki sonraki adımlar atlanır ve döngü başa döner.
"""

for a_number in range(8):
    if a_number == 5:
        continue
    print(a_number, end=' ')

print('\n')
for num in range(8):
    if num == 5:
        break

    print(num, end=' ')

print('\n')

"""
pass ifadesi, hiçbir şey yapmaz. Sadece geçişi temsil eder. 
Bu ifade, bir bloğun (örneğin, bir fonksiyon, döngü veya koşul ifadesi içinde) söz 
dizimine uygun olması için yer tutucu olarak kullanılır.
Kullanıldığı yerde hiçbir işlem gerçekleşmez, programın akışı sadece geçiş yapar.
"""

# TODO: Bu kısım düzenlenecek
second_string = 'Galatasaray'
for letter in second_string:
    pass

