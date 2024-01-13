# Decorators
"""
Decorators: Meta programlmaya örnek olarak verilebilir. Meta progralmala nedir?-->
Yazılan bir programın başka bir program üretmesi yada belli kod parçasının kodunun değiştirilmesi diyebiliriz

Dekoratör kavramında ise yazdığım fonksiyonların yapıların program içerisinde derleme anında değiştirilmesini öğreneceğiz
Yani yorumlama anında yazdığımız kodlar belli bir yapıyı değiştiriecek. Tabi bu yapılar fonksiyonlar olacak
dolayısıyla decoratorsler fonksiyonlar çeşitli öözellikler kazandırmamızı sağlıyor

Bunun içinde iç içe fonksiyonlar kullanıyoruz. Closuredan farkı ise bir fonksiyon prametre olarak bir fonksiyon alacak.
ve kendi içerisinde bu fonksiyonu değiştirecek. Değiştirdikten sonra tekrar geri döndürecek. Böylelikle yeni özellikler
eklemiş olacağız
"""


def decorator(func):
    print('I am out function')

    def inner_function():
        print('I am inner function')
        func()

    return inner_function


def param_func():
    print('I am param func')


# parametre olarak fonksiyon veriildi
data = decorator(func=param_func)  # --> data = inner_function
data()  # data() = inner_function()


# An Example
def decorator1(func):
    def inner_func():
        print('*' * 9 + '\n' + func() + '\n' + '*' * 9)

    return inner_func


def info():
    name = input('enter a name: ')
    return name


data1 = decorator1(func=info)
data1()


# ileriki derslerde şunu öğreneceğiz. Decoratorleri kullanırken yukarıdaki gibi kullanmak yerine
# o fonksiyonun başına @ işareti koymak yeterlidir
def decorator2(func):
    def inner_func():
        print('*' * 9 + '\n' + func() + '\n' + '*' * 9)

    return inner_func


@decorator2  # bunu yazmamın amacı, python bu işareti görerek bunun dekoratörlerce kullanılmak istendiğini anlıyor.
def info1():
    name = input('enter a name: ')
    return name


info1()  # bunu yazmak yeterli oldu. Çünkü info1'i çalıştırınca info1 bunu @ işaretiyle tanımlanan decoratöre-->
# o fonksiyonu paramtre olarak atıyor
