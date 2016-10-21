import turtle
from turtle_shape import arc, circle, move, polygon


jerry = turtle.Turtle()
jerry.speed(0)

# large circle
circle(jerry, 100)

# two arcs
move(jerry, 0, 100)
jerry.setheading(180)
arc(jerry, 50, 180)

move(jerry, 0, 100)
jerry.setheading(0)
arc(jerry, 50, 180)

# small circles
move(jerry, 0, 50 + 100 / 6)
circle(jerry, 100 / 6)

move(jerry, 0, 150 + 100 / 6)
circle(jerry, 100 / 6)

turtle.mainloop()
