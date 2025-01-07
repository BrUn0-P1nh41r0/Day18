from turtle import Turtle, Screen, pos
import random

tim = Turtle()
tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(7)
turn = [0, 90, 180, 270]
tim.speed(10)

for steps in range(150):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(turn))

screen = Screen()
screen.exitonclick()
