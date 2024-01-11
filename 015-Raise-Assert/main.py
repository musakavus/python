# try:
#     my_number = int('hi')
#     print(my_number)
# except ValueError:
#     print('We find an error')

# raise yi daha iyi anlamak için, dilediğimiz bir kod bloğunda raise deyimi sayesinde biz hata aldırabiliyoruz
# tabi bunun sırası önemlidir

# try:
#     raise ValueError()  # örneğin diyorum ki sen burada sadece value error titpinde bir hata yap
# dikkat ettiysen print kısmı unreachable oldu. Yani raisle aynı blokta olup kendisinin altındaki kodlar çalışmaz
#     my_number = int('hi')
# except ValueError:
#     print('an error occured')

# dikkatini çektiyse excepte yazdığımız error tipi parantezsiz ama raisedeki parantezli
# demek ki biz raise'nin yanındaki paranteze parametre yada mesaj verebilirimz. Örnek aşağıdaki gibi
print('------------------------------------------')
print('BİRİNCİ KULLANIM ')
# istediğimiz kod bloğunda pythonun hazır hata kütüphanelerini kullanarak istediğimiz tarzda hata yaratabiliriz
# try:
#     raise ValueError('Hata')
#
#
# except ValueError:
#     print('an error occured')
# output: an error occured -->Z Dikkat ettiysen output olarak yine exceptteki outputu gösterdi sadece
# bu durumu değiştirmek istiyorsak as ifadersini kullanabiliriz
# artık dilediğimiz mesajı verip pythonun hata kütüphanesini istediğimiz gibi manipüle edebiliyoruz
print('---------------------------------------------')

# try:
#     raise ValueError('Hata')
# except ValueError as err:
#     print('an error occured')
#     print(err)

"""
Output: 
an error occured
Hata

Burda fake ettiysen raisedeki string parametresini excepte okutabildim as deyimi sayesinde.
Dolayısıyla ekstra print yazmamma gerek kalmadı
"""

# while True:
#     try:
#         raise ValueError('Error occured. Try again later...')
#
#     except ValueError as err:
#         print(err)
#         break


# try:
#     raise NameError('Name Error occured')
#
# except ValueError as err:
#     print(err)

# burdaki kodu çıktısında dikkat ettiysen sadece Name error occured hatası alıyorsun.
# Bu name error hatasını Except kısmında göremediğimiz için (Sadece Valueerror tanımlı olduğu için) hatayı except ile
# yakalayamadık. Yani program çöker. Ve dikkat ettiysen bizim verdiğimiz parametre yazıldı.
# Dolayısıyla biz neyi öğreniyoruz. İstediğimiz hatayı istediğimiz kod bloğunda verdirebiliyoruz.
# Raisede verdiğimiz hataların, except bloğunda yakalanması gerekiyor
# Birinci kullanımda bilmen gereken en önemli şeylerden bir tanesi de verdiğin hatanın python
# kütüphanesinde tanımlı olması zorunluluğu

print('---------------------------------------------------------')
print('2. KULLANIM')

"""
ikinci kullanım şekli ise biz raise terimini istediğimiz yerde istediğimiz yapıda istediğim 
şekilde, bizim kurallarımıza göre (python kütüphanesine göre değil) yapabiliyoruz
"""

my_number = 5
if my_number == 5:
    raise Exception(
        'Number cannot can not be 5')
else:
    print(my_number)
"""
eğer benim istediğim hata türü python'ın hatalar kütüphanesinde yoksa kendi hata classımızı oluştururuz.
normalde burada bizim kendi yarattığımız hatanın class'ını belirtmemiz gerekiyor ve fakat henüz oop'ye geçmediğimiz için
bunu yapmayacağız. bunu yapmak yerine şimdilik tüm hataları içerisine alan pythonun exception classını kullanacağız
"""

# output: ine 80, in <module> raise Exception(Exception: Number cannot can not be 5
# dikkat ettiysen python kütüphanelerinin gösterdiği hata tarzında bir hata aldık

my_number = 5
# if my_number == 5:
#     print(
#         'number can not be 5')  # böyle de yapabilirdim. Ama sanki bu bir istisnaymış gibi, python tarzında hata verdim
#     # ve eğer geliiştirici bu hatayı çözmezse programın çökmesini istiyorum
# else:
#     print(my_number)

# şimdi de hata giderme yaklaşımı yapalım. Dolayısıyla yine try except kullanacağız

try:
    if my_number == 5:
        raise Exception('Number can npt be 5')

except Exception as err:  # raise de verdiğim hata classını veriyorum hata classı olarak
    # kodlar --> ve artık hatayı yönetmiş olmayı da öğreniyoruz
    print(err)

# eğer raisede belirttiğin hata except bloklarında yoksa program tamamen çöker
"""
# bu arada raise deyimine parametre vermek zorunlu değildir.as deyimini kullanıp assertteki mesajı 
vermek istiyorsan kullanabilirsin
"""
