"""
Static Metohd
self yada cls paramtrelerini almazlar. Yada o işlevi görecek parametreleri. Ama nırmal parametre alabilirler
"""


class Math:
    total_count = 0

    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2
        self.total()

    def addiction(self):
        return 'Result: ' + str(self.__number1 + self.__number2)

    @classmethod
    def total(cls):
        cls.total_count = cls.total_count + 1

    @staticmethod
    def find_max(a, b):
        return 'Max number is: ' + str(max(a, b))

    @staticmethod  # static method olduğunu belirtmek için @staticmethod decoratörünü kullanırız
    def pi():
        return 3.14

    def __repr__(self):
        return f'Welcome to calculator...'


m1 = Math(3, 4)
m2 = Math(3, 4)
m3 = Math(3, 4)
result = m1.addiction()
print(m1.__repr__())
print(result)
print('Pi sayısı: ', Math.pi())

print(Math.find_max(9, 10))
print('Toplam işlem sayısı: ', Math.total_count)

# Kodunda bağımsız bir fonskiyon yada method return ifadesini gördü mü hemen o fonskiyondan çıkar. İç içe olması önemsiz
# statik metodlara hem nesne üzerinden ulaşabiliyoruz. hem de class üzerinden
# aynı şekilde classmetodlara da öyle
print(m2.find_max(9, 90))

# static metodların en büyük avantajı nesne üzerinden ulaşabilme zorunluluğunu ortadan kaldırmaları
# ve fakat self içeren metodlara, instance üzerinden ulaşabilirim sadece
"""
en önemli şeylerden biri class attributesi kullanırken, self metodlarında veya attributelerinde bu class değişkenini
kullanmamaya dikkat et. Hata almazsın ama hatalı sonuç alabilirsin
"""
