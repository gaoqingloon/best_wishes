import os
import time

history_dir = "resources/run_record/history"
history_dir = os.path.abspath(history_dir).replace("running\\", "").replace("\\", "/")
files_list = []


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


# def show_hero_score():
#     files_list.clear()
#     get_absolute_file_paths(history_dir)
#     print()
#     print("+" + "-" * 85 + "+")
#     index = 1
#     track_show_dict = {}
#     print("| " + " " * 5 + "NAME" +  " "* 5 + "PLACE" + " " * 14 + "START TIME"  + " " * 11 + "END TIME" + " " * 13 + "DISTANCE" + " " * 1 + "|")
#     print("+" + "-" * 85 + "+")
#
#     # 按跑步开始时间排序
#     sorted_files_list = []
#     for i in range(len(files_list)):
#         sorted_files_list.append((files_list[i].split("\\")[-1].split("_")[1], files_list[i]))
#     sorted_files_list.sort()
#
#     for path in sorted_files_list:
#         path = path[1]
#         file_name = os.path.basename(path)
#         if file_name.startswith("gql"):
#             your_name = "高庆龙"
#         else:
#             your_name = "刘姝鹏"
#         # gql_2021-01-31 07#40#36+00#00_2021-01-31 08#41#43+00#00_上海市跑步
#         fields = file_name.split("_")
#         start_time = fields[1]  # 2021-01-31 07#40#36+00#00
#         end_time = fields[2]
#         running_name = fields[3]
#         if len(fields) == 5:
#             run_distance = fields[4]
#         else:
#             run_distance = ""
#         start_time = start_time.split("+")[0].replace("#", ":")
#         end_time = end_time.split("+")[0].replace("#", ":")
#         if len(str(index)) == 1:
#             index_ = "0" + str(index)
#         else:
#             index_ = str(index)
#
#         space_count = 3
#         running_part = str(running_name) + " " * space_count
#         if len(running_part) < 9:
#             space_count = 9 - len(running_part)
#             running_part = running_part + " " * space_count * 6
#
#         if len(run_distance) == 1:
#             run_distance = "0" + run_distance + ".00"
#         else:
#             zhengshu = run_distance.split(".")[0]
#             if len(zhengshu) == 1:
#                 run_distance = "0" + zhengshu + "."+ run_distance.split(".")[1]
#
#         print("| " + "<" + index_ + "> " + your_name + " " * 3 + running_part +
#               str(start_time) + " " * 2 + str(end_time) + " " * 3 + run_distance + " " * 3 + "|")
#
#         track_show_dict[index] = path
#         index += 1
#     print("+" + "-" * 85 + "+")
#     return track_show_dict


def show_hero_score():
    files_list.clear()
    get_absolute_file_paths(history_dir)
    print()
    print("+" + "-" * 25 + "+")
    index = 1
    track_show_dict = {}
    print("| " + " " * 6 + "NAME" + " " * 5 + "DISTANCE" + " " * 1 + "|")
    print("+" + "-" * 25 + "+")

    # 按跑步开始时间排序
    sorted_files_list = []
    for i in range(len(files_list)):
        sorted_files_list.append((files_list[i].split("\\")[-1].split("_")[1], files_list[i]))
    sorted_files_list.sort()

    for path in sorted_files_list:
        path = path[1]
        file_name = os.path.basename(path)
        if file_name.startswith("gql"):
            your_name = "高庆龙"
        else:
            your_name = "刘姝鹏"
        # gql_2021-01-31 07#40#36+00#00_2021-01-31 08#41#43+00#00_上海市跑步
        fields = file_name.split("_")
        start_time = fields[1]  # 2021-01-31 07#40#36+00#00
        end_time = fields[2]
        running_name = fields[3]
        if len(fields) == 5:
            run_distance = fields[4]
        else:
            run_distance = ""
        start_time = start_time.split("+")[0].replace("#", ":")
        end_time = end_time.split("+")[0].replace("#", ":")
        if len(str(index)) == 1:
            index_ = "0" + str(index)
        else:
            index_ = str(index)

        space_count = 3
        running_part = str(running_name) + " " * space_count
        if len(running_part) < 9:
            space_count = 9 - len(running_part)
            running_part = running_part + " " * space_count * 6

        if len(run_distance) == 1:
            run_distance = "0" + run_distance + ".00"
        else:
            zhengshu = run_distance.split(".")[0]
            if len(zhengshu) == 1:
                run_distance = "0" + zhengshu + "." + run_distance.split(".")[1]

        print("| " + "<" + index_ + "> " + your_name + " " * 5 + run_distance + " " * 3 + "|")

        path = "\n" + "+" + "-" * 85 + "+\n" + "| " + " " * 5 + "NAME" + \
               " " * 5 + "PLACE" + " " * 14 + "START TIME" + " " * 11 + "END TIME" + " " * 13 + \
               "DISTANCE" + " " * 1 + "|\n" + "+" + "-" * 85 + "+" + "\n" + "| " + "<" + index_ + "> " + \
               your_name + " " * 3 + running_part + str(start_time) + " " * 2 + str(end_time) + " " * 3 + \
               run_distance + " " * 3 + "|\n" + "+" + "-" * 85 + "+" + "\n"

        track_show_dict[index] = path
        index += 1
    print("+" + "-" * 25 + "+")
    return track_show_dict


if __name__ == '__main__':
    # show_hero_score()
    string = ["b_14", "a_13"]
    li = []
    for i in range(len(string)):
        li.append((string[i].split("_")[1], string[i]))
    li.sort()
    print(li)
    for line in li:
        line = line[1]
        print(line)
    # import datetime
    # import time
    #
    # # time_utc = datetime.datetime.utcnow()
    # # print(type(time_utc))
    # # time_now = (time_utc + datetime.timedelta(hours=8))
    # # print(time_utc)
    # # print(time_now)
    # utc_time = "2021-02-06 03:07:20"
    # utc_time = time.strptime(utc_time, "%Y-%m-%d %H:%M:%S")
    # utc_float_time = time.mktime(utc_time)
    # beijing_float_time = utc_float_time + 8 * 60 * 60
    # new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(beijing_float_time))
    # print(new_time)
