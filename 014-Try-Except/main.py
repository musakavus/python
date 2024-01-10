"""
Error Types:
Syntax
Logic
Exception
"""

# except olmadan try çalışmaz.Her try'ın muhakkak bir exceptionu olmalı

# Shift + * --> todo list

try:
    number = int(input('please enter an integer number: '))
    print('Your entered number: ', number)

except ValueError:
    print('You can entered just integer. Pls try again')

print('block-out')

while True:
    try:
        mark = int(input('please enter your mark: '))
        average = int(input('Total count: '))
        division = mark / average
        print('your entered number: ', average)
        break
    except ValueError:
        print('pls enter an number...')
    except ZeroDivisionError:
        print('Total count can not be Zero. Try again...')

print('block-out')

# TODO: Else

# TODO: Raise
