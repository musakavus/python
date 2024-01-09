"""
Python fonksiyonları, belirli bir görevi gerçekleştiren ifadelerin bir araya
getirilmesiyle oluşturulan bloklardır. Temel fikir, sıkça yapılan görevleri
bir araya getirip bir fonksiyon oluşturarak, aynı kodu farklı girişler için
tekrar tekrar yazmak yerine fonksiyon çağrıları yaparak kodun içindeki kodu
tekrar kullanmaktır.
"""

"""
Kod Okunabilirliğini Artırır
Kodun Yeniden Kullanılabilirliğini Artırır
"""


def function_name():
    print('hi ruinchain')


function_name()

"""
Python'da İki Tür Fonksiyon:

Yerleşik Kütüphane Fonksiyonları: Python'da kullanılabilen standart fonksiyonlardır.
Kullanıcı Tanımlı Fonksiyonlar: İhtiyaca göre kendi fonksiyonlarımızı oluşturabiliriz.
"""


def say_hi():
    print('Hi')


say_hi()


def even_odd_control(a_number):
    if a_number % 2 == 0:
        print('it is odd')

    else:
        print('it is even')


a_number = int(input('Enter a number: '))
even_odd_control(a_number)

"""
Varsayılan Argümanlar: Belirli bir argümana değer verilmezse, varsayılan bir değeri alır.

Anahtar Kelime Argümanları: Argümanların sırasını hatırlamaya gerek 
kalmadan argüman adını belirleyerek kullanma.

Pozisyonel Argümanlar: Argümanların sırasına dikkat edilmesi gereken geleneksel argüman türü.

Belirtilmeyen Argümanlar (Değişken Uzunluklu Argümanlar): *args ve **kwargs 
kullanarak değişken sayıda argümanları işleme alma.
"""


def def_arg(x, y=50):
    print(x + y)


def_arg(49)


def student(name, surname):
    print(name, ' ', surname)


student(name='musa', surname='kavus')
student(surname='kavus', name='musa')


def vole(name, yas):  # Hatalı kullanım
    print('name: ', name, ' ', 'age: ', yas)


vole('Onder', 56)
vole(36, 'ruin')

"""
Dökümantasyon Strings (Docstring):
Fonksiyon tanımının hemen ardından yazılan dökümantasyon stringidir. 
Bu, fonksiyonun işlevini açıklamak için kullanılır ve isteğe bağlıdır.
"""


# TODO: this function should take a return value
def passing_control(name, mark):
    """
    This function calculate status to passing exam
    :param name: this param. using for student's name
    :param mark: this param. using for student's mark
    :return: nothing
    """
    if mark < 40:
        print('name: ', name, 'status: you failed')

    else:
        print('name: ', name, "status: you passed")


passing_control('semih', 41)
print(passing_control.__doc__)

"""
İç İçe Fonksiyonlar ve Lambda Fonksiyonlar:
Python'da bir fonksiyonun içinde tanımlanan fonksiyonlara iç içe fonksiyonlar denir. 
"""


def login(username, password):
    print('Dear ', username)

    def user_control():
        if username == 'admin':
            print('you are an moderator')
        else:
            print('You are normal user')

    user_control()


login('ruinchain', '123123')
login('admin', 123123)

"""
Ayrıca, isimsiz fonksiyonlar olan lambda fonksiyonları da bulunmaktadır.
"""
kare = lambda x: x * x * x
print(kare(7))


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


def func(number1: int, mystring: str) -> str:  # --> amaç okunabilirliği ve esnekliği artırmak
    return str(number1) + ' ' + mystring


result = func(4, 'chain')
print(result)


def func2(param: str) -> list:
    return [1, 2]


result2 = func2('param')
print(result2)


