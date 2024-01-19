# Lambda Fonksiyonları
"""
Pythonda isim vermeden isimsiz dediğimiz fonksiyonlar oluşturmamız mümkün
Bunlara lambda fonksiyonlar denmekte.
Ve bunlar çok HIZLI çalışmaktadır.
Ve birden fazla parametre alabilse de sadece içerisinde bir tane ifade döndürebilir.
"""


# 1. avantajı --> kdo kalabalığını önler. Daha kısa. Dolayısıyla performansı artırır
# 2. avantajı --> Lambda fonksiyonunu başka bir fonksiyonun içerisinde kullanınca daha fazla verim elde ediyoruz
def func(x):
    return x + 1


(lambda x: x + 1)(x=10)  # --> soldaki x değeri parametre --> iki noktandan sonraki yapı fonksiyonun RETURN değeri
# sağdaki parantez--> fonksiyonu çalıştırma ve parametre verme yeri
# bu fonksiyonun bir return değeri olduğu için onu bir değere atayıp print alabiliriz
datax = (lambda x: x + 1)(x=10)
print(datax)

# yine aynı şekilde
datax = lambda x: x + 1
print(datax(12))  # tabi bu metodu kullandığında parametreyi fonksiyon içinde vermen lazım


# closureda öğrendiğin mantığı uyguladık.
# dolayısıyla lambdayı iki şekildede kullanabiliriz
# aslında bilgisayar bilimlerinde lambda çok popüler ve büyük bir kural
# Lambda calculus diye hesaplama teoremleri var. Profesyonel dillerin vazgeçilmezidir


def func2(name, surname):
    return f'name: {name} Surname: {surname}'


info = (lambda name, surname: f'name: {name} Surname: {surname}')('Ruin', 'Chain')
print(info)


def func3(x):
    return x ** 2


result = (lambda x: x ** 2)(x=5)
print(result)


# en faydalı kullanım yöntemi de şudur aslında. İç içe fonksiyon kullanmak yerine fonksiyon içinde lambda kullanmak
# gayet verimlidir. Lambda fonskiyonları belirli fonksiyonların içinde return değeri olarak verilebilir


def info(version):
    print('Outer function')
    return (lambda param: param)(f'lambda inner function and python version is: {version}')
    # unutma burda fonksiyonun ismini değil fonksiyonun parantezli halini döndürüyorsun
    # --> (lambda param: param)('lambda inner function') kısmı fonksiyon olduğu için bir lambda fonksiyonu return ettim


data = info('3.9')
print(data)


def info1():
    print('Outer function')
    return lambda param: 'lambda inner function and python version is: ' + param
    # --> (lambda param: param)('lambda inner function') kısmı fonksiyon olduğu için bir lambda fonksiyonu return ettim
    # --> Unutma burda fonksiyonun parantezli halini değil ismini gönderiyorsun


print('---------')
data = info1()
print(data('3.9'))
