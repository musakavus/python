"""
Aggregation bir sınıfın, başka bir sınıfı içermesi anlamına gelir. bu ilişki "has a" ilişkisidir.
Bir sınıf, diğer bir sınıfın örneğini içerir. Ancak bu örnekler ayrı ayrı var olabilir ve birbirinden bağımsız olabilir.

Peki aggreagation ilişkisine örnek verelim. bu bağ zayıfır mesela
-> Üniveriste - Öğrenci ilişkisi
Bir üniversite bir öğrenciye sahip olabilir. Ancak bir öğrenci üniversiteye bağlı olmayabilir.(Örneğin mezun olmuş
olabilir veya başka bir üniversitede olabilir
"""


class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # Creating a list to store the students of the course

    def add_student(self, student):
        self.students.append(student)


# Creating student objects
student1 = Student("Ali", 123)
student2 = Student("Ayse", 456)

# Creating a course object
course = Course("Math")

# Adding students to the course
course.add_student(student1)  # student1 = object main at 0X6483438
course.add_student(student2)

# Listing the students of the course
print(f"Students of {course.name} course:")
for student in course.students:
    print(f"Name: {student.name}, Number: {student.number}")

"""
 Biz burda referasn değeri veriyoruz ya parantez içerisine. Referans, nasıl listeye eklenebiliyor ki

ChatGPT
Anladım, aslında burada bir referans değeri verilmiyor. add_student yöntemi, öğrenci nesnesini dersin öğrenciler 
listesine eklemek için kullanılıyor. student1 ve student2 nesneleri, Student sınıfının örnekleridir ve bu nesnelerin 
kendileri değil, referansları dersin öğrenciler listesine eklenir.

Python'da nesnelerin kendileri değil, referansları bellekte tutulur ve bu referanslar üzerinden nesnelere erişilir. 
Dolayısıyla, add_student yöntemi çağrılırken student1 ve student2 nesnelerinin referansları 
dersin öğrenciler listesine eklenir. Bu sayede, dersin öğrenciler listesi, öğrencilerin referanslarını içerir ve 
bu referanslar üzerinden öğrencilere erişilebilir.

Yani, add_student yöntemi çağrıldığında, student1 veya student2 nesnelerinin kopyaları değil, doğrudan bu nesnelerin bellekteki referansları dersin öğrenciler listesine eklenir. Bu şekilde, dersin öğrenciler listesi, bu öğrencilere erişmek için gerekli olan referansları içerir.
"""
