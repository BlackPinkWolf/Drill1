import turtle
import random

def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,100))
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_move, 'w')
turtle.onkey(drunken_move, 'a')
turtle.onkey(drunken_move, 's')
turtle.onkey(drunken_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
