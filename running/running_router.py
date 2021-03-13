from utils.valid_util import module_select
# from running.draw_running_track import show_running_track
from running.gps_parse import generate_run_history
from running.show_scores import show_hero_score
import os


def track_return_button():
    # print("Return ? [y/n] (default n): ", end="")
    # is_quit = input()
    # while is_quit != 'y':
    #     select_track(track_show_dict)
    #     print("Return ? [y/n] (default n): ", end="")
    #     is_quit = input()
    running_router()

def detail_return_button():
    print("Return ? [y/n] (default n): ", end="")
    is_quit = input()
    while is_quit != 'y':
        select_detail(track_show_dict)
        print("Return ? [y/n] (default n): ", end="")
        is_quit = input()
    running_router()


def running_return_button():
    print("任意键返回\n", end="")
    input("Please input: ")
    running_router()


def select_detail(track_show_dict):
    num = input("\nPlease select detail route: ")
    num = module_select(num, "Error! Please select detail route: ", 1, len(track_show_dict))
    path = track_show_dict.get(int(num))

    print(path)
    # print(":) 暂时隐藏...")

# def select_track(track_show_dict):
#     num = input("\nPlease select track route: ")
#     num = module_select(num, "Error! Please select track route: ", 1, len(track_show_dict))
#     path = track_show_dict.get(int(num))
#     input_sample = input("Please input sample (default 30): ")
#     if input_sample == "":
#         sample_n = 30
#     else:
#         sample_n = int(input_sample)
#
#     input_delay = input("Please input delay (default 10ms): ")
#     if input_delay == "":
#         delay = 10
#     else:
#         delay = int(input_delay)
#
#     input_figure = input("Please figure size (default 5x7): ")
#
#     if not input_figure.__contains__("x"):
#         long = 5
#         width = 7
#     else:
#         fields = input_figure.split("x")
#         long = int(fields[0])
#         width = int(fields[1])
#
#     show_running_track(path, sample_n, delay, long, width)
#     # print(":) 暂时隐藏...")



def running_router():
    global track_show_dict
    function_select_parse = \
        "+" + "-" * 58 + "+\n" \
        "| <1> Show hero score\t\t\t\t\t   |\n" + \
        "| <2> PK\t\t\t\t\t\t   |\n" + \
        "| <3> Show together time\t\t\t\t   |\n" + \
        "| <4> Upload running file\t\t\t\t   |\n" + \
        "| <5> Download running file\t\t\t\t   |\n" + \
        "| <0> Return\t\t\t\t\t\t   |\n" + \
        "+" + "-" * 58 + "+\n" + \
        "Please select: "

    print()
    select_num = input(function_select_parse)
    select_num = module_select(select_num, function_select_parse, 0, 5)

    # 分支一：
    if int(select_num) == 1:

        history_dir = os.path.abspath("resources/run_record/history").replace("running\\", "").replace("\\", "/")

        if len(os.listdir(history_dir)) == 0:
            generate_run_history()
            from running.gps_parse import delete_result_dir, result_dir
            try:
                delete_result_dir(result_dir)
            except Exception as e:
                pass
        else:
            y_or_n = input("Parse? [y/n] (default: n): ")
            if y_or_n == "y":
                generate_run_history()
                from running.gps_parse import delete_result_dir, result_dir
                try:
                    delete_result_dir(result_dir)
                except Exception as e:
                    pass

        track_show_dict = {}
        try:
            track_show_dict = show_hero_score()
        except Exception as e:
            print(e)
            track_return_button()

        # select_track(track_show_dict)
        # track_return_button()

        select_detail(track_show_dict)
        detail_return_button()

        # running_return_button() # un running


    elif int(select_num) == 2:
        from running.pk import pk
        pk()
        running_return_button()

    elif int(select_num) == 3:
        from running.together_time import show_together_time
        # from running.gps_parse import delete_result_dir, result_dir
        print()
        print("+" + "-" * 58 + "+")
        print("|" + " " * 28 + "DAYS" + "  " + "HOURS" + "  " + "MINUTES" + "  " + "SECONDS" + " |")
        print("|" + " " * 58 + "|")
        print("|" + show_together_time() + "|")
        print("+" + "-" * 58 + "+")
        running_return_button()

    elif int(select_num) == 4:
        from sftp_client import upload_running_record
        upload_running_record()
        running_return_button()

    elif int(select_num) == 5:
        from sftp_client import download_running_record
        download_running_record()
        running_return_button()

    elif int(select_num) == 6:
        from sftp_client import show
        show()
        running_return_button()

    else:
        from best_wishes import select_route
        select_route()


if __name__ == '__main__':
    fields = "5 7".__contains__("x")
    print(fields)
