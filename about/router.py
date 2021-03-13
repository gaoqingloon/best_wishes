from utils.valid_util import module_select
from about.about_software import *
from about.update_log import *

def about_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    about_router()


def about_router():
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> About BEST_WISHES software\t\t\t   |\n" + \
        "| <2> Show update log\t\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, 2)

    # 分支一：
    if int(select_num) == 1:
        show_software()
        about_return_button()

    # 分支二：
    elif int(select_num) == 2:
        from VERSION import SOFTWARE_VERSION
        print()
        print("+" + "-" * 58 + "+")
        print("|" + " " * 58 + "|")
        print("|" + " " * 20 + "BEST_WISHES " + SOFTWARE_VERSION + " " * 21 + "|")
        print("|" + " " * 58 + "|", end="")
        show_1_1_0()
        show_1_2_0()
        show_2_0_0()
        show_2_0_1()
        show_2_1_0()
        show_2_1_1()
        show_2_2_0()
        show_2_2_1()
        show_2_2_2()
        show_2_3_0()
        show_2_3_1()
        show_2_3_2()
        show_2_3_3()
        show_2_3_4()
        show_2_4_0()
        show_2_4_1()
        show_2_4_2()
        print("+" + "-" * 58 + "+")
        about_return_button()

    else:
        from best_wishes import select_route
        select_route()


if __name__ == '__main__':
    about_router()
