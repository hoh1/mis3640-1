import math

def quadratic(a, b, c):
    A = b**2-4*a*c # calculate the discriminant
    
    if A >= 0: #equation has solutions
        X1 = ((-b + math.sqrt(A))/2*a)
        X2 = ((-b - math.sqrt(A))/2*a)
        return X1,X2
    
    else:
        #print('No Real Number Solution')
        return "Anything"


#print(quadratic(2,2,2))
#print(quadratic(1,4,1))

a = int(input('please enter a number:'))
b = int(input('please enter a number:'))
c = int(input('please enter a number:'))
print('results are:')
msg = quadratic(a,b,c)
print(msg)