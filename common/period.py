from common.constant import *
from utils.valid_util import *


record_file = "period_record.txt"
history_file = "period_history.txt"


def event_period():
    """
    计算大姨妈
    :param before_time:
    :param duration:
    :return:
    """
    print()
    print("*" * 60)
    print(":)          Only for you. (your period)         ")
    print()

    try:
        f = open(record_file, "r")
        f.close()
    except Exception:
        f = open(record_file, "w")
        f.close()

    try:
        f = open(history_file, "r")
        f.close()
    except Exception:
        f = open(history_file, "w")
        f.close()


    with open(record_file, "r+") as f:
        line = f.readline()
        if line == "":
            file_before_time = BEFORE_TIME
            file_default_period = DEFAULT_PERIOD
        else:
            file_before_time = line.split(",")[0]
            file_default_period = line.split(",")[1]

        before_time = input("Before time is %s (allow modify: YYYY-MM-dd) : " % file_before_time)
        while not is_valid_date(before_time) and before_time != "":
            print(":( date format ERROR!!!")
            before_time = input("Before time is %s (allow modify: YYYY-MM-dd) : " % file_before_time)

        duration = input("Default period is %s (allow modify: N) : " % str(file_default_period))
        while not is_valid_number(duration) and duration != "":
            print(":( number format ERROR!!!")
            duration = input("Default period is %s (allow modify: N) : " % str(file_default_period))

        if before_time == "":
            before_time = file_before_time

        if duration == "":
            duration = file_default_period

    with open(record_file, "w+") as f:
        f.write(str(before_time) + "," + str(duration))

    is_save = input("Save as history? [y/n] (default n) : ")
    if is_save.lower() == "y":
        with open(history_file, "a+") as f:
            f.write(str(before_time) + "," + str(duration) + "\n")
            f.flush()

    y = int(before_time.split('-')[0])
    m = int(before_time.split('-')[1])
    d = int(before_time.split('-')[2])

    the_date = datetime.datetime(y, m, d)
    result_date = the_date + datetime.timedelta(days=int(duration))
    cal_day = result_date.strftime('%Y-%m-%d')
    left_days = cal_time(cal_day, time.strftime("%Y-%m-%d", time.localtime()))

    print()
    print(":)          Next time is %s, %s days left.         " % (cal_day, left_days))

    print("*" * 60)


def show_history():
    print()
    # print("+" + "-" * 58 + "+")
    print("+" + "-" * 28 + "+" + "-" * 29 + "+")
    # 11 + 6
    print("|" + " " * 9 + "PERIOD DATE" + " " * 8 + "|" +" " * 12 + "PERIOD" + " " * 11 + "|")
    print("+" + "-" * 28 + "+" + "-" * 29 + "+")
    with open(history_file, "r") as f:
        for line in f:
            if line.strip() != "":
                fields = line.split(",")
                print("|" + " " * 9 + fields[0] + " " * 9 + "|" + " " * 14 + fields[1].strip() + " " * 13 + "|")

    print("+" + "-" * 28 + "+" + "-" * 29 + "+")

