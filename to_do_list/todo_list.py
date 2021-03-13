def todo_list():
    print()
    print("+" + "-" * 78 + "+")
    print("|" + " " * 30 + "PLAN TIME" + " " * 19 + "FIRST TIME" + " " * 10 + "|")
    print("|" + " " * 78 + "|")

    no_finished = " " * 19

    print("| " + "01. Make love. " + " " * 14 + "2021-02-10 23:24:00" + " " * 9 + no_finished + " |")
    print("| " + "02. Buy underwear together." + " " * 2 + "2021-02-12 01:21:00" + " " * 9 + no_finished + " |")
    print("| " + "03. Stroll the streets." + " " * 6 + "2021-02-12 13:29:00" + " " * 9 + no_finished + " |")
    print("| " + "04. Watch AV together." + " " * 7 + "2021-02-13 00:19:00" + " " * 9 + no_finished + " |")
    print("| " + "05. 给她擦身体乳." + " " * 12 + "2021-02-14 18:20:00" + " " * 9 + no_finished + " |")
    print("| " + "06. 一起跑马拉松." + " " * 12 + "2021-01-03 10:40:00" + " " * 9 + "2020-12-06 07:00:00" + " |")
    print("| " + "07. 她跑马拉松在终点等她." + " " * 4 + "2021-01-03 10:40:00" + " " * 9 + no_finished + " |")
    print("| " + "08. 一起献最小毫升的血." + " " * 6 + "2021-01-10 17:01:00" + " " * 9 + no_finished + " |")
    print("| " + "09. 一起放烟花." + " " * 14 + "2021-01-25 01:04:00" + " " * 9 + no_finished + " |")
    print("| " + "10. 穿情侣睡衣." + " " * 14 + "2021-02-21 14:25:00" + " " * 9 + no_finished + " |")

    """
    Wait for her at the end of the marathon
    跑马拉松在终点等她
    献最小毫升的血
    """
    print("+" + "-" * 78 + "+")


def first_time():
    print()
    print("+" + "-" * 78 + "+")
    print("|" + " " * 30 + "QINGLONG.GAO RECORD" + " " * 29 + "|")
    print("|" + " " * 78 + "|", end="")
    print("""
| 2020-12-31 00:00:00 First : Do the countdown together                        |
| 2021-01-01 00:00:00 First : Hangzhou West Lake rose run                      |
| 2021-01-02 00:00:00 First : Hand in hand, visiting West Lake                 |
| 2021-01-17 00:00:00 First : Know your physiological period (more 30)         |
| 2021-01-23 00:00:00 First : Go to your house (Hangzhou)                      |
| 2021-01-23 00:00:00 First : Watch movie (拆弹专家)                           |
| 2021-01-23 00:00:00 First : KTV for us                                       |
| 2021-01-23 00:00:00 First : Kiss *^_^*                                       |
| 2021-01-23 00:00:00 First : Touch your breast (one) *^_^*                    |
| 2021-01-27 00:52:00 First : Say "I love U"                                   |
| 2021-02-05 00:00:00 Plan private module (touch another breast.. next) *^_^*  |
""", end="")
    print("+" + "-" * 78 + "+")


if __name__ == '__main__':
    todo_list()
    first_time()
