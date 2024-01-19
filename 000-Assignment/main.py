"""
Python'da iç fonksiyonlar, dış fonksiyonunun yerel değişkenlerine sadece okuma erişimine sahiptir. Bu nedenle,
iç fonksiyonlar, dış fonksiyonlarının yerel değişkenlerini doğrudan değiştiremez.

Ancak, nonlocal anahtar kelimesini kullanarak iç fonksiyon içinde
dış fonksiyonunun yerel değişkenini değiştirebilirsiniz.

Eğer sadece değeri okumak istiyorsanız, erişmek mümkündür.
Ancak, değeri değiştirmek istiyorsanız, nonlocal kullanmanız gerekecektir.
"""

"""
dış fonksiyonunun yerel değişkenlerini doğrudan değiştiremez. 
İç fonksiyonlar, dış fonksiyonlarının yerel değişkenlerine sadece okuma erişimine sahiptir. 
Değişiklik yapmak için nonlocal anahtar kelimesini kullanmanız gerekiyor.
"""


def outer():
    outer_value = "Dış değişken"

    def inner():
        # Bu durumda hata alırsınız
        # dıs_degisken = "Yeni değer"
        print("İç fonksiyon içinden:", outer_value)

    inner()


outer()

print('----------')
"""
Eğer dış fonksiyonunuzun yerel bir değişkenini iç fonksiyon içinde değiştirmek istiyorsanız, 
nonlocal anahtar kelimesini kullanmanız gerekecektir.
"""


def outer():
    outer_value = "Dış değişken"

    def inner():
        nonlocal outer_value
        outer_value = "Yeni değer"
        print("İç fonksiyon içinden:", outer_value)

    inner()
    print("Dış fonksiyon içinden:", outer_value)


outer()
