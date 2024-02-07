"""
Name mangling (isim değiştirme)
"""
"""
Python programcılarının da sık sık söylediği gibi: ‘Neticede hepimiz, doğruyu yanlışı bilen, yetişkin insanlarız.’
Bir önceki derslerimizde private ile değişken ve metodları gizleyebileceğimizi öğrenmeiştik.
Ve fakat pythonda böyle bir şey mümkün değildir.

Bu name mangling işleminin yapılması pek etik değildir
"""


class Users(object):
    def __init__(self, username):  # şu an bu değişkenle
        self.__username = username

    def __info(self):  # bu methoda dışarıdan ulaşmak mümkün değil--> fakat
        print(f'Kullanıcı adı: {self.__username}')


u1 = Users('admin')
# u1.__username # hata --> 'Users' object has no attribute '__username'
# u1.__info()  # hata --> 'Users' object has no attribute '__info'
print(u1._Users__username)  # --> bu şekilde ulaşılabiliyor
u1._Users__info()  # aynı şekilde
print('*' * 45)
u1._Users__username = 'ruin'
print(f'New username: {u1._Users__username}')  # aynı şekilde değişiklik işkemi de yapılabilir
u1._Users__info()
"""
Fakat python bunu yapmamıza her ne kadar müsade etse de bunu yapmamamız lazım.
1-> Encapsulation yapısına terstir.
2--> Eğer bir geliştirici bir değişkeni private yapmışsa buna saygı duymamız lazım ve müdahale etmememiz lazım

"""
