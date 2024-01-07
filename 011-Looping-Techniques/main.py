"""
Python, rekabetçi programlamada ve özellikle belirli döngü yapılarının gerektiği
projelerde zaman ve bellek tasarrufu sağlayan çeşitli gelişmiş döngü teknikleri sunar.
Bu teknikler özellikle ek değişkenlere ihtiyaç duyulmadığında zaman ve bellek tasarrufuna yardımcı olur.
"""
# enumurate() kullanımı
"""
enumerate() fonksiyonu, konteyner üzerinde dolaşmak için kullanılır ve indeks numarasını, 
o indeksteki değeri yazdırmak için kullanılır. Bu özellikle elemanların sırasının 
korunması gerektiğinde kullanışlıdır.
"""
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

# zip() kullanımı
"""
zip() fonksiyonu, iki veya daha fazla konteyneri birleştirerek 
değerleri sırayla yazdırır. Bu özellikle iki veya daha fazla farklı türde 
veri yapısını birleştirmek için kullanılır.
"""
my_cars = ['Audi', 'Seat', 'Opel']
my_models = ['A3', 'Leon', 'Astra']

for car, model in zip(my_cars, my_models):
    print('Car: ', car)
    print('Model', model)

# reversed() kullanımı
"""
reversed() fonksiyonu, konteynerdaki değerleri ters sırayla yazdırmak için kullanılır. 
Bu, orijinal listeye herhangi bir değişiklik yapmaz.
"""
marks = [45, 57, 39, 78, 29, 13, 98]
for mark in reversed(marks):
    print(mark, end=' ')

print()
