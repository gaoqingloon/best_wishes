from common.period import *
from utils.valid_util import *
from best_wishes import select_route


def function_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    common_router()


def common_router():
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Calculate period\t\t\t\t\t   |\n" + \
        "| <2> Insert record\t\t\t\t\t   |\n" + \
        "| <3> Show history period\t\t\t\t   |\n" + \
        "| <4> Query Whether\t\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, 4)

    # 分支一：计算姨妈周期
    if int(select_num) == 1:
        event_period()
        function_return_button()

    # 姨妈来了
    elif int(select_num) == 2:
        insert_current()
        function_return_button()

    # 分支二：显示历史姨妈周期
    elif int(select_num) == 3:
        show_history()
        function_return_button()

    # 分支二：查询天气
    elif int(select_num) == 4:
        from common.whether import query_whether
        try:
            query_whether()
        except Exception as e:
            print(":( 天气查询接口不可用,请联系管理员.")
        function_return_button()

    else:
        select_route()
