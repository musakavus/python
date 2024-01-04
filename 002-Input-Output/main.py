"""
Python'da kullanıcıdan giriş almak için input() fonksiyonu kullanılır.
input() fonksiyonu her zaman bir string döndürür, bu nedenle sayı gibi farklı türlerle çalışırken dikkatli olmalısınız.
"""

user_string = input("Enter a string: ")
print('Your string: ', user_string)

user_number = int(input('Enter a number: '))
print('Your number: ', user_number)

user_float = float(input('enter a float: '))
print('Your float: ', user_float)

user_boolean = bool(input('Your status: '))
print('Your status: ', user_boolean)

#   multiple input

multiple_input = input('Take a space beetwen two input pls: ')
number1, number2 = multiple_input.split()

number1 = int(number1)
number2 = int(number2)
print(type(number1), type(number2))
print('first number: ', number1, 'second number: ', number2)

# \n is the break line

print('i am a software \n engineer')

"""
print() fonksiyonu, bir çıktı satırını bitirdikten sonra varsayılan olarak bir alt satıra geçer(\n). 
"""

print('Gsap is the best live CSS', end=' ')
print('plugin')

# Örnek 1: Satır sonunda boşluk bırakma
print("Bu satırın sonunda boşluk bırakma.", end=" ")

# Aynı satırda devam eden bir yazı
print("Bu, önceki satırın devamıdır.")

print("Bu satırın sonunda özel bir karakter olsun.", end="***")

# Aynı satırda devam eden bir yazı
print("Bu, önceki satırın devamıdır.")

"""
In Python 3.x, the print() function behaves slightly differently from Python 2.x. 
To print without a newline in Python 3. 
x, you can use the end parameter of the print() function.
"""

my_text = 'ruin'
my_second_text = "chain"
my_list = [1, 2, 3, 4]

print(my_text, end=' ')
print(my_second_text)

for i in range(4):
    print(my_list[i], end=' ')

"""
In Python 3. x, you can print without a newline without using
 a for loop by using the sep parameter of the print() function.
The sep parameter specifies the separator to be used between multiple items when they are printed.
"""
my_list2 = [2, 4, 6, 8, 12]
print(*my_list2)

"""
Python | sep parameter in print()
"""
print('R', 'U', 'I', 'N', sep="")
print('R', 'U', 'I', 'N', sep=" ")
print('R', 'U', 'I', 'N', sep="@")

"""
%s: String (or any object with a string representation)
%d: Decimal (integer)
%f: Floating-point decimal
%r: String representation of any object
"""

price = 15.99
stok = 'True'
print('product price: %f ' % price, 'Stok status: %s ' % stok)

browser1 = 'Firefox'
browser2 = 'Chrome'
browser3 = 'Edge'

print(' I love {0} and hate {1} and {2} have no opinion about this'.format(browser1, browser2, browser3))

cstr = "I love geeksforgeeks"

# Printing the center aligned string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))

"""
Genellikle, TODO belirteci ile işaretlenmiş alanlar, kodun geliştirilme sürecinde dikkat çekmek veya bir sonraki 
adımın ne olması gerektiğini belirtmek amacıyla kullanılır. 
Geliştiriciler, bu belirteçleri gördüklerinde, 
o kısımda bir iş yapılması gerektiğini anlarlar.
"""


# TODO: bu fonksiyonu optimize et
def my_function2():
    # there some problem heree
    # maybe added some parameters
    pass


# TODO: Kullanıcı girişi doğrulaması eklenmeli
user_input = input("Lütfen bir değer girin: ")

# TODO: Bu modülü daha sonra incele
import random
