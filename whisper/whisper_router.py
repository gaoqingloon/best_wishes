from utils.valid_util import module_select

def whisper_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    whisper_router()


def whisper_router():
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Confession\t\t\t\t\t   |\n" + \
        "| <2> Attitude towards you\t\t\t\t   |\n" + \
        "| <3> Our Valentine's Day\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)

    if select_num != "0829":
        select_num = module_select(select_num, function_select_parse, 0, 3)


    if select_num == "0829":
        from to_do_list.todo_list import first_time
        first_time()
        whisper_return_button()

    elif int(select_num) == 1:
        from whisper.confession import confession
        confession()
        whisper_return_button()

    elif int(select_num) == 2:
        from whisper.confession import first_show
        first_show()
        whisper_return_button()

    elif int(select_num) == 3:
        from whisper.valentine_s_day import day_2021_0214
        day_2021_0214()
        whisper_return_button()

    else:
        from best_wishes import select_route
        select_route()


if __name__ == '__main__':
    whisper_router()