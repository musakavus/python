# assert iddia anlamına gelmektedir
# bu sayede her zaman doğru olduğunu varsaydığımız iddialarda bulunabiliriz.
# assert yazıldıktan sonra tıpkı karar yapılarındaki gibi bir koşul yazılır. Ve biz bu koşulun
# doğruluğunu daima iddia ederiz

# ve eğer assert içerisindeki bu koşul doğru ise program diğer satırları çalıştırmaya devam eder
# ancak assert içerisindeki koşul yanlışşsa program çöker ve bir hata nesnesi fırlatır.
# ve bu hata nesnesine de AssertionError deriz


# bir liste oluşturucaz ve ısrarla bu listenin içerisinin dolu olduğunu iddia edicez.
# ve eğer bu liste doluysa bir fonskiyon yardımıyla bu listeye eleman ekleyeceğiz
# AssertionError fırlatmasını isticez
# eğer boşsa hata vermesini sağlayacağız

cars = ['Ferrari']
cars2 = []


def add_item(car_list: list) -> list:
    assert len(
        car_list) != 0, 'list cannot be empty'
    # bu listenin boş olmadığı iddiasında bulunduk. Boş değilse alttaki satırları çalıştır
    car_list.append('BMW')
    return car_list
    # output: assert len(car_list) != 0  AssertionError


# print(add_item(cars))  # liste boş olmadığı için listeye sorunsuz bir şekilde eleman eklendi
# print(add_item(cars2))  # burda ise liste boş olduğu için AssertionError tarzında bir hata aldık ve program çöktü

# eğer istersek assert'e hata mesajı da verebiliriz EXTRA olarak Aşağıda-->
# --> Opsiyonel  assert len(car_list) != 0, 'List can not be empty'

# şimdi de bu örneğin hata yönetimini yapalım


# try:
#     print(add_item(cars2))  # bizim hatamız burda olabilir. Dolayısıyla bu kısmı trya yazdık
# except AssertionError:
#     print('we find an error')
#     # output: we find an error
#     # Ayrıca dikkat ettiysen assert kısmındaki hata mesajı çıkmadı. Sadece exceptteki çalıştı. Tıpkı raisedeki gibi

# hata mesajını vermek istiyorsak

# try:
#     print(add_item(cars2))
# except AssertionError as err:
#     print('we find an error')
#     print(err)

# aslında aynı işlemi if ile de yapabilirdik. Burada önemli olan nokta assert deyimi geliştiriciye ithaf edilir
# yani amaç "programın çökmesi" değil de "kullanıcıya" mesaj vermekse if kullanılır.
# Ayrıca sadece if le hata yöentimi yapılamaz

# Amaç programın çöküp hata yönetimi yapmaksa assert veya raise kullanılır
# Program çöktükten sonra amaç hata yönetimi yapılıp "kullanıcıya" mesaj vermekse raise deyimi kullanılır
# amaç geliştiriciye mesaj vermekse asert deyimi kullanılır

# bir diğer fark assert ile sadece AssertionException hatası fırlatılır
# raise ise bizim oluşturduğumuz veya kullandığımız hazır bir classsın hatasını fırlatabiliyoruz


# diyelim ki kullanıdığım django versiyonu  güncel değil ve yetersiz kalıyor bazı modüller için.
# o halde assert kullanacağız. Çünkü bu geliştirici bazlı bir hata


# sayi1 = 5
# sayi2 = 0
# try:
#     raise NameError('Name error hatası alındı')
#
# except NameError as err:
#     print(err)
#
# else:  # sadece hata meydana gelmezse çaışır
#     pass
#
# finally:  # her türlü çalışır
#     pass

my_number = 4

try:
    assert my_number == 5, 'bir hata meydana geldi'
except AssertionError as err:
    print(err)
