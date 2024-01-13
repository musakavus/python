def out_func():
    print('Outer function')

    def in_func():
        print('Inner function')

    in_func()
    return 'str'


out_func()

data = out_func  # böyle bir ifade mümkündür. data artık bir fonksiyon tipindedir. ve out_func'un yerini almıştır
data()  # dolayısıyla ben artık data'yı out_func'un yerine kullanabilirim
print(type(out_func()))  # type--> func
print(type(out_func))  # type--> str

x = out_func  # dediğimiz zaman türüne göre eşitleme yapmış oluyoruz
x = out_func()  # dediğimiz zaman ise return değerine göreeşitleme yapıyoruz

# closure
"""
closure kavramı sayesinde fonksiyonlara esneklik katmış oluyoruz.
Bir fonksiyonun closure şeklinde olması için 
1-içe içe olması gerekiyor
2-iç fonksiyonunu return etmesi gerekiyor 
"""
print('-----------------')


# !!! data bir fonksiyonsa data() terimi artık bir fonksiyon değil o fonskiyonu "çalıştırmaktır"
def outer_func():
    print('Dış fonksiyon')

    def inside_func():
        print('iç fonksiyon')

    return inside_func  # burda parantez yok. Fonksiyonun çalışan halini değil, kendisini return etmiş oluyorsun


# !!! atama işlemi yaparken kilit nokta tür eşitliği olmalı
data = outer_func()  # Outer fonksiyonu çalıştı, return olarak inside_func fonksiyonunu döndürdük ama çalıştırmadık.
# Dolayısıyla içindeki kodlar çalışmadı mantıken
# output--> Dış fonksiyon

data()  # data() = func2() oluyor mantıken
# output: iç fonksiyon oluyor mentıken

print('------------------')


def func1():
    print('i am out function')

    def func2():
        print('i am inner function')

    return func2


data = func1()  # dolayısıyla data değişkeni artık bir fonkjsiyon.
# burda sonuç mantıken data = func2 oluyor--> return değerinden dolayı --> dolayısıyla data() = func2() oluyor

data()  # --> data artık fonksiyon olduğu için data() yaparak onu çağırabilirim

print('-----------------------')


def out(param_a):
    print(param_a)

    def inn(param_b):
        print(param_b)

    return inn


closure = out(param_a='Merhaba')
closure(param_b='Python')  # zaten python derleyicisi kod tamamlamada param_b diye öneride bulundu
