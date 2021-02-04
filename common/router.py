from common.period import *
from utils.valid_util import *
from best_wishes import select_route


def function_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    function_router()


def function_router():
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Calculate period\t\t\t\t\t   |\n" + \
        "| <2> Show history period\t\t\t\t   |\n" + \
        "| <3> Query Whether\t\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, 3)

    # 分支一：计算姨妈周期
    if int(select_num) == 1:
        event_period()
        function_return_button()

    # 分支二：显示历史姨妈周期
    elif int(select_num) == 2:
        show_history()
        function_return_button()

    # 分支二：查询天气
    elif int(select_num) == 3:
        from common.whether import query_whether
        query_whether()
        function_return_button()

    else:
        select_route()
