from common.constant import *
from utils.valid_util import *
import paramiko

# record_file = "period_record.txt"
# history_file = "period_history.txt"

# record_file = os.path.abspath("resources/period_record.txt").replace("common\\", "").replace("\\", "/")
# history_file = os.path.abspath("resources/period_history.txt").replace("common\\", "").replace("\\", "/")
history_file = str(os.getcwd()).replace("\\", "/") + '/resources/period_history.txt'


def event_period():
    """
    计算大姨妈
    :param before_time:
    :param duration:
    :return:
    """
    # print()
    # print("*" * 60)
    print()
    print("""
                                _                                    
                /             /  `                                   
----__----__---/------------_/__-----__---)__--------------__--------
  /   ) /   ) /   /   /     /      /   ) /   )     /   / /   ) /   / 
_(___/_/___/_/___(___/_____/______(___/_/_________(___/_(___/_(___(__
                    /                                /               
                (_ /                             (_ /                
    """)
    # print(":)" + " " * 25 + "ONLY FOR YOU")
    print(" " * 55 + "ONLY FOR YOU")
    print()

    try:
        f = open(history_file, "r")
        f.close()
    except Exception:
        f = open(history_file, "w")
        f.close()

    line = str(__get_last_line(history_file)).replace("\\r\\n'", "").replace("b'", "")

    if line == "":
        file_before_time = BEFORE_TIME
        file_default_period = DEFAULT_PERIOD
    else:
        file_before_time = line.split(",")[1].strip()
        file_default_period = cal_time(line.split(",")[1].strip(), line.split(",")[0].strip())

    before_time = input(":] BEFORE TIME IS %s (YYYY-MM-dd) : " % file_before_time)
    while not is_valid_date(before_time) and before_time != "":
        print(":( date format ERROR!!!")
        before_time = input(":] BEFORE TIME IS %s (YYYY-MM-dd) : " % file_before_time)

    duration = input(":] YOUR PERIOD IS %s (N) : " % str(file_default_period))
    while not is_valid_number(duration) and duration != "":
        print(":( number format ERROR!!!")
        duration = input(":] YOUR PERIOD IS %s (N) : " % str(file_default_period))

    if before_time == "":
        before_time = file_before_time

    if duration == "":
        duration = file_default_period

    # with open(record_file, "w+") as f:
    #     f.write(str(before_time) + "," + str(duration))

    # is_save = input("Save as history? [y/n] (default n) : ")
    # if is_save.lower() == "y":
    #     with open(history_file, "a+") as f:
    #         f.write(str(before_time) + "," + str(duration) + "\n")
    #         f.flush()

    y = int(before_time.split('-')[0])
    m = int(before_time.split('-')[1])
    d = int(before_time.split('-')[2])

    the_date = datetime.datetime(y, m, d)
    result_date = the_date + datetime.timedelta(days=int(duration))
    cal_day = result_date.strftime('%Y-%m-%d')
    left_days = cal_time(cal_day, time.strftime("%Y-%m-%d", time.localtime()))

    print()
    if int(left_days) <= 3:
        print(":) It is assumed that the next date is %s, [%s] days left. " % (cal_day, left_days))
    elif int(left_days) <= 7:
        print(":) It is assumed that the next date is %s, %s days left. " % (cal_day, left_days))
    else:
        print(":) It is assumed that the next date is %s, %s days left. " % (cal_day, left_days))

    print()
    # print("*" * 60)



def insert_current():
    print()
    try:
        f = open(history_file, "r")
        f.close()
    except Exception:
        f = open(history_file, "w")
        f.close()

    try:
        line = str(__get_last_line(history_file))
        with open(history_file, "a+") as f:

            current_date = input(":] Coming date (YYYY-MM-dd) : ")
            while (not is_valid_date(current_date)) or current_date == "":
                print(":( date format ERROR!!!")
                current_date = input(":] Coming date (YYYY-MM-dd) : ")

            is_save = input(":] Save? [y/n] (default n) : ")
            if is_save.lower() == "y":
                f.write(line.split(",")[1].replace("\\r\\n'", "") + "," + current_date + "\n")

                duration = cal_time(current_date, line.split(",")[1].replace("\\r\\n'", ""))
                print(":) Save success. Your current period is " + str(duration) + " days.")

    except Exception as e:
        print(e)



def upload():
    from sftp_client import host
    sftp = host.connect()

    remote_file = '/home/gql/running/resources/period_history.txt'
    local_file = str(os.getcwd()).replace("\\", "/") + '/resources/period_history.txt'

    sftp.put(local_file, remote_file)


def download():
    from sftp_client import host
    sftp = host.connect()

    remote_file = '/home/gql/running/resources/period_history.txt'
    local_file = str(os.getcwd()).replace("\\", "/") + '/resources/period_history.txt'

    sftp.get(remote_file, local_file)


def get_remote_file_size():
    from sftp_client import host
    sftp = host.connect()
    remote_file = '/home/gql/running/resources/period_history.txt'

    remote_file_size = sftp.stat(remote_file).st_size
    return remote_file_size


def __get_last_line(filename):
    """
    get last line of a file
    :param filename: file name
    :return: last line or None for empty file
    """
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, 'rb') as fp: # to use seek from end, must use mode 'rb'
                offset = -8                 # initialize offset
                while -offset < filesize:   # offset cannot exceed file size
                    fp.seek(offset, 2)      # read # offset chars from eof(represent by number '2')
                    lines = fp.readlines()  # read from fp to eof
                    if len(lines) >= 2:     # if contains at least 2 lines
                        return lines[-1]    # then last line is totally included
                    else:
                        offset *= 2         # enlarge offset
                fp.seek(0)
                lines = fp.readlines()
                return lines[-1]
    except FileNotFoundError:
        print(filename + ' not found!')
        return None


def show_history():
    try:
        local_file = str(os.getcwd()).replace("\\", "/") + '/resources/period_history.txt'

        if int(os.path.getsize(local_file)) > int(get_remote_file_size()):
            upload()
        else:
            download()
    except Exception as e:
        print(e)

    print()
    # print("+" + "-" * 58 + "+")
    print("+" + "-" * 28 + "+" + "-" * 29 + "+" + "-" * 29 + "+")
    # 11 + 6
    print("|" + " " * 9 + "Before date" + " " * 8 + "|" + " " * 9 + "Current date" + " " * 8 + "|" + " " * 12 + "Period" + " " * 11 + "|")
    print("+" + "-" * 28 + "+" + "-" * 29 + "+" + "-" * 29 + "+")
    with open(history_file, "r") as f:
        for line in f:
            if line.strip() != "":
                fields = line.split(",")
                duration = cal_time(line.split(",")[1].strip(), line.split(",")[0].strip())
                print("|" + " " * 9 + fields[0] + " " * 9 + "|" + " " * 9 + fields[
                    1].strip() + " " * 10 + "|" + " " * 14 + str(duration) + " " * 13 + "|")

    print("+" + "-" * 28 + "+" + "-" * 29 + "+" + "-" * 29 + "+")


