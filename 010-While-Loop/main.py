"""
while döngüsü, belirli bir koşul karşılanana kadar bir bloğu
tekrar tekrar çalıştırmak için kullanılır.
Koşul yanlış olduğunda (False), döngüden çıkılır ve döngünün hemen
sonrasındaki satır çalıştırılır.
"""

"""
while expression:
    statement(s)
    
expression: Döngünün devam etmesi veya sona ermesi için bir koşul ifadesidir.
statement(s): Koşul doğru olduğu sürece tekrarlanacak olan ifadeler.
"""
number = 1
while number < 5:
    print(number)
    number += 1

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
    print(s[i])

    # break the loop as soon it sees 'e'
    # or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1

print("Out of while loop ")
