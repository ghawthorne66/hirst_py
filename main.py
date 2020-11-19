import turtle as turtle_module
import random
from colors import color_list

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

