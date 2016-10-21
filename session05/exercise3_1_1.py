from turtle_shape import arc, circle, move, polygon
import turtle
import math

# 3.1.1


jerry = turtle.Turtle()
jerry.speed(0)

# large circle
circle(jerry, 100)

# 4 triangles
move(jerry, 0, 100)
jerry.setheading(60)
polygon(jerry, 3, 100)
jerry.setheading(150)
polygon(jerry, 3, 100)
jerry.setheading(240)
polygon(jerry, 3, 100)
jerry.setheading(330)
polygon(jerry, 3, 100)


# 4 small circles
moving_step = 50 * math.sqrt(3)
small_radius = 50 * math.sqrt(3) / 3

move(jerry, 0, 100 - moving_step)
jerry.setheading(0)
circle(jerry, small_radius)

move(jerry, moving_step, 100)
jerry.setheading(90)
circle(jerry, small_radius)

move(jerry, 0, 100 + moving_step)
jerry.setheading(180)
circle(jerry, small_radius)

move(jerry, -moving_step, 100)
jerry.setheading(270)
circle(jerry, small_radius)


turtle.mainloop()
