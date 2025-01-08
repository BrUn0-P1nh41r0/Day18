from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.pensize(7)
turn = [0, 90, 180, 270]
tim.speed(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours

for steps in range(150):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(turn))

screen = Screen()
screen.exitonclick()
