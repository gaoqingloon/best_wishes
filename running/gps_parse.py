# coding: utf-8
import os
import gpxpy.parser as parser
import shutil
import time


source_dir = os.path.abspath("resources/run_record/src").replace("running\\", "").replace("\\", "/")
result_dir = os.path.abspath("resources/run_record/result").replace("running\\", "").replace("\\", "/")
history_dir = os.path.abspath("resources/run_record/history").replace("running\\", "").replace("\\", "/")
files_list = []


def replace(src_path, dst_path):
    with open(src_path, 'r', encoding="utf-8") as fr:
        with open(dst_path, 'w', encoding="utf-8") as fw:
            for line in fr:
                line = line \
                    .replace("<metadata>", "") \
                    .replace("</metadata>", "") \
                    .replace("<extensions>", "") \
                    .replace("</extensions>", "") \
                    .replace("type", "desc").replace("heartrate", "magvar").replace("distance", "geoidheight")
                fw.write(line)
    # print("replace " + src_path + " ok...")


def delete_result_dir(dir_path):
    """
    删除某一目录下的所有文件或文件夹
    :param file_path: 路径
    :return:
    """
    del_list = os.listdir(dir_path)
    for f in del_list:
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    shutil.rmtree(dir_path)


# def absolute_file_paths(directory):
#     """
#     某目录下所有文件的绝对路径
#     :param directory:
#     :return:
#     """
#     print(os.path.abspath(directory))
#     print(os.path.abspath(directory).replace("running\\", ""))
#     print(os.path.dirname(directory))
#     print(os.path.basename(directory))
#
#     files = os.listdir("D:\\myStudyProject\\py_project\\resources\\run_record\\source")
#     for item in files:
#         print(item)
#         if os.path.isdir(item):
#             absolute_file_paths(item)
#         else:
#             for root, _, files in os.walk(directory):
#                 for f in files:
#                     yield os.path.abspath(os.path.join(root, f))



def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        files_list.append(os.path.join(path, f))
        # print(os.path.join(path, f))


# def absolute_file_paths(directory):
#     """
#     某目录下所有文件的绝对路径
#     :param directory:
#     :return:
#     """
#     for root, _, files in os.walk(directory):
#         for f in files:
#             yield os.path.abspath(os.path.join(root, f))
"""
import os
import sys

def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path,i))]
    for f in files:
       print(os.path.join(path, f))
"""


def store_history(res_file, content, start_time, end_time, run_type, run_distance):
    """
    定义文件名字 lsp_2021-01-31-07-40-35-0000_2021-01-31-07-40-40-0000_杭州市跑步
    定义文件名字 gql_20210131074035_20210131074040_上海市跑步
    :return:
    """
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)

    if "猪猪" in res_file:
        your_name = "lsp"
    else:
        your_name = "gql"

    name_list = [your_name, start_time, end_time, run_type, run_distance]
    dst_file_name = history_dir + "/" + "_".join(name_list)
    with open(dst_file_name, 'w', encoding="utf-8") as fw:
        for line in content:
            fw.write(line)
            fw.write("\n")


def parse(src_dir):
    files_list.clear()
    print_files(src_dir)
    for path in files_list:
        if path.endswith(".gpx"):
            dst_path = path.replace("src", "result")
            dst_base_dir = os.path.dirname(dst_path)
            if not os.path.exists(dst_base_dir):
                os.makedirs(dst_base_dir)
            replace(src_path=path, dst_path=dst_path)
    print(":) Parse source file success.")


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

def generate_run_history():
    parse(source_dir)
    # print("parse....")

    files_list.clear()
    print_files(result_dir)
    # D:/myStudyProject/py_project/resources/run_record/result\\养猪专业户的跑步记录\\跑步20210101071827.gpx

    for res_file in files_list:
        # 拿到csv文件
        csv_file_path = str(res_file).replace("result", "src").replace(".gpx", ".csv")
        last_line = __get_last_line(csv_file_path)
        run_distance = str(last_line).split(",")[3].replace("\"", "")

        try:
            gpx_file = open(res_file, 'r', encoding="utf-8")
            gpx_parser = parser.GPXParser(gpx_file)
            gpx = gpx_parser.parse()  # 文件解析
            gpx_file.close()
        except Exception as e:
            continue

        # print('======================')
        # print(gpx.time)

        content = []
        run_type = ""
        # 打印解析的轨迹数据
        for track in gpx.tracks:
            # print(track.name)
            # print(track.description)
            # print('======================')
            run_type = track.name.replace(" ", "")

            for segment in track.segments:
                for point in segment.points:
                    curr_time = get_utc_time(str(point.time).split("+")[0])
                    latitude = point.latitude
                    longitude = point.longitude
                    heart_rate = point.magnetic_variation
                    distance = point.geoid_height
                    elevation = point.elevation
                    content.append(str(curr_time) + "," + str(latitude) + "," + str(longitude) + "," +
                                   str(heart_rate) + "," + str(distance) + "," + str(elevation))
        # 2021-01-31 07:40:46+00:00
        start_time = content[0].split(",")[0].replace(":", "#")
        end_time = content[-1].split(",")[0].replace(":", "#")
        # print("start_time", start_time)
        # print("end_time", end_time)

        store_history(res_file, content, start_time, end_time, run_type, run_distance)


def get_utc_time(utc_time_str):
    """
    将时间+8区
    :param utc_time_str:
    :return:
    """
    utc_time = time.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")
    utc_float_time = time.mktime(utc_time)
    beijing_float_time = utc_float_time + 8 * 60 * 60
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(beijing_float_time))




if __name__ == '__main__':
    # generate_run_history()
    line = __get_last_line("D:/myStudyProject/py_project/resources/run_record/src/猪猪的跑步记录/运动场跑步20210104095537.csv")
    print(str(line))
    print(str(line).split(",")[3].replace("\"", ""))
    # print_files("D:\\myStudyProject\\py_project\\resources\\run_record")
    # print_files("D:\\myStudyProject\\py_project\\resources\\run_record")
    # print_files(source_dir)
    # for i in files_list:
    #     print(i)
    # for i in print_files("D:\\myStudyProject\\py_project\\resources\\run_record"):
    #     print(i)