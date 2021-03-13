from utils.valid_util import module_select

def todo_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    todo_router()


def todo_router():

    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Our plan\t\t\t\t\t\t   |\n" + \
        "| <2> Secret\t\t\t\t\t\t   |\n" + \
        "| <3> First time for us\t\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)

    if select_num != "0829" and select_num != "papapa":
        select_num = module_select(select_num, function_select_parse, 0, 3)

    if select_num == "papapa":
        from to_do_list.papapa import our_papapa
        our_papapa()
        todo_return_button()

    elif select_num == "0829":
        from to_do_list.todo_list import first_time
        first_time()
        todo_return_button()

    elif int(select_num) == 1:
        from to_do_list.todo_list import todo_list
        todo_list()
        todo_return_button()

    elif int(select_num) == 2:
        print(":) 嘿嘿，暗号不对哦~\n")
        todo_return_button()

    elif int(select_num) == 3:
        print(":) qinglong.gao record, secret...\n")
        todo_return_button()

    else:
        from best_wishes import select_route
        select_route()

if __name__ == '__main__':
    todo_router()
