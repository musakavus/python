"""
 nesne yönelimli programlamada bir sınıfın başka bir sınıfı içermesi ve bu içerilen sınıfın ömrünün,
 içeren sınıfın ömrüne bağlı olması durumudur. Composition, "has-a" ilişkisi ile tanımlanır ve
 aggregation'dan farklı olarak daha güçlü bir ilişkiyi ifade eder, çünkü içerilen nesnenin ömrü,
 içeren nesnenin ömrüne bağlıdır.
"""

"""
Compositiona örnekler
0-> Kitap ve sayfalar: Kitap kaybolduğunda sayfalar da kaybolur
1-> Ev ve mobilya: Bir ev yok olduğunda mobilyalar da yok olur
2-> Bilgisayar ve bileşenleri: Bir bilgisayar yok olduğunda bileşenler de yok olur
3-> Restoran ve mutfak ekipmanları
"""

import time


class Part:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running.")


class Computer:
    def __init__(self):
        self.cpu = Part("CPU")
        self.memory = Part("Memory")
        self.storage = Part("Storage")

    def boot_up(self):
        print("Computer is booting up.")
        self.cpu.run()
        self.memory.run()
        self.storage.run()


c1 = Computer()
c1.boot_up()

"""
Yalova Üniversite -> class
login işlemi
entered_mark işlemi
seen işlemi
ubs -> class
"""

print('-' * 45)


class University:  # university classı olmasa Ubs classının hiç bir anlamı yok.
    def __init__(self):
        self.login = Ubs('Giriş')  # burada diğer sınıfın referansını oluşturduk
        self.entered_mark = Ubs('Not girme')
        self.seen = Ubs('Görüntüleme')

    def send(self):
        self.login.show()  # burda da referansı oluşturulan classın metodunu çağırdık
        self.entered_mark.show()
        self.seen.show()


class Ubs:
    def __init__(self, islem):
        self.islem = islem

    def show(self):
        time.sleep(1)
        print(f'{self.islem} işlemi yapıldı...')


university1 = University()
university1.send()
time.sleep(1)


class Department:
    def __init__(self, name):
        self.name = name

    def create_department(self):
        print(f'Department Name: {self.name}')


class Student:
    def __init__(self, name, surname, num, department):
        self.name = name
        self.surname = surname
        self.num = num
        self.department = Department(department)

    def add_student(self):
        print(self.name + ' ' + self.surname + ' ' + self.num + ' added')


s1 = Student('Musa', 'Kavuş', '15010105', 'computer Engineer')
s1.add_student()
s1.department.create_department()
