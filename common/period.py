from common.constant import *
from utils.valid_util import *


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

    record_file = "record.txt"
    try:
        f = open(record_file, "r")
        f.close()
    except Exception:
        f = open(record_file, "w")
        f.close()

    with open(record_file, "r+") as f:
        line = f.readline()
        if line == "":
            file_before_time = BEFORE_TIME
            file_default_duration = DEFAULT_DURATION
        else:
            file_before_time = line.split(",")[0]
            file_default_duration = line.split(",")[1]

        before_time = input("Before time is %s (allow modify: YYYY-MM-dd) : " % file_before_time)
        while not is_valid_date(before_time) and before_time != "":
            print(":( date format ERROR!!!")
            before_time = input("Before time is %s (allow modify: YYYY-MM-dd) : " % file_before_time)

        duration = input("Default duration is %s (allow modify: N) : " % str(file_default_duration))
        while not is_valid_number(duration) and duration != "":
            print(":( number format ERROR!!!")
            duration = input("Default duration is %s (allow modify: N) : " % str(file_default_duration))

        if before_time == "":
            before_time = file_before_time

        if duration == "":
            duration = file_default_duration

    with open(record_file, "w+") as f:
        f.write(str(before_time) + "," + str(duration))

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
