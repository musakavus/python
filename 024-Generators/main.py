"""
Generators konusunu bilmek için iteratos konusunu iyi bilmek gerek.
İterasyon konusunda bir iteri tümüyle gezdikten sonra başa dönemiyorduk. Ve tüm elemanlar sonlandıktan sonra kalıyorduk
Çünkü nesne tükeniyor ve tekrar gezme işlemi yapamıyoruz.
Fakat for döngüsünde tekrar ve tekrar gezebiliyoruz ve kullanabiliyoruz.

Şimdi de generators konusunda bu işleri daha ileri götürüyoruz
Generatorleri oluşturup bir kere kullandığımızda tek kullanımlık olarak çalışır.

Örneğin bir listeyi istediğimiz kadar for döngüsüne koyup kullanabiliriz.
Ama bir generatorle oluşturulan bir yapıyı sadece bir kez kullanabiliriz. Hafızadan hemen değerleri unutulur.
Dolayısıyla bu da bize
* Bellek Verimliliği:
Generator'lar, elemanları tek seferde belleğe yüklemezler. Bunun yerine, her bir elemanı ihtiyaç duyulduğunda üretirler.
 Bu özellik, büyük veri setleri üzerinde çalışırken bellek kullanımını optimize eder.
 Özellikle, büyük veri setleri üzerinde döngü yaparken generator'lar, bellek tüketimini minimize eder.

* Lazy Evaluation(Lazımlık)
Generator'lar, elemanları sadece talep edildiğinde üretirler. Bu, tüm elemanların hemen hesaplanmasını gerektirmez,
bu da işlemleri geciktirme veya gerektiğinde başlatma yeteneği sağlar.
Bu özellik, programın daha verimli çalışmasını sağlar.

* Sonsuz veriler elde etme
Generator'lar, sonsuz serileri temsil etmek için kullanılabilir. Örneğin, range() fonksiyonu sadece belirli bir aralığı
temsil edebilirken, bir generator fonksiyonu ile sonsuz bir sayı serisi temsil edebilirsiniz.

"""


# --> bir generatoru oluşturabilmek için kullandığımız yapıda yield deyimini kullanırız. Yield deyimi de tıpkı
# return değeri gibidir. Return'den farkı return gibi fonksiyondan çıkış yapmaz. Sadece değerini döndürür. Bir sonraki
# iterasyonu bekler

def func():
    my_number = 0
    yield my_number

    my_number = my_number + 2
    yield my_number

    my_number = my_number + 4
    yield my_number

    my_number = my_number + 6
    yield my_number


data = func()
print(data)  # output: --> <generator object func at 0x0000023B1CAC68C0>
print(type(data))  # output --> <class 'generator'>
# data'nın bir generator olduğunu yield deyimi sayesinde anlıyor
# fakat dikkat ettiysen ekran çıktısı alamıyorum elemanlara dair. Bunun için next deyimini kullanmam lazım. Çünkü-->
# generatorlerde bir iteratördür bu yapıya sahiptir

"""
print(next(data)) # 0 yazdırdı
print(next(data)) # 2 yazdırdı
print(next(data)) # 6 yazdırdı
print(next(data)) # 12 yazdırdı

yield nerede kaldığını unutmuyor. İki kere next deyimini kullanırsan 2 ve 6 yı yazdırır

print(next(data)) derken fonksiyon içerisine giriyor yield deyimini arıyor. Yield deyimi hangi değeri döndürüyorsa
sonuç olarak onu veriyor.  bir kez daha gezme işlemi yaparsan 2 sonucunu alırsın çünkü kaldığı yeri unutmuyor.
Daha doğrusu 0 2 sonucu. Burayı karıştırma iki kere next yaptığın için farklı farklı 0 ve 2 değerini döndürüyor
yukarıdaki kodu çalıştırırsan (printli kısımları) aşağıdaki kod çalışmaz. Aslında çalışır ama sonuç vermez.
Hemen stopiteration hatasını yakalar
Çünkü generatörler bir kez kullanılıp siliniyordu
"""

while True:
    try:
        print(next(data))
    except StopIteration:
        break

my_range = range(1, 11)  # kendi range'ni belirtebilirsin


def add_list() -> list:
    my_list = []
    for value in my_range:
        my_list.append(value * value * value)

    return my_list


data = add_list()
print(data)


# yukarıdaki bu işlemi yaparken aslında pythonun belleğini çok yormuş oluyoruz. Neden çünkü ppython bu yapıları birden
# oluşturmaya çalışıyor. Mesela 1 den 1000'e kadar olan sayıları listelersek eğer (return my_list) kısmı mesela
# bu liste birden oluşturulduğu için pythonun belleği yorulmuş olacak. İşte bu tarz ifadelerde generatorlerin
# faydalarını görmüş oluruz

def triple(a):
    yield a * a * a


for data in my_range:
    result = triple(data)
    print(next(result))

print(type(triple(data)))

print('-------------')


# yada bir benzer işlem:
def calculate(p1):  # p1:range(1,5)
    for item in p1:  # item:1, item:2, item:3, item:4
        yield item * item * item  # 1 , 8, 27,67


a = range(1, 5)
v1 = calculate(a)  # v1 im artık 4 tane eleman taşıyor. normalde burda fonksiyona gitmemiz gerekiyor.
# Ama biz gitmicez. Çünkü bu yapının generator olduğu anlaşılıyor fonksiyondaki yield değerinden dolayı.
# Ve generatörler "oluşturulduklarında" değil, sadece " tek tek çağırıldıklarında" üretilirler
# args yada kwargs şeklinde toplu şekilde değil yani
print('type of v1: ', type(v1))
# calculate(a)'dan yield değeri döndüğü için v1 artık generatordur
for function_item in v1:  # function_item = v1(), v2(), v3(), v4() , toplamda 4 tane elemanım var.
    # Her biri için for'un içine giriyorum
    # ve asıl şimdi calculate fonksiyonun içine gideceğiz. Çünkü artık tek tek çağırıyoruz
    print(function_item)

for function_item in v1:
    # bu tekrar çalışmaz. Çünkü "tüm" generatörler üstteki for döngüsünde gezildiği ve üretildiği için yokedildi
    print(function_item)  # dolayısıyla burdan boş değer alırız

# range deyimi önemli
# range deyimi oluşturulduğunda hemen çıktı alamıyorsun. Örnek aşağıda
our_range = range(5, 11)
print(our_range)  # görüldüğü gibi çıktı olarak --> range(5, 11) sonucunu aldım. Değerleri göstermedi.
# çünkü değerlerini sadece biz kullandığımız zaman oluşturuluyor. Bu da bellekten ve zamandan tasarruf sağlıyor
# dolayısıyla range, generatörler mantığına çok uygundur
# eskiden pythonun 2. versiyonunda range ve xrange diye bir fonksiyon vardı. xrange değerinin rangeden farkı şuydu:
# xrange kullandığın zaman liste şeklinde değerleri tutuyordu. Belki hatırlarsın eskiden görüyordun xreangeyi for'larda
# python 3 ile bu kaldırıldı. xrange'nin yerine de artık range kullanılıyor. Unutma zaman ve bellek
# data = range(1,500) desen bile sorun yok. Çünkü sadece kullanılınca oluşturulucak değerler

your_range = range(1, 25)  # belirttik ama henüz değerleri oluşturmadık

for value in your_range:  # şu an kullandık mesela. Kullanılan değerler hafızadan silinir.
    # Dolayısıyla bu şu anlama gelir. Range fonksiyonu da generatörlerle yazılmış diyebiliriz
    print(value, end=' ')

# işimiz bitince kullanmayacağımız kapsamlı değerler için generatörleri kullanalım. Büyük avantaj
