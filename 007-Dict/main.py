"""
 Python'da çok güçlü ve yaygın olarak kullanılan bir veri yapısıdır.
 Sözlükler, anahtar-değer (key-value) çiftleri içerir ve bu çiftlerle
 veri depolamak ve yönetmek için kullanılır
"""

# süslü parantez içinde tanımlanır ve anahtar-değer çiftleri arasında virgül kullanılır:
my_cars = {'wolswagen': 'passat', 'mercedes': 'benz', 'renault': 'megan'}
print(my_cars)

# Sözlükteki bir value'ye key kullanarak ulaşılabilir
value_of_a_car = my_cars['wolswagen']
print(value_of_a_car)

my_cars['seat'] = 'leon'
print(my_cars)

# Access a Value in Dictionary using get() in Python

print(my_cars.get('wolswagen'))

"""
keys() metodu ile anahtarları, values() metodu ile değerleri ve 
items() metodu ile anahtar-değer çiftlerini alabilirsiniz:
"""
my_keys = my_cars.keys()
print(my_keys)
my_values = my_cars.values()
print(my_values)
my_items = my_cars.items()
print(my_items)

is_key_present = 'seat' in my_cars
print(is_key_present)

for item in my_cars:
    print(item, my_cars[item])

# Boş bir dict oluşturma

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# Nested Dictionaries

nested_dict = {1: 'ruin', 2: 'chain', 3: {'Ruin': 'Chain'}}
print(nested_dict)

"""
ALL FUNCTION
dic.clear()->Dictteki tüm key value değerlerini siler
dic.copy()->Bir kopyasını döndürür
dic.get(key, default='none') --> print(nested_dict.get(1)) --> Eğer değer yoksa none dönrürür
dict.keys -->  Returns a list containing dictionary’s keys
dict.update(dict2) Updatelenen dictten kendisinde olmayan elemanları da ekler
dict.values() -->  Returns a list of all the values of dictionary
dict.pop()--> Remove the element with specified key
popItem() --> Removes the last inserted key-value pair
dict.get(key, default = “None”) --> used to get the value specified for the passed key.
"""

existing_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2'}
new_data = {'anahtar2': 'yeni_değer2', 'anahtar3': 'değer3'}
existing_dict.update(new_data)
print(existing_dict)

nested_dict.pop(1)
print(nested_dict)

nested_dict.popitem()
print(nested_dict)

my_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2'}

# 'anahtar1' anahtarı zaten mevcut olduğu için mevcut değeri döndürür
value_of_key1 = my_dict.setdefault('anahtar1', 'yeni_değer1')
print(value_of_key1)  # 'değer1'

# 'anahtar3' anahtarı sözlükte bulunmadığı için varsayılan değeri ekler
value_of_key3 = my_dict.setdefault('anahtar3', 'yeni_değer3')
print(value_of_key3)  # 'yeni_değer3'

print(my_dict)
