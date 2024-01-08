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


