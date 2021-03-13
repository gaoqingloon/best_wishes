from utils.valid_util import *
import os

BEFORE_TIME = "2021-01-17"
DEFAULT_PERIOD = 30
DEFAULT_BORDER = "*"

heart_file = os.path.abspath("resources/heart_phrase.txt").replace("common\\", "").replace("commemorative_moment\\", "").replace("\\", "/")
# HEART_PARSE = ['猪猪, I LOVE YOU.',
#                '你黑暗的时候我陪你等天亮。',
#                '鱼是海的故事，你是我的故事！',
#                '我想牵你的手,从心动到古稀!',
#                '自从遇见你，人生苦短，甜长',
#                '愿抓紧你的手，走过未来的朝朝暮暮',
#                '我有一百种样子，我有一百个喜欢。',
#                '你是我口中最为骄傲的语气',
#                '没有什么软肋，除了你。',
#                '遇见你，是一切美好的开始！',
#                '你就是我要寻找的小幸福。',
#                '我发现，你在我心中的位置会膨胀！',
#                '最浪漫的事，就是和你一起慢慢变老',
#                '你那么瘦，却还是填满了我的心',
#                '你好，能不能借一生说话。',
#                '天青色等烟雨，而我在等你',
#                '为你遇见你，竟花光了我所有的运气',
#                '想去的地方有你才最美丽。',
#                '不知道爱你算不算是一个贴心的理由？',
#                '两情若是久长时，又岂在朝朝暮暮。',
#                '你是我此生最美的风景!']

try:
    f = open(heart_file, "r")
    f.close()
except Exception:
    f = open(heart_file, "w")
    f.write('遇见你，是一切美好的开始！')
    f.close()


###################################################
def upload():
    from sftp_client import host
    sftp = host.connect()

    remote_file = '/home/gql/running/resources/heart_phrase.txt'
    local_file = str(os.getcwd()).replace("\\", "/") + '/resources/heart_phrase.txt'

    sftp.put(local_file, remote_file)


def download():
    from sftp_client import host
    sftp = host.connect()

    remote_file = '/home/gql/running/resources/heart_phrase.txt'
    local_file = str(os.getcwd()).replace("\\", "/") + '/resources/heart_phrase.txt'

    sftp.get(remote_file, local_file)


def get_remote_file_size():
    from sftp_client import host
    sftp = host.connect()
    remote_file = '/home/gql/running/resources/heart_phrase.txt'

    remote_file_size = sftp.stat(remote_file).st_size
    return remote_file_size

###################################################

def get_heart_phrase():

    try:
        local_file = str(os.getcwd()).replace("\\", "/") + '/resources/heart_phrase.txt'
        if int(os.path.getsize(local_file)) > int(get_remote_file_size()):
            upload()
        else:
            download()
    except Exception as e:
        pass

    HEART_PARSE = []
    with open(heart_file, "r", encoding="utf-8") as fr:
        for line in fr:
            HEART_PARSE.append(line.replace("\n", ""))
    return HEART_PARSE


def together_time():
    """
    【欢迎语】在一起的时间
    :return:
    """
    days, hours, minutes, seconds = cal_all_detail_time(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "2021-01-03 11:18:00")
    print()
    print("*" * 60)
    print(":)" + " " * 1 + "Together for " + str(days) + " days, " + str(
        hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")
    print("*" * 60)


if __name__ == '__main__':
    print(get_heart_phrase())
