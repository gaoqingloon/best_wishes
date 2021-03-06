import turtle
import random
from common.constant import *



def draw_heart(delay=0):

    me = "qinglong.gao"
    """
    turtle.speed(0)
    “fastest”: 0
    “fast”: 10
    “normal”: 6
    “slow”: 3
    “slowest”: 1
    turtle.Turtle().screen.delay(0)
    """
    # love = HEART_PARSE[random.randint(0, len(HEART_PARSE) - 1)]
    t = turtle.Turtle()
    t.hideturtle()
    t.screen.delay(delay)
    heart_phrase = get_heart_phrase()

    love = heart_phrase[random.randint(0, len(heart_phrase) - 1)]

    # turtle.setup(width=900, height=500)
    # turtle.reset()
    turtle.setup()
    turtle.color('red', 'red')
    turtle.pensize(1)
    turtle.up()
    turtle.hideturtle()
    turtle.goto(0, -180)
    turtle.showturtle()
    turtle.down()
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
    # turtle.write(love, font=('gungsuh', 14,), align="center")
    # turtle.write(love, font=(10,), align="center")
    turtle.write(love, align="center", font=("Courier", 14, "bold"))

    turtle.up()
    if me != '':
        turtle.color('green', 'red')
    turtle.goto(180, -180)
    turtle.write(me, font=(20,), align="center", move=True)
    # turtle.write(me, align="center", font=("Courier", 12, "bold"))

    turtle.mainloop()
    # window = turtle.Screen()
    # window.exitonclick()


def little_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


if __name__ == '__main__':
    for i in range(1):
        print(i)
        try:
            draw_heart()
        except Exception as e:
            draw_heart()
        time.sleep(2)
