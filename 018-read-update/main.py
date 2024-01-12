# utf-8 kullanmazsak türkçe karakter kullanamayız
with open('document.txt', 'w', encoding='utf-8') as f:
    f.write('hi friend\n')
    f.write('are u okay?\n')
    f.write('i think u are!')

with open('document.txt', 'r') as f:
    print(f.read(4))  # burda sadece 4 karakter oku diyoruz. İmlec nerde kaldıysa orda devam ediyor
    print(f.read())  # burda KALAN hepsini oku diyoruz.
    print('read fonksiyonun return tipi: ', type(f.read()))  # f.read fonkysionun return tipini göster

# imlecin hareketlerini normalde pythonda yazarken imlec nasıl davranıyorsa öyle kabul etmelisin
# boşlukları da 1 karakter olarak kabul eder

print("-----------")
# şimdi de readline()
with open('document.txt', 'r') as f:
    print(f.readline(), end='')  # readline fonksiyonu satur satır okumamıza yardımcı olur
    print(f.readline(), end='')  # cümle sonlarında kullanıdğım \n yi silmek için kullandım sadece
    print(f.readline(), end='')
    print(f.readline(), end='')
    print(f.readline(5), end='')  # paramtre olarak sayı verirsen yine karakter karakter okur

print("-----------")
# şimdi de readlines()
with open('document.txt', 'r') as f:
    print(f.readlines())  # readlinedan  farkı normalde return değeri str iken bunda list şeklinde döndürüyor
    # output--> ['hi friend\n', 'are u okay?\n', 'i think u are!']
    print(type(f.readlines()))  # output--> <class 'list'>
    # içine paramtre yazarsak
    print(f.readlines(5))  # 5. karakter hangi satıra aitse o satırın tümünü liste şeklinde veriyor
    # burda output [] boş liste oldu çünkü imlec readlines'de tüm satırları okuduğu için sonraki liste birşey kalmadı

print("-----------")

with open('document.txt', 'r') as f:
    # içine paramtre yazarsak
    print(f.readlines(5))  # 5. karakter hangi satıra aitse o satırın tümünü liste şeklinde veriyor
    print(f.readlines())  # imlec kaldığı yerden devam eder
    print(f.readlines())  # boş liste verir
    print(f.readlines())  # boş liste verir

print('------------------')
# tabi okuma işlemini başka şekildede yapabilriz mesela for döngüsü sayesinde
with open('document.txt', 'r') as f:
    for satir in f:
        print(satir, end='')
        # output-->
        # hi friend
        # are u okay?
        # i think u are!

print()
print('----------------')
# yada liste şeklinde almak için
with open('document.txt', 'r') as f:
    data = f.readlines()  # tüm satırları tek bir listede topladık
    for satir in data:
        word = satir.split()  # böylelikle her satırı kelimelere bölüp tüm kelimeleri liste şeklinde döndürdük
        print('Her satır ve o satırdaki her kelime ayrı ayrı tek listede,', word)

print('-------------')
print('Tüm satırlar bir eleman ve tek listede', data)

# open fonksiyonunun default modülü 'r'dir. Yani read işlemi yapacaksan r yazmana gerek yok ama seni yine de yaz


# şimdi de imlec konumlarıyla oynayalım

with open('document.txt', 'r') as f:
    print(f.tell())  # imlecin o anki konumunu gösterir--> output: 0
    print(f.read())  # tüm dosyayı okur
    print(f.read())  # boş
    print(f.tell())  # imlecin güncel konumu: --> 38
    f.seek(0)  # imlecin yeni konumu: 0 --> (imlec içindeki indise gider)
    f.read()  # yine tüm dosyayı okur
    f.seek(6)  # imlecin yeni konumu --> 6

# dosya güncelleme işlemi için
"""
r+ --> Read(+) --> Dosya okuma yazma
w+ --> Write(+) --> Dosya okuma yazma. Dosya zaten var ise yeniden oluşturur
a+ --> Append(+) --> Dosya okuma ekleme
x+ --> Create(+) --> Dosya okuma yazma. eğer dosya yoksa oluşturur. Varsa hata verir
"""

# şimdi mantık oldukça basit. Dosyaya ekleme işlemi yapabilmem için önce okuyabilmem lazım mantıken

with open('document.txt', 'r+') as f:
    temp_data = f.read()  # eski datayı bir değişkene atadık
    # şu an imlecimiz en sonda.
    f.seek(0)  # başa ekleme yapacaksak imlecimizi tekrar en başa alalım
    added_data = 'ruinchain\n'  # eklenecek yeni data
    new_data = added_data + temp_data
    f.write(new_data)
# burda amaç "istediğimiz" bir yere veri eklemekti. Dolayısıyla dosyayı okumamız gerekiyordu

# eğer veriyi en sona ekleyeceksek dosyayı okumamıza gerek yok

try:
    added_data = '\nbest'
    f = open('document.txt', 'a+')
    f.write(added_data)
except OSError as err:
    print(err)

finally:
    f.close()

# yine dosyanın herhangi bir yerine veri eklemek için şu metodu da kullanabiliriz
# mantıken yine okumam lazım
with open('document.txt', 'r+', encoding='utf-8') as f:
    added_data = 'a data piece'  # eklenecek yeni data
    all_data_list = f.readlines()  # tüm satırları ayrı ayrı bir liste şeklinde ele alalım
    print(all_data_list)  # yazdıralım -->  ['ruinchain\n', 'hi friend\n', 'are u okay?\n', 'i think u are!\n', 'best']
    all_data_list.insert(2, added_data)  # 2. indise eklenecek datayı yazaım
    f.seek(0)  # tekrardan başa dönelim
    f.writelines(all_data_list)  # dosyayı tekrar oluşturup satır şeklinde ekleyelim

