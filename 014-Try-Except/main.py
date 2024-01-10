# """
# Error Types:
# Syntax
# Logic
# Exception

# hata konusunda olabildiğince açıklayıcı ol. Mümkünse her hatayı açıkla ki kullanıcı bilgilensin
# """
#
# # except olmadan try çalışmaz.Her try'ın muhakkak bir exceptionu olmalı
#
# # Shift + * --> todo list
#
# try:
#     number = int(input('please enter an integer number: '))
#     print('Your entered number: ', number)
#
# except ValueError:
#     print('You can entered just integer. Pls try again')
#
# while True:
#     try:
#         mark = int(input('please enter your mark: '))
#         average = int(input('Total count: '))
#         division = mark / average
#         print('your entered number: ', division)
#         break
#     except ValueError:
#         print('pls enter an number...')
#     except ZeroDivisionError:
#         print('Total count can not be Zero. Try again...')
#
# # TODO: Else
#
# while True:
#     try:
#         mark = int(input('please enter your mark: '))
#         average = int(input('Total count: '))
#         division = mark / average
#         print('your entered number: ', division)
#     except ValueError:
#         print('pls enter an number...')
#     except ZeroDivisionError:
#         print('Total count can not be Zero. Try again...')
#     else:
#         print('Succeed')  # hiç bir hata bulunamadığı takdirde, ve try sorunsuz çalışırsa else çalışır
#         # yani anlayacağın else hata olmadığı durumlarda çalışır
#         break
#
# print('block-out')

# Hataları birleştirme
# while True:
#     try:
#         mark = int(input('please enter your mark: '))
#         average = int(input('Total count: '))
#         division = mark / average
#         print('your entered number: ', division)
#     except (ValueError, ZeroDivisionError):  # hata birleştirme kısmı
#         print('pls enter an number and except number zero...')
#     else:
#         print('Succeed')  # hiç bir hata bulunamadığı takdirde, ve try sorunsuz çalışırsa else çalışır
#         # yani anlayacağın else hata olmadığı durumlarda çalışır
#         break
# # TODO: Raise


# TODO: Else


# bu şekil yazarsan hata alırsın. Çünkü try da bir hata olmadığı için bölüm işleminde 0 bölünme hatası oluyor
# ve bundan dolayı program patlıyor. O yüzden yapılması gereken else içinde tekrar try except
# while True:
#     try:
#         mark = int(input('please enter your mark: '))
#         average = int(input('Total count: '))
#
#     except ValueError:
#         print('pls enter an number...')
#     except ZeroDivisionError:
#         print('Total count can not be Zero. Try again...')
#     else:
#         division = mark / average
#         print('your entered number: ', division)
#         print('Succeed')  # hiç bir hata bulunamadığı takdirde, ve try sorunsuz çalışırsa else çalışır
#         # yani anlayacağın else hata olmadığı durumlarda çalışır
#         break


# En doğru kullanım buu
# while True:
#     try:
#         mark = int(input('please enter your mark: '))
#         average = int(input('Total count: '))
#     except ValueError:
#         print('pls enter an integer number')
#     else:
#         try:
#             division = mark / average
#             print('average number: ', division)
#             break
#         except ZeroDivisionError:
#             print('this function can not be dividing by 0...')

# AS deyimi

# total_err = 0
# while True:
#     try:
#         product = (input('Enter product name: '))
#         price = float(input('Enter a price: '))
#
#     except ValueError as err:
#         total_err = total_err + 1
#         print('Hata: ', err)
#         # bu err değişkeninin çıktısı tuple şeklinde de alabilirsin. mesaj.args ile. Fonksiyon değil
#     except ZeroDivisionError as err:  # hepsini err ile tanımlayabilirsin. Çünkü err burda local değişkendir
#         print(err)
#     else:
#         print('Product Saved')
#         break
#
# print('Total count: ', total_err)

# finally hata olsa da olmasa da çalışır

# try, finally olduğu sürece except olmadan da çalışır
# while True:
#     try:
#         point = int(input('Enter a number: '))
#         print(point * 5)
#
#     finally:
#         print('finally block always work')
#         break
#
# print('block out')

# raise deyimi bizim kendi hata durumumuzu yaratmamızı sağlar


# try:
#     raise NameError('Error... It is name error ')
#
# except NameError as e:
#     print(e)

# Raise deyimi try olmadan da çalışır
# my_number = 5
# if my_number == 5:
#     raise Exception('Number cannot be equal to 5')  # exception tüm hataların hiyerarşik atası,dır
# else:
#     print(my_number)

# --> Olası bu hatayı gidermek için işte o zaman try except bloğu kullanır

# my_number = 5
# try:
#     if my_number == 5:
#         raise Exception('Number cannot be equal to 5')  # exception tüm hataların hiyerarşik atası,dır
#     else:
#         print(my_number)
# except Exception as e:
#     print('Hata', e)

# assert deyimi --> iddia anlamına gelir


my_products = []


# def add_product(product: list):
#     assert len(
#         product) != 0, 'the list is not empty'  # burda hata olmaması grektiğini iddia ediyoruz.
#     # Hata varsa output versin istiyoruz.
#     # Assert ifadesi çalışırsa sonraki hiç bir kod çalışmayacaktır
#     product.append('iphone')
#     return product
#
#
# try:
#     add_product(my_products)
# except AssertionError as e:
#     print(e)


# aynı şekilde assert kullanmak yerine raise ile de aynı işlemi else if kısmında yapabiliriz
def add_product2(product: list) -> list:
    if len(product) != 0:
        product.append('LG')
    else:
        raise Exception('Liste uzunluğu 0 değil...')
    return product


add_product2(my_products)

# ve fakat bu işlemi else if ile yaparsak hata yönetimi yapamayız
# burda programın çökmesini istemeyip sadece kullanıcıya hata mesajı vermek istiyorsak
# else if  kullanabiliriz. (raiseiz ve assertsiz)
# eğer programın çökmesini ve kullanıcıya hata vermesini istiyorsak raise
# eğer programın çökmesini isteyip geliştiriciye mesaj vermek istiyorsak assert kullanırız
