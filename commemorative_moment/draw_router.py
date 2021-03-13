from utils.valid_util import module_select
from commemorative_moment.draw_heart import draw_heart
from commemorative_moment.draw_rose import draw_rose
from commemorative_moment.draw_clock import clock_main
from whisper.confession import first_show

def draw_return_button():
    print("任意键返回\n", end="")
    """
invalid command name "1490004663688tick"
    while executing
"1490004663688tick"
    ("after" script)
    """
    input("Please input: ")
    draw_router()


def draw_router():
    draw_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Heart for you\t\t\t\t\t   |\n" + \
        "| <2> Rose for you\t\t\t\t\t   |\n" + \
        "| <3> Together for time\t\t\t\t\t   |\n" + \
        "| <4> All in one\t\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(draw_select_parse)
    select_num = module_select(select_num, draw_select_parse, 0, 4)

    # 分支一：
    if int(select_num) == 1:
        try:
            draw_heart()
        except Exception as e:
            draw_heart()
        draw_return_button()

    elif int(select_num) == 2:
        try:
            draw_rose()
        except Exception as e:
            draw_rose()
        draw_return_button()

    elif int(select_num) == 3:
        try:
            clock_main()
        except Exception as e:
            try:
                clock_main()
            except Exception as e:
                clock_main()
        draw_return_button()

    elif int(select_num) == 4:
        try:
            # 【图片】欢迎语
            try:
                draw_heart()
            except Exception as e:
                try:
                    draw_heart()
                except Exception as e:
                    draw_heart()
            print(":) According to the command line prompt operation will have surprise Oh... ")
            input(":) Please press Enter : ")
            # 【图片】画玫瑰
            try:
                draw_rose()
            except Exception as e:
                draw_rose()
            # 【文字】表白
            print(":) A rose for you. ", end="")
            input("Continue to Enter : ")
            first_show()
            input(":) Please press Enter : ")
            # 【图片】在一起的时间
            try:
                clock_main()
            except Exception as e:
                try:
                    clock_main()
                except Exception as e:
                    clock_main()
        except Exception as e:
            print(e)
            pass
        draw_return_button()

    else:
        from best_wishes import select_route
        select_route()


if __name__ == '__main__':
    draw_router()
