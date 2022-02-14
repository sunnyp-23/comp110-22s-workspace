"""Some common commands used with the turtle."""

__author__ = 730487787
# first, need to import the library and set up our turtle object
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
side_length: float = 300
# above line constructs a new Turtle obj the program will control

leo.penup()
leo.goto(-150, 100)
leo.pendown()

leo.fillcolor(183, 123, 255)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.right(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()
bob.pencolor(12, 0, 27)
bob.penup()
bob.goto(-150, 100)
bob.pendown()
bob.speed(20)
k: int = 0
m: int = 0
while (m < 230):
    while (k < 3):
        bob.forward(side_length)
        bob.right(123)
        k = k + 1
    side_length = side_length * 0.98
    k = 0
    m = m + 1

done()