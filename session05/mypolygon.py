import turtle

'''
#Exercise 2.1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
'''

# Exercise 2.2
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Exercise 2.3
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


jerry = turtle.Turtle()
#square(jerry, 100) 
polygon(jerry, 50, 12)

alex = turtle.Turtle()
square(alex, 30, 8) 

turtle.mainloop()  