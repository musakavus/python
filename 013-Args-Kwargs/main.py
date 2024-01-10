"""
*args (Anahtar Kelime Olmayan Argümanlar)
**kwargs (Anahtar Kelimeli Argümanlar)
Not: "Bir fonksiyona kaç argüman iletmemiz gerektiğinden şüpheliysek,
*args veya **kwargs olarak işlevimizin argümanını kullanırız."
"""


def mult(*args):
    # [2,4,6,8] gibi düşün boyut 4
    temp = 1  # temp --> 2 --> 8 --> 48 -->
    for arg in args:
        temp = temp * arg  # 2 * 1= 2 --> 2*4 = 8 -->  6 * 8 = 48 --> 48 * 8 = 384
    return temp


print(mult(2, 4, 6, 8))  # 384


def my_string(*args):
    sentence = ''
    for word in args:
        sentence = sentence + word + ' '

    return sentence


print(my_string('the', 'big', 'bang', 'theory'))

episodes_points = []
episodes_name = []


def episode_list(**kwargs):
    for key, value in kwargs.items():
        episodes_points.append(key)
        episodes_name.append(value)


episode_list(game_of_thrones=9.3, lord_of_the_ring=9.6)
print(episodes_points)
print(episodes_name)


def my_func(sayi1, sayi2):
    """
    return fonksiyonlardan çıkmaya yarar. Fonksiyon returnü gördü mü  fonksiyondan çıkar
    ve yanındaki değeri döndürür
    """
    return sayi1 + sayi2  #


total = my_func(5, 7)
print(total)


def basic_sum(*args):
    return sum(args)


total = basic_sum(4, 98, 121, 1)
print(total)


def an_example(*args):
    return args


return_value = an_example('it', 'is', 'an', 'example')
print(return_value)
print(type(return_value))  # output: <class 'tuple'>


# dikkat edilmesi gereken şey şu--> fonksiyon eleman gönderince tuple şeklinde gönderir.
# dolayısıyla işleme sokacağımız elemanları bir tuple gibi düşünebiliriz. Zaten o yüzden sum() fıonksiyonu işe yaradı


# Bir fonksiyon içerisine parametre olarak hem arg hemde kwarg verilebilir. Ama sıralama çok önemlidir

def info(classroom, *args, **kwargs):
    print(f'classroom: {classroom}')
    print(f'Marks: {args}')
    print(f'Infos: {kwargs}')


info('12 / C', 25, 30, 45, 78, 95, name='ruin', surname='chain')

a_value = 'Django'
print(a_value)
