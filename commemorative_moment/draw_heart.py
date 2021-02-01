import turtle
import random
from common.constant import *


def draw_heart():
    try:
        me = "qinglong"
        love = HEART_PARSE[random.randint(0, len(HEART_PARSE) - 1)]
        # turtle.setup(width=900, height=500)
        turtle.reset()

        turtle.setup()
        turtle.color('red', 'red')
        turtle.pensize(1)
        turtle.speed(100) #
        turtle.up()
        turtle.hideturtle()
        turtle.goto(0, -180)
        turtle.showturtle()
        turtle.down()
        turtle.speed(200) #
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(224)
        little_heart()
        turtle.left(120)
        little_heart()
        turtle.forward(224)
        turtle.end_fill()
        turtle.pensize(5)
        turtle.up()
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.showturtle()
        # turtle.color('#CD5C5C', 'blue')
        turtle.color('blue', 'blue')
        # turtle.write(love, font=('gungsuh', 10,), align="center")
        turtle.write(love, font=(10,), align="center")
        turtle.up()
        turtle.hideturtle()
        if me != '':
            turtle.color('green', 'red')
        turtle.goto(180, -180)
        turtle.showturtle()
        turtle.write(me, font=(20,), align="center", move=True)
        # window = turtle.Screen()
        # window.exitonclick()
    except Exception:
        pass


def little_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
