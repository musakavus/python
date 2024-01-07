"""
if ifadesi, belirli bir koşulu kontrol eder ve eğer bu koşul doğruysa
ilgili bloğu çalıştırır.
"""

my_number = 15
if my_number > 12:
    print('Koşul sağlandı. Sayınız: ', my_number)

# else ifadesi, bir önceki if ifadesi yanlışsa çalışacak olan bloğu belirtir.
if my_number > 16:
    print('koşul sağlandı. Sayınız: ', my_number)
else:
    print('koşul sağlanamadı...')

"""
elif ifadesi, bir önceki if veya elif ifadesi yanlışsa ve kendi koşulu 
doğruysa çalışacak olan bloğu belirtir. Birden fazla elif ifadesi kullanılabilir.
"""
if my_number > 16:
    print('Koşul sağlandı. Sayınız ', my_number)
elif my_number == 15:
    print('Elif sağlandı. Sayınız: ', my_number)
else:
    print('Hiçbir koşul sağlanamadı')

"""
if, else, ve elif ifadeleri iç içe kullanılabilir. 
Bu, daha karmaşık koşulları ele almak için kullanışlıdır.
"""
a = 15

if a > 10:
    print("a, 10'dan büyük")
    if a > 20:
        print("a, 20'den büyük")
    else:
        print("a, 20'den küçük veya eşit")
else:
    print("a, 10'dan küçük veya eşit")

"""
Kısa yol if-else ifadesi, if ve else bloklarında yalnızca bir ifadeye ihtiyaç duyulduğu durumlarda, 
if ve else ifadelerini tek bir satırda yazmak için kullanılabilir.
"""
my_number = 10
if my_number > 9: print('your number bigger than 9')

"""
statement_when_True if condition else 
"""
my_number2 = 8
print(True) if my_number2 < 8 else print(False)

