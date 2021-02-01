# -*- coding:utf-8 -*-
import sys
from common.period import *
from commemorative_moment.draw_heart import *
from commemorative_moment.draw_rose import *
from commemorative_moment.draw_clock import *
from commemorative_moment.first_show import *
from marathon.marathon import *
from VERSION import *


SELECT_PARSE = "+" + "-" * 58 + "+\n" \
               "| <1> Common Tools\t\t\t\t\t   |\n" \
               "| <2> Commemorative Moment\t\t\t\t   |\n" \
               "| <3> Marathon\t\t\t\t\t\t   |\n" \
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
    select_num = module_select(select_num, SELECT_PARSE, 0, 3)

    # 分支一：姨妈周期
    if int(select_num) == 1:
        event_period()

    # 分支二：图片惊喜
    elif int(select_num) == 2:
        try:
            # 【图片】欢迎语
            draw_heart()
            input("[ 按命令行提示操作会有惊喜哦^_^... ]\n\n[ 按回车键有惊喜哦... ]")
            # 【图片】画玫瑰
            draw_rose()
            # 【文字】表白
            first_show()
            # 【图片】在一起的时间
            clock_main()
        except Exception:
            pass

    # 分支三：马拉松
    elif int(select_num) == 3:
        marathon_show()

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
pip install numpy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""
