# -*- coding:utf-8 -*-
from turtle import *
from datetime import *
import turtle
import time


def skip(step):
    penup()
    forward(step)
    pendown()


def mk_hand(name, length):
    # 注册Turtle形状，建立表针Turtle
    reset()
    skip(-length * 0.1)
    begin_poly()
    forward(length * 1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)


def init():
    global secHand, minHand, hurHand, printer
    mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mk_hand("secHand", 125)
    mk_hand("minHand", 130)
    mk_hand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()


def setup_clock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            forward(20)
            skip(-radius - 20)
        else:
            dot(5)
            skip(-radius)
        right(6)


def Week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)


# 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
def cal_time(date1, date2):
    # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
    # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1 = datetime(date1[0], date1[1], date1[2])
    date2 = datetime(date2[0], date2[1], date2[2])
    # 返回两个变量相差的值，就是相差天数
    return (date1 - date2).days


def tick():
    try:
        # 绘制表针的动态显示
        t = datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        secHand.setheading(6 * second)
        minHand.setheading(6 * minute)
        hurHand.setheading(30 * hour)

        tracer(False)
        printer.forward(65)
        printer.write(Week(t), align="center", font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(Date(t), align="center", font=("Courier", 14, "bold"))
        printer.back(170)
        together_time = cal_time(t.strftime("%Y-%m-%d"), "2021-01-03")
        printer.write("\n在一起" + str(together_time) + "天啦...", align="center", font=("Courier", 14, "bold"))

        printer.home()
        tracer(True)
        ontimer(tick, 100)  # 100ms后继续调用tick
    except Exception:
        pass


def clock_main():
    tracer(False)
    init()
    setup_clock(160)
    tracer(True)
    tick()
    mainloop()


def draw():
    # 设置初始位置
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    # 花蕊
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # 花瓣1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # 花瓣2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # 叶子1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()

    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    # 叶子2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()

    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)


def input_():
    print()
    print("[ 哈哈，送你一朵玫瑰花... ]")
    say = input("[ 图片不要关闭哦，继续回车吧... ]")
    print()
    print("\n\t\t+", end="")
    print("-" * 40, end="+")
    print("\n\t\t|\t\t\t\t\t |", end="")
    print("\n\t\t|\t     *^_^*     *^_^*\t\t |\n\t\t|\t\t\t\t\t |\n\t\t|\t\t\t\t\t |\n\t\t|     我的世界从此以后多了一个你\t |\n\t\t|\t\t\t\t\t |\n\t\t|     有时天晴有时雨\t\t\t |\n\t\t|\t\t\t\t\t |\n\t\t|     阴天时候我会告诉你\t\t |\n\t\t|\t\t\t\t\t |\n\t\t|     我爱你，胜过彩虹的美丽！！\t |\n\t\t|\t\t\t\t\t |\n\t\t|\t\t\t\t\t |\n\t\t|     -*- 姝鹏·我的彩虹女孩 !!! -*-     |")
    print("\t\t|\t\t\t\t\t |")
    print("\t\t|\t\t\t\t -庆龙-  |")
    print("\t\t+" + "-" * 40, end="+")
    print("\n")

    print("\n\t\t\t * Jan 03 11:18 CST 2021 *\n\n")
    say = input("[ 回车后图片关掉吧，拜拜~... ]")


def tree(plist, l, a, f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level. """
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)  # 沿着当前的方向画画Move the turtle forward by the specified distance, in the direction the turtle is headed.
            q = p.clone()  # Create and return a clone of the turtle with same position, heading and turtle properties.
            p.left(a)  # urn turtle left by angle units
            q.right(a)  # turn turtle right by angle units, nits are by default degrees, but can be set via the degrees() and radians() functions.
            lst.append(p)  # 将元素增加到列表的最后
            lst.append(q)
        tree(lst, l * f, a, f)


def treemain():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    # p.setundobuffer(None)
    p.hideturtle()  # Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing,
    # because hiding the turtle speeds up the drawing observably.
    # p.speed(10)
    # p.getscreen().tracer(1,0)#Return the TurtleScreen object the turtle is drawing on.
    p.speed(15)
    # TurtleScreen methods can then be called for that object.
    p.left(90)  # Turn turtle left by angle units. direction 调整画笔
    p.penup()  # Pull the pen up – no drawing when moving.
    p.goto(0, -200)  # Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
    p.pendown()  # Pull the pen down – drawing when moving. 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    # 否则turtle一移动就会自动的把线画出来
    # t = tree([p], 200, 65, 0.6375)
    tree([p], 200, 65, 0.6375)


if __name__ == "__main__":
    try:
        say = input("[ 按命令行提示操作会有惊喜哦^_^... ]\n\n[ 按回车键有惊喜哦... ]")
        draw()
        # treemain()
        input_()

        try:
            clock_main()
        except Exception:
            pass

        # say = input("[ Enter... ]")
        print("[ 关掉黑窗口吧... ]")
        time.sleep(30)
    except Exception:
        pass

"""
pip install mkl-service -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""