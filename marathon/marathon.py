from utils.valid_util import *
from best_wishes import select_route


her_name = "刘姝鹏"
my_name = "高庆龙"

def return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    marathon_show()


def marathon_show():
    select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> 2019.05.12 大连半程\t\t\t\t   |\n" + \
        "| <2> 2019.05.26 沈阳女子半程\t\t\t\t   |\n" + \
        "| <3> 2019.06.17 锦州半程\t\t\t\t   |\n" + \
        "| <4> 2019.06.23 吉林半程\t\t\t\t   |\n" + \
        "| <5> 2019.09.08 沈阳全马\t\t\t\t   |\n" + \
        "| <6> 2019.11.03 北京全马\t\t\t\t   |\n" + \
        "| <7> 2019.12.01 千岛湖半程\t\t\t\t   |\n" + \
        "| <8> 2020.12.06 千岛湖半程\t\t\t\t   |\n" + \
        "| <0> Exit\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select = input(select_parse)
    select = module_select(select, select_parse, 0, 8)

    if int(select) == 1:
        dalian_half_2019_05_12()
        return_button()

    elif int(select) == 2:
        shenyang_girl_half_2019_05_26()
        return_button()

    elif int(select) == 3:
        jinzhou_half_2019_06_17()
        return_button()

    elif int(select) == 4:
        jilin_half_2019_06_23()
        return_button()

    elif int(select) == 5:
        shenyang_all_2019_09_08()
        return_button()

    elif int(select) == 6:
        beijing_all_2019_11_03()
        return_button()

    elif int(select) == 7:
        qiandaohu_half_2019_12_01()
        return_button()

    elif int(select) == 8:
        qiandaohu_half_2020_12_06()
        return_button()

    else:
        select_route()




def dalian_half_2019_05_12():
    base = "2019.05.12 大连半程马拉松"
    title = "获得29岁以下大众二级选手称号，恭喜！"

    race_no = "2F2894"
    gun_time = "2:28:12"
    net_time = "2:13:42"
    avg_pace = "06:21"
    avg_speed = "09:47"

    km_5_timing = "0:31:03"
    km_5_time = "0:31:03"
    km_10_timing = "1:01:49"
    km_10_time = "0:30:46"
    km_15_timing = "1:47:14"
    km_15_time = "0:30:55"
    km_20_timing = "2:06:35"
    km_20_time = "0:33:52"
    half_finish_timing = "2:13:42"
    half_finish_time = "0:07:08"

    gender_place_gun_time = "573"
    gender_place_net_time = "439"

    overall_place_gun_time = "4132"
    overall_place_net_time = "3656"

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time, half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name)


def shenyang_girl_half_2019_05_26():
    base = "2019.05.26 沈阳女子半程马拉松"
    title = None

    race_no = "20439"
    gun_time = "02:06:50"
    net_time = "02:06:42"
    avg_pace = ""
    avg_speed = ""

    km_5_timing = ""
    km_5_time = ""
    km_10_timing = ""
    km_10_time = ""
    km_15_timing = ""
    km_15_time = ""
    km_20_timing = ""
    km_20_time = ""
    half_finish_timing = ""
    half_finish_time = ""

    gender_place_gun_time = "69"
    gender_place_net_time = "70"

    overall_place_gun_time = "69"
    overall_place_net_time = "70"

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name)


def jinzhou_half_2019_06_17():
    base = "2019.06.17 锦州半程马拉松"
    title = None

    race_no = "B2048"
    gun_time = "02:05:34"
    net_time = "02:05:26"
    avg_pace = "05:57"
    avg_speed = ""

    km_5_timing = ""
    km_5_time = ""
    km_10_timing = ""
    km_10_time = "00:58:45"
    km_15_timing = ""
    km_15_time = "00:23:13"
    km_20_timing = ""
    km_20_time = ""
    half_finish_timing = ""
    half_finish_time = "00:43:29"

    gender_place_gun_time = "580"
    gender_place_net_time = "142"

    overall_place_gun_time = "580"
    overall_place_net_time = "142"

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time, half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name)


def jilin_half_2019_06_23():
    base = "2019.06.23 吉林半程马拉松"
    title = "获得(20-24)岁年龄段第7名，恭喜！"

    race_no = "D0875"
    gun_time = "2:17:01"
    net_time = "2:13:32"
    avg_pace = "00:06:20"
    avg_speed = "9:48"

    km_5_timing = "0:29:39"
    km_5_time = "0:29:39"
    km_10_timing = "1:01:40"
    km_10_time = "0:32:01"
    km_15_timing = "1:33:29"
    km_15_time = "0:31:49"
    km_20_timing = "2:05:44"
    km_20_time = "0:32:15"
    half_finish_timing = ""
    half_finish_time = ""

    gender_place_gun_time = "154"
    gender_place_net_time = "161"

    overall_place_gun_time = "1282"
    overall_place_net_time = "1346"

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing,
                    km_20_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name)


def shenyang_all_2019_09_08():
    base = "2019.09.08 沈阳全程马拉松"
    title = None

    race_no = "A0203"
    gun_time = "4:54:29"
    net_time = "4:53:43"
    avg_pace = ""
    avg_speed = ""

    km_5_timing = "00:26:21"
    km_5_time = "00:26:21"
    km_10_timing = "00:50:54"
    km_10_time = "00:24:33"
    km_15_timing = "01:16:31"
    km_15_time = "00:25:37"
    km_20_timing = "01:43:12"
    km_20_time = "00:26:41"
    km_25_timing = "02:14:33"
    km_25_time = "00:31:21"
    km_30_timing = "02:52:09"
    km_30_time = "00:37:36"
    km_35_timing = "03:38:31"
    km_35_time = "00:46:22"
    km_40_timing = "04:29:12"
    km_40_time = "00:50:41"
    half_finish_timing = ""
    half_finish_time = ""

    gender_place_gun_time = "1585/2584"
    gender_place_net_time = "1593/2584"

    overall_place_gun_time = "1836/3096"
    overall_place_net_time = "1846/3096"

    print_all_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time,
                    km_25_timing, km_25_time, km_30_timing, km_30_time, km_35_timing, km_35_time, km_40_timing, km_40_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, my_name, True)


def beijing_all_2019_11_03():
    base = "2019.11.03 北京全程马拉松"
    title = "获得29岁以下大众一级选手称号，恭喜！"

    race_no = "F8918"
    gun_time = "4:23:30"
    net_time = "4:10:32"
    avg_pace = "00:05:57"
    avg_speed = "10:11"

    km_5_timing = "0:29:30"
    km_5_time = "0:29:30"
    km_10_timing = "00:59:33"
    km_10_time = "00:30:03"
    km_15_timing = "01:29:01"
    km_15_time = "00:29:08"
    km_20_timing = "01:59:18"
    km_20_time = "00:30:17"
    km_25_timing = "02:30:07"
    km_25_time = "00:30:49"
    km_30_timing = "02:59:50"
    km_30_time = "00:29:43"
    km_35_timing = "03:29:34"
    km_35_time = "00:29:44"
    km_40_timing = "03:58:23"
    km_40_time = "00:28:49"
    half_finish_timing = "2:06:01"
    half_finish_time = "2:19:00"

    gender_place_gun_time = "2805/5874"
    gender_place_net_time = "1848/5874"

    overall_place_gun_time = "15435/29402"
    overall_place_net_time = "14398/29402"

    print_all_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time,
                    km_25_timing, km_25_time, km_30_timing, km_30_time, km_35_timing, km_35_time, km_40_timing, km_40_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name, True)


def qiandaohu_half_2019_12_01():
    base = "2019.12.01 千岛湖半程马拉松"
    title = "获得29岁以下大众一级选手称号，恭喜！"

    race_no = "C25564"
    gun_time = ""
    net_time = "01:58:54"
    avg_pace = ""
    avg_speed = ""

    km_5_timing = "00:30:08"
    km_5_time = "00:30:08"
    km_10_timing = "00:59:21"
    km_10_time = "00:29:13"
    km_15_timing = "01:27:11"
    km_15_time = "00:27:50"
    km_20_timing = "01:53:16"
    km_20_time = "00:26:05"
    half_finish_timing = "01:58:54"
    half_finish_time = "00:05:38"

    gender_place_gun_time = "194"
    gender_place_net_time = "194"

    overall_place_gun_time = ""
    overall_place_net_time = ""

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing,
                    km_20_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, her_name, True)


def qiandaohu_half_2020_12_06():
    base = "2020.12.06 千岛湖半程马拉松"
    title = None
    tab_3 = "\t\t\t"
    tab_2 = "\t\t"

    our_name = "刘姝鹏" + tab_3 + "高庆龙"
    race_no = "C29201" + tab_3 + "C29202"
    gun_time = ""
    net_time = "02:28:02" + tab_3 + "02:28:01"
    avg_pace = ""
    avg_speed = ""

    km_5_timing = "00:30:56" + tab_3 + "00:30:54"
    km_5_time = "00:30:56" + tab_3 + "00:30:54"
    km_10_timing = "01:01:14" + tab_3 + "01:01:12"
    km_10_time = "00:30:18" + tab_3 + "00:30:18"
    km_15_timing = "01:41:58" + tab_3 + "01:41:57"
    km_15_time = "00:40:44" + tab_3 + "00:40:45"
    km_20_timing = "02:21:00" + tab_3 + "02:21:18"
    km_20_time = "00:39:02" + tab_3 + "00:39:21"
    half_finish_timing = "02:28:02" + tab_2 + "02:28:01"
    half_finish_time = "00:07:02" + tab_2 + "00:06:43"

    gender_place_gun_time = "1122" + tab_3 + "2566"
    gender_place_net_time = "1122" + tab_3 + "2566"

    overall_place_gun_time = ""
    overall_place_net_time = ""

    print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing,
                    km_20_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, our_name)


def print_half_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time, half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, name, is_pb = False):
    print("*" * 60)
    print(":) Base Info")
    print()
    print("\t\t* " + base + " *")
    print()
    if title is not None:
        print("\t|  TITLE : " + title)
        print("\t|")
    print("\t|  NAME : " + name)
    print("\t|  RACE NO  : " + race_no)
    if gun_time != "":
        print("\t|  GUN TIME : " + gun_time)
    if is_pb:
        print("\t|  NET TIME : " + net_time + " (PB)")
    else:
        print("\t|  NET TIME : " + net_time)
    if avg_pace != "":
        print("\t|  PACE  : " + avg_pace)
    if avg_speed != "":
        print("\t|  SPEED : " + avg_speed)

    if km_5_timing != "" and km_10_timing != "" and km_15_timing != "" and km_20_timing != "":
        print()
        print(":) Net Split Time - Timing")

    if km_5_timing != "":
        print("\t|  05KM : " + km_5_timing)
    if km_10_timing != "":
        print("\t|  10KM : " + km_10_timing)
    if km_15_timing != "":
        print("\t|  15KM : " + km_15_timing)
    if km_20_timing != "":
        print("\t|  20KM : " + km_20_timing)
    if half_finish_timing != "":
        print("\t|  HALF Finish : " + half_finish_timing)

    if km_5_time != "" and km_10_time != "" and km_15_time != "" and km_20_time != "":
        print()
        print(":) Net Split Time - Time")
    if km_5_time != "":
        print("\t|  05KM : " + km_5_time)
    if km_10_time != "":
        print("\t|  10KM : " + km_10_time)
    if km_15_time != "":
        print("\t|  15KM : " + km_15_time)
    if km_20_time != "":
        print("\t|  20KM : " + km_20_time)
    if half_finish_time != "":
        print("\t|  HALF Finish : " + half_finish_time)

    if gender_place_gun_time != "" and gender_place_net_time != "":
        print()
        print(":) Gender Place")
    if gender_place_gun_time != "":
        print("\t|  GUN TIME : " + gender_place_gun_time)
    if gender_place_net_time != "":
        print("\t|  NET TIME : " + gender_place_net_time)

    if overall_place_gun_time != "" and overall_place_net_time != "":
        print()
        print(":) Overall Place")
    if overall_place_gun_time != "":
        print("\t|  GUN TIME : " + overall_place_gun_time)
    if overall_place_net_time != "":
        print("\t|  NET TIME : " + overall_place_net_time)

    print()
    print("*" * 60)


def print_all_info(base, title, race_no, gun_time, net_time, avg_pace, avg_speed,
                    km_5_timing, km_5_time, km_10_timing, km_10_time, km_15_timing, km_15_time, km_20_timing, km_20_time,
                    km_25_timing, km_25_time, km_30_timing, km_30_time, km_35_timing, km_35_time, km_40_timing, km_40_time,
                    half_finish_timing, half_finish_time,
                    gender_place_gun_time, gender_place_net_time, overall_place_gun_time, overall_place_net_time, name, is_pb = False):

    print("*" * 60)
    print(":) Base Info")
    print()
    print("\t\t* " + base + " *")
    print()
    if title is not None:
        print("\t|  TITLE : " + title)
        print("\t|")
    print("\t|  NAME : " + name)
    print("\t|  RACE NO  : " + race_no)
    print("\t|  GUN TIME : " + gun_time)
    if is_pb:
        print("\t|  NET TIME : " + net_time + " (PB)")
    else:
        print("\t|  NET TIME : " + net_time)
    if avg_pace != "":
        print("\t|  PACE  : " + avg_pace)
    if avg_speed != "":
        print("\t|  SPEED : " + avg_speed)

    if km_5_timing != "" and km_10_timing != "" and km_15_timing != "" and km_20_timing != "" \
            and km_25_timing != "" and km_30_timing != "" and km_35_timing != "" and km_40_timing != "":
        print()
        print(":) Net Split Time - Timing")

    if km_5_timing != "":
        print("\t|  05KM : " + km_5_timing)
    if km_10_timing != "":
        print("\t|  10KM : " + km_10_timing)
    if km_15_timing != "":
        print("\t|  15KM : " + km_15_timing)
    if km_20_timing != "":
        print("\t|  20KM : " + km_20_timing)
    if km_25_timing != "":
        print("\t|  25KM : " + km_25_timing)
    if km_30_timing != "":
        print("\t|  30KM : " + km_30_timing)
    if km_35_timing != "":
        print("\t|  35KM : " + km_35_timing)
    if km_40_timing != "":
        print("\t|  40KM : " + km_40_timing)
    if half_finish_timing != "":
        print("\t|  HALF Finish : " + half_finish_timing)

    if km_5_time != "" and km_10_time != "" and km_15_time != "" and km_20_time != "" \
            and km_25_time != "" and km_30_time != "" and km_35_time != "" and km_40_time != "":
        print()
        print(":) Net Split Time - Time")
    if km_5_time != "":
        print("\t|  05KM : " + km_5_time)
    if km_10_time != "":
        print("\t|  10KM : " + km_10_time)
    if km_15_time != "":
        print("\t|  15KM : " + km_15_time)
    if km_20_time != "":
        print("\t|  20KM : " + km_20_time)
    if km_25_time != "":
        print("\t|  25KM : " + km_25_time)
    if km_30_time != "":
        print("\t|  30KM : " + km_30_time)
    if km_35_time != "":
        print("\t|  35KM : " + km_35_time)
    if km_40_time != "":
        print("\t|  40KM : " + km_40_time)
    if half_finish_time != "":
        print("\t|  HALF Finish : " + half_finish_time)

    if gender_place_gun_time != "" and gender_place_net_time != "":
        print()
        print(":) Gender Place")
    if gender_place_gun_time != "":
        print("\t|  GUN TIME : " + gender_place_gun_time)
    if gender_place_net_time != "":
        print("\t|  NET TIME : " + gender_place_net_time)

    if overall_place_gun_time != "" and overall_place_net_time != "":
        print()
        print(":) Overall Place")
    if overall_place_gun_time != "":
        print("\t|  GUN TIME : " + overall_place_gun_time)
    if overall_place_net_time != "":
        print("\t|  NET TIME : " + overall_place_net_time)

    print()
    print("*" * 60)

