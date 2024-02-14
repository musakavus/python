"""
 Bir sınıfta normal bir metot tanımlamak, o sınıfın bir örneği (instance) üzerinden çağrılmak üzere tasarlanmıştır.
 Ancak bazen, referans kullanmadan bir sınıfın kendisiyle ilgili işlemler yapmak isteyebilirsiniz.
 İşte bu noktada classmethod ve cls devreye girer.
 Bu konuyu bilmek için class attribute ve instance attribute kavramlarına hakim olmak lazım
"""


class Personel:
    # paramtre olarak self alan her method yada başına self. ifadesi alan her attribute, instancedır. Ve
    # sadece o referans için geçerlidir
    personel_count = 0  # class attributes

    def __init__(self, name):
        self.name = name  # instance attrübutes
        self.count()  # burası da instance attrbiutes. Çünkü self var başında
        self.count2()

    def info(self):
        print(f'{self.name} added')

    def count(self):
        self.personel_count = self.personel_count + 1

    @classmethod  # bu artık class metod
    def count2(cls):  # alışkanlık gereği cls parametresi kullanılır
        # class method olduğu için class attributeye direkt etki ediyor. Geçici değil yani
        cls.personel_count = cls.personel_count + 1


p1 = Personel('Ruin')
p2 = Personel('chain')
p3 = Personel('Ramazan')
print('Total Personel: ', p3.personel_count)  # -> outpur -> Total Personel:  1
"""
3 kere çalıştırmama rağmen 1 sonucunu aldım. Çünkü personel count ifadesi self ifadesi bağlı. dolayısıyla 
her yeni nesne oluşturulduğunda class attribute değeri yine 0'lanıyor 
"""

print('Total Personel: ', Personel.personel_count)  # -> output -> Total Personel:  0
# Doğrudan sınıf adı ile ulaştık
"""
burda da sıfır değerini alıyorum. Çünkü nesneler üzerinde yapılan değişiklikler nesne oluşturma işlemi bittikten
sonra yine sıfırlandı
"""
p4 = Personel('Ruin')
p5 = Personel('chain')
p6 = Personel('Ramazan')
print('Total Personel: ', Personel.personel_count)  # output -> Total Personel:  6
"""
Görüldüğü gibi artık 0 veya 1 değerini almadım. Class method sayesinde
Ayrıca buna da direk class ismiyle ulaşabildim
"""

print('Total Personel: ', p2.personel_count)  # output -> Total Personel:  2
print('Total Personel: ', p3.personel_count)  # output -> Total Personel:  3
print('Total Personel: ', p4.personel_count)  # output -> Total Personel:  4
"""
dikkat ettiysen sürekli 1 çıkan p1, p2, p3 referansları artık farklı değer çıkıyor
ÇÜNKÜ
classmethod, instance metod içinde geçerli. Ama instance method, classmethod için geçerli değil
"""
