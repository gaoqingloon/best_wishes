from utils.valid_util import *

BEFORE_TIME = "2021-01-17"
DEFAULT_PERIOD = 30
DEFAULT_BORDER = "*"
HEART_PARSE = ['猪猪, I LOVE YOU.',
               '你黑暗的时候我陪你等天亮。',
               '鱼是海的故事，你是我的故事！',
               '我想牵你的手,从心动到古稀!',
               '自从遇见你，人生苦短，甜长',
               '愿抓紧你的手，走过未来的朝朝暮暮',
               '我有一百种样子，我有一百个喜欢。',
               '你是我口中最为骄傲的语气',
               '没有什么什么软肋，除了你。',
               '遇见你，是一切美好的开始！',
               '你就是我要寻找的小幸福。',
               '我发现，你在我心中的位置会膨胀！',
               '最浪漫的事，就是和你一起慢慢变老',
               '你那么瘦，却还是填满了我的心',
               '你好，能不能借一生说话。',
               '天青色等烟雨，而我在等你',
               '为你遇见你，竟花光了我所有的运气',
               '想去的地方有你才最美丽。',
               '不知道爱你算不算是一个贴心的理由？',
               '两情若是久长时，又岂在朝朝暮暮。',
               '你是我此生最美的风景!']


def together_time():
    """
    【欢迎语】在一起的时间
    :return:
    """
    days, hours, seconds = cal_detail_time(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "2021-01-03 11:18:00")
    print()
    print("*" * 60)
    print(":)" + " " * 4 + "Together for " + str(days + 1) + " days, " + str(hours) + " hours, " + str(
        seconds) + " seconds." + " " * 4 + "*")
    print("*" * 60)
