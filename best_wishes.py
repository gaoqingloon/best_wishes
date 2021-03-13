# -*- coding:utf-8 -*-
import sys

from VERSION import *
from commemorative_moment.draw_heart import *

SELECT_PARSE = "+" + "-" * 58 + "+\n" \
               "| <1> Common Tools\t\t\t\t\t   |\n" \
               "| <2> A little Surprise\t\t\t\t\t   |\n" \
               "| <3> Marathon\t\t\t\t\t\t   |\n" \
               "| <4> Running\t\t\t\t\t\t   |\n" \
               "| <5> To do list\t\t\t\t\t   |\n" \
               "| <6> Valentine's Day\t\t\t\t\t   |\n" \
               "| <7> About\t\t\t\t\t\t   |\n" \
               "| <0> Exit\t\t\t\t\t\t   |\n" \
               "+" + "-" * 58 + "+\n" \
               "Please select : "


def select_route():
    """
    分支
    :return:
    """
    print()
    print("Please select module: ")
    select_num = input(SELECT_PARSE)
    select_num = module_select(select_num, SELECT_PARSE, 0, 10)

    # 分支一：姨妈周期
    if int(select_num) == 1:
        from common.router import common_router
        common_router()

    # 分支二：图片惊喜
    elif int(select_num) == 2:
        from commemorative_moment.draw_router import draw_router
        draw_router()

    # 分支三：马拉松
    elif int(select_num) == 3:
        from marathon.marathon import marathon_show
        marathon_show()

    # running
    elif int(select_num) == 4:
        from running.running_router import running_router
        try:
            running_router()
        except Exception as e:
            print(e)

    # to do list
    elif int(select_num) == 5:
        from to_do_list.todo_router import todo_router
        todo_router()

    # whisper
    elif int(select_num) == 6:
        from whisper.whisper_router import whisper_router
        whisper_router()

    # about
    elif int(select_num) == 7:
        from about.router import about_router
        about_router()

    else:
        sys.exit(0)


def main():
    # 【文字】欢迎语
    welcome()
    # 【文字】在一起的时间
    together_time()

    while True:
        try:
            # 选择模块
            select_route()
        except Exception:
            pass


if __name__ == "__main__":
    main()


"""
pip install matplotlib -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install paramiko -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""
