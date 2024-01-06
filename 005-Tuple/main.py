"""
Tuple'lar, Python'da kullanılan bir veri yapısıdır ve listelere benzer,
ancak önemli bir farkı vardır: tuple'lar değiştirilemez (immutable)dir.
Yani, bir kere oluşturulduktan sonra elemanları üzerinde değişiklik yapılamaz.
"""

# Tuple'lar parantez içinde tanımlanır:
my_tuple = (1, 3, 5, 'a', 'c', 'e')

# elemeanlara index kullanılarak erişilebilir
first_element = my_tuple[0]
second_element = my_tuple[1]
print(first_element)
print(second_element)

# Tuple'lar oluşturulduktan sonra üzerlerinde değişiklik yapılamaz:
# my_tuple[0] = 10
# print(my_tuple)

for item in my_tuple:
    print(item, end=' ')

# Tuple'ları + operatörü ile birleştirebiliriz:
print()
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c', 'a')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

# Tuple'lar özel metodlara sahiptir. Örneğin, count() metodu ile bir elemanın kaç kez geçtiğini öğrenebiliriz:

count_a = concatenated_tuple.count('a')
print('Total count of the a: ', count_a)
