# import math
# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
#
#
# def global_init(file_name, simple_n, long=5, width=7):
#     global fig
#     global ax
#     global ln
#     global xdata
#     global ydata
#     fig, ax = plt.subplots(figsize=(long, width))
#     xdata, ydata = [], []
#     # ln, = plt.plot([], [], 'ro', animated=True)
#     ln, = plt.plot([], [], 'r--', marker='o', animated=True)
#
#     global x_list
#     global y_list
#     x_list = []
#     y_list = []
#     with open(
#             # "D:\\myStudyProject\\py_project\\resources\\run_record\\history\\gql_2021-01-01 07#18#28_2021-01-01 09#51#05_杭州市跑步",
#             # "D:\\myStudyProject\\py_project\\resources\\run_record\\history\\lsp_2021-01-01 07#18#15_2021-01-01 09#50#01_杭州市跑步",
#             file_name, "r") as fr:
#         index = 0
#         for line in fr:
#             if index % simple_n == 0:
#                 fields = line.split(",")
#                 x_list.append(float(fields[2]))
#                 y_list.append(float(fields[1]))
#             index += 1
#
#     x_min, x_max, y_min, y_max = math.floor(float(min(x_list)) * 100) / 100, math.ceil(
#         float(max(x_list)) * 100) / 100, math.floor(float(min(y_list)) * 100) / 100, math.ceil(
#         float(max(y_list)) * 100) / 100
#     return x_min, x_max, y_min, y_max
#
#
# def init():
#     # 30.252412,120.13
#     # ax.set_xlim(120.12, 120.16)
#     # ax.set_ylim(30.21, 30.27)
#     ax.set_xlim(x_min, x_max)
#     ax.set_ylim(y_min, y_max)
#     return ln,
#
#
# def update(frame):
#     xdata.append(float(frame[0]))
#     ydata.append(float(frame[1]))
#     ln.set_data(xdata, ydata)
#     return ln,
#
#
# def data_gen():
#     for i in range(len(x_list)):
#         yield x_list[i], y_list[i]
#
#
# def show_running_track(file_name, sample_n, delay, long=5, width=7):
#     # print("本功能不提供.")
#     global x_min, x_max, y_min, y_max
#     x_min, x_max, y_min, y_max = global_init(file_name, sample_n, long, width)
#     anim = animation.FuncAnimation(fig, update, frames=data_gen, interval=delay, repeat=False, init_func=init, blit=True)
#
#     plt.show()
#
#
# if __name__ == '__main__':
#     show_running_track(
#         "D:\\myStudyProject\\py_project\\resources\\run_record\\history\\lsp_2021-01-01 07#18#15_2021-01-01 09#50#01_杭州市跑步",
#         30, 100)
