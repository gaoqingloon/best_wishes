import turtle
from utils.valid_util import *


def skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mk_hand(name, length):
    """
    注册Turtle形状，建立表针Turtle
    :param name:
    :param length:
    :return:
    """
    turtle.reset()
    skip(-length * 0.1)
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    hand_form = turtle.get_poly()
    turtle.register_shape(name, hand_form)


def init():
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mk_hand("secHand", 125)
    mk_hand("minHand", 130)
    mk_hand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()


def setup_clock(radius):
    """
    建立时钟的表盘
    :param radius:
    :return:
    """
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            skip(-radius - 20)
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)


def format_week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def format_date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)


def tick():
    """
    绘制表针的动态显示
    :return:
    """
    try:
        t = datetime.datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        secHand.setheading(6 * second)
        minHand.setheading(6 * minute)
        hurHand.setheading(30 * hour)

        turtle.tracer(False)
        printer.forward(65)
        printer.write(format_week(t), align="center", font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(format_date(t), align="center", font=("Courier", 14, "bold"))
        printer.back(170)
        together_time = cal_time(t.strftime("%Y-%m-%d"), "2021-01-03") + 1
        printer.write("\n在一起" + str(together_time) + "天啦...", align="center", font=("Courier", 14, "bold"))

        printer.home()
        turtle.tracer(True)
        turtle.ontimer(tick, 100)  # 100ms后继续调用tick
    except Exception:
        pass


def clock_main():
    try:
        turtle.tracer(False)
        init()
        setup_clock(160)
        turtle.tracer(True)
        tick()
        turtle.mainloop()
    except Exception:
        pass