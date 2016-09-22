'''
age = int(input('How old are you?'))

if age >= 21:
    print('Your age is {}.'.format(age))
    print('Your age is ' + str(age) + '.')
    print('Yes, you can.')
elif age >= 6:
    print('Your age is ', age)
    print('You are a teenager. No, you cannot.')
else:
    print('Your age is ', age)
    print('No, not allowed.')

if age >= 6 and age <18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

'''

# Nested
x = 1
y = 2
if x == y:
    print('x and y are equal.')
else:
    if x < y:
        print('x is less than y.')
    else:
        print('x is greater than y')
