from turtle import Turtle, Screen
import heroes


tim = Turtle()
tim.shape("turtle")
tim.color("blue")


for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen = Screen()
screen.exitonclick()
