# set'ler, benzersiz elemanların bir araya getirildiği bir veri yapısıdır.

# Set'ler süslü parantezler içerisinde tanımlanır

# aynı elemandan birden fazla ekleyemezsin eklersen hata vermez ama set'e 1 adet eklenmiş olur

my_set = {1, 1, 5}
print(my_set)

my_set = {1, 2, 3, 'a', 'b', 'c'}
my_set.add(4)
print(my_set)  # eleman random indise eklenir

my_set.remove('b')
print(my_set)

"""
Birleşim (Union): union() veya |
Kesişim (Intersection): intersection() veya &
Fark (Difference): difference() veya -
Simetrik Fark (Symmetric Difference): symmetric_difference() veya ^
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)  # print(set1 | set2)
print(union_set)
intersection_set = set1.intersection(set2)  # print(set1 & set2)
print(intersection_set)
difference_set = set1.difference(set2)  # print(set1-set2)
print(difference_set)
symetric_difference_set = set1.symmetric_difference(set2)  # a birleşim b eksi a kesişim b
print(symetric_difference_set)  # print(set1^set2)

# Set içindeki elemanları döngü ile gezmek için for döngüsü kullanılabilir:
k = is_present = 3 in my_set  # true
print(k)

"""
Set'ler, benzersiz elemanları sırasız bir şekilde saklar
 ve bu özellikleri sayesinde çeşitli uygulamalarda faydalı olabilir
"""
