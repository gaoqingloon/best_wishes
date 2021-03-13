import os
import time
import datetime

history_dir = "resources/run_record/history"
history_dir = os.path.abspath(history_dir).replace("running\\", "").replace("\\", "/")


def show_together_time():
    """
    gql_2021-01-31 07#40#36+00#00_2021-01-31 08#41#43+00#00_上海市跑步
    lsp_2021-01-31 07#40#03+00#00_2021-01-31 08#30#35+00#00_抚顺市跑步

    gql_2021-01-04 01#55#40+00#00_2021-01-04 02#47#34+00#00_杭州市运动场跑步
    lsp_2021-01-04 01#55#42+00#00_2021-01-04 02#46#34+00#00_杭州市运动场跑步

    2021-01-04 01:01:00 2021-01-04 01:05:00
    2021-01-04 01:08:00 2021-01-04 01:20:00
    :return:
    """
    # 1. 每个人放到一个列表内[(起始时间,结束时间),(起始时间,结束时间)...]
    # 2. 遍历一个列表，看另一个列表是否有相同的日期
    # 3. 两个起始时间取最大，结束时间取最小，求时间差
    list_lsp = []
    list_gql = []
    for file in absolute_file_paths(history_dir):
        fields = file.split("\\")[-1].split("_")
        start_time = fields[1].split("+")[0].replace("#", ":")
        end_time = fields[2].split("+")[0].replace("#", ":")
        if "lsp" in file:
            list_lsp.append((start_time, end_time))
        else:
            list_gql.append((start_time, end_time))

    list_common = []
    for lsp_item in list_lsp:
        for gql_item in list_gql:
            if lsp_item[0][:10] == gql_item[0][:10]:
                list_common.append((lsp_item, gql_item))

    # print(list_common)

    record_time_res = []
    for item in list_common:
        start_date_1 = item[0][0]
        start_date_2 = item[1][0]
        end_date_1 = item[0][1]
        end_date_2 = item[1][1]
        if start_date_1 < start_date_2:
            max_start_date = start_date_2
        else:
            max_start_date = start_date_1

        if end_date_1 < end_date_2:
            min_end_date = end_date_1
        else:
            min_end_date = end_date_2

        if max_start_date >= min_end_date:
            continue

        # start_time
        print("|" + " " * 2 + max_start_date + " " * 37 + "|")
        days, hours, minutes, seconds = cal_detail_time(min_end_date, max_start_date)
        record_time_res.append((days, hours, minutes, seconds))

        days_ = str(days)
        hours_ = str(hours)
        minutes_ = str(minutes)
        seconds_ = str(seconds)
        if len(str(days)) != 2:
            days_ = " " + str(days)
        if len(str(hours)) != 2:
            hours_ = " " + str(hours)
        if len(str(minutes)) != 2:
            minutes_ = " " + str(minutes)
        if len(str(seconds)) != 2:
            seconds_ = " " + str(seconds)

        print("|" + " " * 27 + days_ + " " * 4 + hours_ + " " * 6 + minutes_ + " " * 7 + seconds_ + " " * 6 + "|")
        print("|" + " " * 2 + min_end_date + " " * 37 + "|")

        print("|" + " " * 58 + "|")
        print("|" + " " * 58 + "|")

    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    for record in record_time_res:
        days += record[0]
        hours += record[1]
        minutes += record[2]
        seconds += record[3]

    if seconds > 60:
        minutes_tmp = seconds // 60
        seconds = seconds - minutes_tmp * 60
        minutes += minutes_tmp

    if minutes > 60:
        hours_tmp = minutes // 60
        minutes = minutes - hours_tmp * 60
        hours += hours_tmp

    if hours > 60:
        days_tmp = hours // 24
        hours = hours - days_tmp * 24
        days += days_tmp

    days_ = str(days)
    hours_ = str(hours)
    minutes_ = str(minutes)
    seconds_ = str(seconds)
    if len(str(days)) != 2:
        days_ = " " + str(days)
    if len(str(hours)) != 2:
        hours_ = " " + str(hours)
    if len(str(minutes)) != 2:
        minutes_ = " " + str(minutes)
    if len(str(seconds)) != 2:
        seconds_ = " " + str(seconds)

    return "Our running time together :" + days_ + " " * 4 + hours_ + " " * 6 + minutes_ + " " * 7 + seconds_ + " " * 6


def cal_detail_time(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
    date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])

    seconds = (date1 - date2).days * 24 * 3600 + (date1 - date2).seconds  # seconds

    days = seconds // (24 * 60 * 60)
    hours = (seconds - days * 24 * 60 * 60) // 3600
    minutes = (seconds - days * 24 * 60 * 60 - hours * 3600) // 60
    seconds = seconds - days * 24 * 60 * 60 - hours * 3600 - minutes * 60
    return days, hours, minutes, seconds


def absolute_file_paths(directory):
    """
    某目录下所有文件的绝对路径
    :param directory:
    :return:
    """
    for root, _, files in os.walk(directory):
        for f in files:
            yield os.path.abspath(os.path.join(root, f))


if __name__ == '__main__':
    show_together_time()
