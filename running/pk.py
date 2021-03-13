from utils.valid_util import module_select, get_last_month ,get_month_range, get_current_month
import os
import datetime

history_dir = "resources/run_record/history"
history_dir = os.path.abspath(history_dir).replace("running\\", "").replace("\\", "/")
files_list = []


def pk_month_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    show_month()


def pk_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    pk()



def pk():
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> History\t\t\t\t\t\t   |\n" + \
        "| <2> 月实时跑量(漫漫追妻路)\t\t\t\t   |\n" + \
        "| <3> 年实时跑量(漫漫追妻路)\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, 3)

    if int(select_num) == 1:
        show_month()
    elif int(select_num) == 2:
        show_current_running()
    elif int(select_num) == 3:
        show_current_year_running()
    else:
        from running.running_router import running_router
        running_router()

    pk_return_button()



def show_current_year_running():

    print()
    print("+" + "-" * 85 + "+")
    print("| " + " " * 5 + "年份" + " " *9 + "刘姝鹏" + " " * 7 + "高庆龙" + " " * 8 + "|" + " " * 16 + "PK结果" + " " * 16 + "|")
    print("+" + "-" * 85 + "+")

    last_year, last_month = get_last_month()
    date_str_list = get_month_range(datetime.date(2021, 1, 1), datetime.date(last_year, last_month, 1))

    year, month = get_current_month()
    month_key = str(year) + "年" + str(month) + "月"

    gql_dict, lsp_dict = gen_hero_agg_score()

    date_str_list.append(month_key)

    lsp_total_year = 0
    gql_total_year = 0
    for per_date_str in date_str_list:
        if str(per_date_str).startswith(str(year) + "年"):
            lsp_total_year += get_distance_by_month(lsp_dict, per_date_str)
            gql_total_year += get_distance_by_month(gql_dict, per_date_str)

    if float(lsp_total_year) > float(gql_total_year):
        v_info = "媳妇胜,老公要加油哦~ (" + str(round((float(lsp_total_year) - float(gql_total_year)),2)) + "公里)"
    elif float(lsp_total_year) > float(gql_total_year):
        v_info = "老公胜,媳妇要加油哦~ (" + str(round((float(gql_total_year) - float(lsp_total_year)),2)) + "公里)"
    else:
        v_info = "哎呦，打成平手啦，都要加油哦~"

    lsp_total_year_str = str(lsp_total_year)
    gql_total_year_str = str(gql_total_year)
    while len(lsp_total_year_str) != 6:
        lsp_total_year_str = " " + lsp_total_year_str
    while len(gql_total_year_str) != 6:
        gql_total_year_str = " " + gql_total_year_str


    print("|" + " " * 5 + (str(year) + "年") + " " * 8 + lsp_total_year_str +
          " " * 7 + gql_total_year_str + " " * 8 + "|" + " " * 3 + v_info + " " * 3 + "|")

    print("+" + "-" * 85 + "+")



def show_current_running():

    print()
    print("+" + "-" * 85 + "+")
    print("| " + " " * 5 + "月份" + " " *9 + "刘姝鹏" + " " * 7 + "高庆龙" + " " * 8 + "|" + " " * 16 + "PK结果" + " " * 16 + "|")
    print("+" + "-" * 85 + "+")

    year, month = get_current_month()
    month_key = str(year) + "年" + str(month) + "月"

    gql_dict, lsp_dict = gen_hero_agg_score()

    lsp_total_str = str(get_distance_by_month(lsp_dict, month_key))
    gql_total_str = str(get_distance_by_month(gql_dict, month_key))

    if len(lsp_total_str.split(".")[1]) == 1:
        lsp_total_str = lsp_total_str.split(".")[0] + "." + lsp_total_str.split(".")[1] + "0"
    if len(gql_total_str.split(".")[1]) == 1:
        gql_total_str = gql_total_str.split(".")[0] + "." + gql_total_str.split(".")[1] + "0"

    if float(lsp_total_str) > float(gql_total_str):
        v_info = "媳妇胜,老公要加油哦~ (" + str(round((float(lsp_total_str) - float(gql_total_str)),2)) + "公里)"
        while len(v_info) < 21:
            v_info += " "
    elif float(lsp_total_str) > float(gql_total_str):
        v_info = "老公胜,媳妇要加油哦~ (" + str(round((float(gql_total_str) - float(lsp_total_str)),2)) + "公里)"
        while len(v_info) < 21:
            v_info += " "
    else:
        v_info = "哎呦，打成平手啦，都要加油哦~"

    while len(lsp_total_str) != 6:
        lsp_total_str = " " + lsp_total_str
    while len(gql_total_str) != 6:
        gql_total_str = " " + gql_total_str


    print("|" + " " * 3 + month_key + " " * 6 + lsp_total_str +
          " " * 7 + gql_total_str + " " * 8 + "|" + " " * 3 + v_info + " " * 3 + "|")

    print("+" + "-" * 85 + "+")



def show_month():

    # 动态生成从2021.1到当前月上一个月的月份
    last_year, last_month = get_last_month()
    date_str_list = get_month_range(datetime.date(2021, 1, 1), datetime.date(last_year, last_month, 1))
    date_index_month_dict = {}
    for i in range(len(date_str_list)):
        date_index_month_dict[i+1] = date_str_list[i]

    date_str_flat = ""
    for i in range(len(date_str_list)):
        date_str_flat += "| <"+str(i+1)+"> "+date_str_list[i]+"\t\t\t\t\t   |\n"

    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        + date_str_flat + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "


    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, len(date_str_list))

    if 1 <= int(select_num) <= len(date_str_list):
        # 1 => 2021-1
        # 2 => 2021-2
        # 13 => 2022-1
        show_hero_agg_score(date_index_month_dict[int(select_num)])
    else:
        pk()

    pk_month_return_button()



def get_absolute_file_paths(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            get_absolute_file_paths(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        files_list.append(os.path.join(path, f))


def absolute_file_paths(directory):
    """
    某目录下所有文件的绝对路径
    :param directory:
    :return:
    """
    for root, _, files in os.walk(directory):
        for f in files:
            yield os.path.abspath(os.path.join(root, f))


def show_hero_agg_score(month_key):
    gql_dict, lsp_dict = gen_hero_agg_score()

    print()
    print("+" + "-" * 85 + "+")
    print("| " + " " * 5 + "月份" + " " *9 + "刘姝鹏" + " " * 7 + "高庆龙" + " " * 8 + "|" + " " * 16 + "PK结果" + " " * 16 + "|")
    print("+" + "-" * 85 + "+")

    lsp_total_str = str(get_distance_by_month(lsp_dict, month_key))
    gql_total_str = str(get_distance_by_month(gql_dict, month_key))

    if float(lsp_total_str) > float(gql_total_str):
        v_info = "媳妇胜,老公要加油哦~ (" + str(round((float(lsp_total_str) - float(gql_total_str)),2)) + "公里)"
        while len(v_info) < 21:
            v_info += " "
    elif float(lsp_total_str) > float(gql_total_str):
        v_info = "老公胜,媳妇要加油哦~ (" + str(round((float(gql_total_str) - float(lsp_total_str)),2)) + "公里)"
        while len(v_info) < 21:
            v_info += " "
    else:
        v_info = "哎呦，打成平手啦，都要加油哦~"

    while len(lsp_total_str) != 6:
        lsp_total_str = " " + lsp_total_str
    while len(gql_total_str) != 6:
        gql_total_str = " " + gql_total_str

    print("|" + " " * 3 + month_key + " " * 6 + lsp_total_str +
          " " * 7 + gql_total_str + " " * 8 + "|" + " " * 3 + v_info + " " * 3 + "|")
    # print("|" + " " * 3 + month_key + " " * 6 + lsp_total_str +
    #       " " * 6 + gql_total_str + " " * 5 + "|" + " " * 17 + v_info + " " * 17 + "|")

    print("+" + "-" * 85 + "+")


def gen_hero_agg_score():
    files_list.clear()
    get_absolute_file_paths(history_dir)

    gql_dict = {}
    lsp_dict = {}
    for path in files_list:
        file_name = os.path.basename(path)

        # gql_2021-01-31 07#40#36+00#00_2021-01-31 08#41#43+00#00_上海市跑步
        fields = file_name.split("_")
        start_time = fields[1]  # 2021-01-31 07#40#36+00#00
        running_name = fields[3]
        if len(fields) == 5:
            run_distance = fields[4]
        else:
            run_distance = ""
        start_time_key = "-".join(str(start_time).split("+")[0].replace("#", ":").split(" ")[0].split("-")[:2])
        start_time_value = float(run_distance)

        # print(start_time_key)

        if file_name.startswith("gql"):

            if gql_dict.__contains__(start_time_key):
                gql_dict[start_time_key].append(start_time_value)
            else:
                gql_value_list = [start_time_value]
                gql_dict[start_time_key] = gql_value_list

        else:
            if lsp_dict.__contains__(start_time_key):
                lsp_dict[start_time_key].append(start_time_value)
            else:
                lsp_value_list = [start_time_value]
                lsp_dict[start_time_key] = lsp_value_list

    return gql_dict, lsp_dict



def get_distance_by_month(your_dict, month):
    # print(your_dict)
    return round(sum(your_dict.get(month.replace("年","-").replace("月",""))), 2)
    # print(round(sum(your_dict.get("2021-02")), 2))
    # print(round(sum(your_dict.get("2021-03")), 2))

    # print(lsp_dict)
    # print(round(sum(lsp_dict.get("2021-01")), 2))
    # print(round(sum(lsp_dict.get("2021-02")), 2))
    # print(round(sum(lsp_dict.get("2021-03")), 2))



if __name__ == '__main__':
    pk()
