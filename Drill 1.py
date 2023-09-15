import turtle
import random

def drunken_move1():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_move2():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_move3():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def drunken_move4():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_move1, 'w')
turtle.onkey(drunken_move2, 'a')
turtle.onkey(drunken_move3, 's')
turtle.onkey(drunken_move4, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
