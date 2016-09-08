import math
# print(math.pi)
'''
comment sample

another comment

'''

# comment

# print('Over.')

age = 21
if age >= 21:
    print('Yes, you can.')
else:
    print('Sorry.')


import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
days = current// 60 //60 //24
print('Current time: %d days, %d hours, %d minutes and %d seconds from Epoch.' % (days, hours, minutes, second))

input()
