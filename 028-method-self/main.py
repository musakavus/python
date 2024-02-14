"""
metodlar için eylem diyebiliriz
Örneğin bir insanın eylemleri olur. Bir arabanı bilgisayarın eylemleri davranışları olur.
Buna biz class içerisindeki "methodlar" deriz.
İşte biz bu yüzden bir sınıf içerisindeki eylemleri veya davranışları bildirirken method kullanırız.
Bir insanın hava alması yürümesi maaş alması. Hepsi bir eylemdir davranış bildirir
"""


class Car:
    # metod
    def speed(self):  # eğer bir fonksiyon class içerisinde ise artık  methoddur
        print('my speed 105')


car1 = Car()
car1.speed()  # speed ise bir methoddur. Çünkü kullnabilmem için bir referans kullanmam gerekiyor

# misal len() bir fonksiyondur. Çünkü her yerde kullanabilirim
"""

Self kelimesinin kullanımı, sınıf içindeki metotlarda objeye erişmek için kullanılır. 
Metotların içinde geçen self ifadesi, o metoda ait olan objeyi ifade eder. Bu sayede sınıf özelliklerine ve metotlarına 
erişmek mümkündür.

Self kelimesinin kullanımı, nesneler arasında veri aktarımının nasıl yapıldığına dair de bir açıklama sunar. 
Her obje kendi verilerine sahip olduğundan, self kelimesi bu veriler arasında geçiş yapmamızı sağlar.

Self kelimesi, genellikle başka programlama dillerindeki this kelimesi gibi kullanılır. 
Sınıfın kendisini ifade eder ve objenin referansını gösterir. 
Herhangi bir sınıf metodu tanımlanırken, ilk parametre olarak self ifadesi kullanılır. 
Bu sayede, sınıf içindeki özellik veya metotlara erişmek mümkün hale gelir.

Self kelimesi, sınıfın özelliklerinde veya metotlarında kullanılabilen diğer değişkenlere benzer şekilde kullanılır. 
Ancak bir farkı vardır; self kelimesi, sınıfın kendi nesnesi içindeki verileri ifade ederken, 
diğer değişkenler sınıfın dışındaki verileri ifade eder.

Kısacası, self kelimesi kullanılarak sınıfın özellikleri ve metotları arasında bağlantı kurulur 
ve nesneler arasındaki veri aktarımı sağlanır. Bu da sınıf yapısının anlaşılmasını ve kodun okunabilirliğini artırır.
"""


class Person:
    name = ''
    height = 0
    weight = 0

    def dance(self):
        print('hi. I am: ', self.name)  # self ifadesini kullanmazsan pythn bunun hangi nesnenein adı olduğunu çözemiyor
        # 2-> Nesne o esnada oluşturuldu mu oluşturulmadı mı haberi yok. Ayrıca henüz bellekte yer ayrıldı mı bilmiyoruz
        # yani biz aslında diyoruz ki, ad'a ulaş ama bellekte şu adreste bulunan şu nesnenin ad'a ulaş


p1 = Person()
p1.name = 'Ruin'
p1.dance()  # neden parametre vermedik. Çünkü arkaplanda p1 = self ataması yapıldı


# self ifadesi her zaman referansın (objenin9 değerini ifade eder.
# böylelikle biz hangi obje nesne referans için o metodu kullandığımızı anlarız p1=self ifadesinden p1 için çağırdığımız
# anlarız

# peki şimdi şu soruyu sormamız lazım. Method içerisinde parametre verdik AMA
# nesneyi oluşturup methodu çağırınca vermedik. Neden
# çünkü python bunu arkpalanda bizim için yapıyor. Ve ordaki self parametresini bizim referansımıza objemize eşitliyor
# yani mantıken p1 = self yapıyor bizim için

class Animal:
    def animal_name(self):
        return self


a1 = Animal()
data = a1.animal_name()
print(data)  # <__main__.Animal object at 0x000001C059D7CDA0>
# görüldüğü üzere selfi döndürdüm. Ve yazdırdığım zaman bunun bir obje olduğunu anladım

print(a1)  # <__main__.Animal object at 0x000001FB9FAECDD0>
print(data)  # <__main__.Animal object at 0x000001FB9FAECDD0>

# yani a1 aslında return edilen self ifadesine eşit. Çok önemli

"""
def dance(self):
    return name 
    --> python burda diyor ki bize, sen name ifadesini döndürmek istiyorsun ama kimin neyin name'si. 
    Ayrıca nesne oluşturdun mu haberim yok diyor
 
def dance(self):
    return self.name
    -> fakat burda diyoruz ki pyhon'a sen p1. ismini getir. p1 in ismi neydi. Tanımlamıştık p1.name = 'xxxx' diye 
    tanımlamıştık
    -> Python o zaman anlıyor    

Biz bu self paramtresini kullansak da kullanmasak da vermek zorundayız    
"""
