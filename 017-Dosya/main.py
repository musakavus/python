import os

# dosya işlemleri
"""
bir dosya işlemi herhangi bir uygulamanın önemli bir parçasıdır.
bu zamana kadar programlarımızda kullanıcyla etkileşime geçtiğimiz zaman bir değeri
değişkenlere atayıp kullanabiliyorduk. Ama bu program kapanana kadardı. Program
kapanınca bilgi de kayboluyordu.
Ama biz dosya işlemleri sayesinde bu değerleri dosyalarda tutup, bu değerleri okuyarak
çeşitli işlemler yapabiliriz. Yani bilgilerimizi geçici hafızadan kalıcı hafızalara taşımış oluruz
"""
# w modu: Write --> Yeni dosya yazma/oluşturma modu--> Eğer aynı isimde dosya mevcutsa o dosyasyı silip yenisini açar
# open('deneme.txt', 'w')  # path belirtmezsen bulunduğun dizini baz alır
# open('C:/Users/M/Desktop/FullStackk/Python/017-Dosya/deneme.txt', 'w') # bu şekilde path ve yanına da modu yazarsın

try:
    open('C:/Users/M/Desktop/FullStackk/Python/017-Dosya/deneme.txt', 'w')

except FileNotFoundError as err:
    print(err)
    print('Böyle bir dosya yolu yok')

# temelde open fonksiyonu iki paramtre alır. İlk parametre dizin,ikincisi de hangi işlemi yapazağımız.(ikiside str tipi

open('../metinbelgesi.txt', 'w')  # burda .. işareti bir üst klasöre çık demek
