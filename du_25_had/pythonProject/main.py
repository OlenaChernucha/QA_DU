from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("Welcome ti the snake game")
screen.setup(width=800, height=500)
screen.tracer(False)

head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

while True:
    move()
    time.sleep(0.1)
    screen.update()




screen.exitonclick()
