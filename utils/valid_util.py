import time
import datetime


def is_valid_number(number):
    """
    判断是否是一个有效数字
    :param number:
    :return:
    """
    try:
        convert_num = int(number)
        return isinstance(convert_num, int)
    except Exception:
        return False


def is_range(number, min_num, max_num):
    """
    范围判断
    :param number:
    :param min_num:
    :param max_num:
    :return:
    """
    if min_num <= int(number) <= max_num:
        return True
    else:
        return False


def is_valid_date(date_str):
    """
    判断是否是一个有效的日期字符串
    :param date_str:
    :return:
    """
    try:
        time.strptime(date_str, "%Y-%m-%d")
        return True
    except Exception:
        return False


def is_valid_date_dot(date_str):
    """
    判断是否是一个有效的日期字符串
    :param date_str:
    :return:
    """
    try:
        time.strptime(date_str, "%Y.%m.%d")
        return True
    except Exception:
        return False


def double_valid(select, range_min, range_max):
    if not is_valid_number(select):
        print(":( Please input number!")
        return False
    else:
        if not is_range(select, range_min, range_max):
            print(":( Input range Error!")
            return False
        else:
            return True


def module_select(select_num, select_parse, range_min, range_max):
    is_success = False
    while not is_success:
        is_success = double_valid(select_num, range_min, range_max)
        if not is_success:
            select_num = input(select_parse)
        else:
            is_success = True
    return select_num


def cal_time(date1, date2):
    """
    计算两个日期相差天数
    :param date1:
    :param date2:
    :return:
    """
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    # 返回两个变量相差的值，就是相差天数
    return (date1 - date2).days


def cal_detail_time(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
    date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
    # 返回两个变量相差的值，就是相差天数
    seconds = (date1 - date2).days * 24 * 3600 + (date1 - date2).seconds  # seconds
    hours = (date1 - date2).days * 24 + (date1 - date2).seconds // 3600  # hours
    days = (date1 - date2).days
    return days, hours, seconds


def cal_all_detail_time(date1, date2):
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


def get_last_month():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    return int(last_month.strftime("%Y")), int(last_month.strftime("%m"))
    # return last_month.strftime("%Y") + "年" + last_month.strftime("%m") + "月"

def get_current_month():
    month = str(datetime.datetime.now().month)
    if len(month) == 1:
        month = "0" + month

    return datetime.datetime.now().year, month


def get_month_range(start_day, end_day):
    months = (end_day.year - start_day.year) * 12 + end_day.month - start_day.month

    # month_range = ['%s年%s月' % (start_day.year + mon // 12, mon % 12 + 1)
    #                for mon in range(start_day.month - 1, start_day.month + months)]

    month_range = []
    for mon in range(start_day.month - 1, start_day.month + months):
        month = str(mon % 12 + 1)
        if len(month) == 1:
            month = "0" + month
        month_range.append(str(start_day.year + mon // 12) + "年" + month + "月")

    return month_range


if __name__ == '__main__':
    # print(cal_time("2021-02-23", "2021-01-17"))
    print(get_last_month())
    print(get_month_range(datetime.date(2021, 1, 1), datetime.date(2021, 2, 26)))
    print(get_current_month())
