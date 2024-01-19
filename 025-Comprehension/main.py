# comprehension
"""
Comprehension kavramı aslında pythonu daha çok popüler yapan ve güçlü özelliklerden bir tanesidir
Python programlama dili konuşma diline oldukça yakın bir dil olduğu için oldukça popülerdir.
comprehension kavra mı tek satırda yazabileceğimiz güçlü kodları ifade ediyor
"""

result_list = []

for number in range(1, 11):
    result_list.append(number * number)
print(result_list)

print('-' * 45)
result_list2 = [value * value for value in range(1, 11)]  # -> sol taraf işlem, sağ taraf döngü.
# [] içerisine almamızın sebebi bunun türünün liste olması
print(type(result_list))  # output -> <class 'list'>
print(result_list2)

print('-' * 45)
result_set = {value * value for value in range(1, 11)}
print(type(result_set))  # output -> <class 'set'>
print(result_set)

print('-' * 45)
result_set = {value: value * value for value in range(1, 11)}
print(type(result_set))  # output -> <class 'dict'>
print(result_set)

print('-' * 45)
result_tuple = (value * value for value in range(1, 11))
print(type(result_tuple))  # output-> <class 'generator'>
for value1 in result_tuple:
    print(value1, end='')

print('-' * 45)
example = 'Ruinchain'
sentence = [str.split(value) for value in example]
print(type(sentence))  # list
print(sentence)  # [['R'], ['u'], ['i'], ['n'], ['c'], ['h'], ['a'], ['i'], ['n']]

kelime = 'where there is ruin there is a treasure'

carkifelek = [value for value in kelime if value in 'bcdyzgi']
print(carkifelek)  # burda output :  ['i', 'i', 'i']

carkifelek = {value for value in kelime if value in 'bcdyzgi'}
print(carkifelek)  # {'i'} (çünkü set içerisine aynı elemandan 1 tane alır sadece)
