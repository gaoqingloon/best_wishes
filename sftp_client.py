from stat import S_ISDIR
from download import ShowProcess
import paramiko
import os


class SFTPClient(object):
    """
    定义一个类，连接一台远端linux主机
    """

    def __init__(self, ip, port, username, password, timeout=30):
        """
        通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
        :param ip:
        :param username:
        :param password:
        :param timeout:
        """
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
        t = paramiko.Transport(sock=(self.ip, self.port))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        return sftp

    @staticmethod
    def mk_remote_dir(sftp, path, remote_dir):
        # path = "/home/gql/running/udpdata/resources/testt"
        path = path.replace(remote_dir + "/", "")
        mk_path = remote_dir
        for field in path.split("/"):
            mk_path += "/" + field
            try:
                sftp.stat(mk_path)
            except Exception:
                sftp.mkdir(mk_path)

    @staticmethod
    def mk_local_dir(path, local_dir):
        # path = "E:/PycharmProjects/hello/resources/udpdata/resources/testt"
        path = path.replace(local_dir + "/", "")
        mk_path = local_dir
        for field in path.split("/"):
            mk_path += "/" + field
            if not os.path.exists(mk_path):
                os.makedirs(mk_path)

    @staticmethod
    def isdir(sftp, path):
        return str(sftp.stat(path))[0] == 'd'

    def tree(self, sftp, directory, layer=0):
        listdir = sftp.listdir(directory)
        for index, file in enumerate(listdir):
            file_path = directory + "/" + file
            print("|  " * (layer - 1), end="")
            if layer > 0:
                print("`--" if index == len(listdir) - 1 else "|--", end="")
            print(file)
            if self.isdir(sftp, file_path):
                self.tree(sftp, file_path, layer + 1)

    def sftp_get(self, remote_file, local_file):
        """
        get单个文件
        :param remote_file:
        :param local_file:
        :return:
        """
        sftp = self.connect()
        sftp.get(remote_file, local_file)
        sftp.close()

    def sftp_put(self, local_file, remote_file):
        """
        put单个文件
        :param local_file:
        :param remote_file:
        :return:
        """
        sftp = self.connect()
        sftp.put(local_file, remote_file)
        sftp.close()

    def __get_all_files_in_remote_dir(self, sftp, remote_dir):
        """
        获取远端linux主机上指定目录及其子目录下的所有文件
        :param sftp:
        :param remote_dir:
        :return:
        """
        all_files = list()

        # 去掉路径字符串最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = sftp.listdir_attr(remote_dir)
        for x in files:
            # remote_dir目录中每一个文件或目录的完整路径
            filename = remote_dir + '/' + x.filename
            # 如果是目录，则递归处理该目录，这里用到了stat库中的S_ISDIR方法，与linux中的宏的名字完全一致
            if S_ISDIR(x.st_mode):
                all_files.extend(self.__get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_get_dir(self, remote_dir, local_dir):
        """
        /home/gql/running/... => E:/tmp == E:/tmp/...
        :param remote_dir: /home/gql/running
        :param local_dir: E:/tmp
        :return:
        """
        sftp = self.connect()

        # 获取远端linux主机上指定目录及其子目录下的所有文件
        local_files = self.__get_all_files_in_local_dir(local_dir)
        remote_files = self.__get_all_files_in_remote_dir(sftp, remote_dir)

        remote_base_dir = ""
        local_files_set = set()
        remote_files_set = set()
        for file in local_files:
            local_files_set.add(file.split("/resources/")[-1])
        for file in remote_files:
            remote_base_dir = file.split("/resources/")[0]
            remote_files_set.add(file.split("/resources/")[-1])

        # print("local_files_set", local_files_set)
        # print("remote_files_set", remote_files_set)
        # print("x", remote_files_set.difference(local_files_set))
        # print("base", remote_base_dir)


        all_files = remote_files_set.difference(local_files_set)
        if len(all_files) == 0:
            sftp.close()
            print(":) 当前本地已是最新记录，快去呼唤她/他跑步吧~")
            return

        print(":) Running file downloading...")
        process_bar = ShowProcess(len(all_files), 'OK')

        # 依次get每一个文件
        is_mkdir = True
        for x in all_files:
            x = remote_base_dir + "/resources/" + x
            # /home/gql/running/udpdata/udp_data_2020_0527_094320.csv
            # "E:/PycharmProjects/hello/resources/udpdata/resources/testt"
            filename = x.replace(remote_dir + "/", "")
            if len(filename.split("/")) >= 2:
                local_filename = local_dir + "/" + filename
                if is_mkdir:
                    self.mk_local_dir(local_filename[:local_filename.rindex("/")], local_dir)
                    is_mkdir = False
            else:
                filename = os.path.split(x)[-1]
                local_filename = local_dir + '/' + filename
            # print(':) Download file %s ...' % filename)
            process_bar.show_process()
            sftp.get(x, local_filename)
        sftp.close()
        print(":) Running file download success!")

    def __get_all_files_in_local_dir(self, local_dir):
        """
        获取本地指定目录及其子目录下的所有文件
        :param local_dir:
        :return:
        """
        # 保存所有文件的列表
        all_files = list()

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = os.listdir(local_dir)
        for x in files:
            # local_dir目录中每一个文件或目录的完整路径
            filename = local_dir + "/" + x
            # 如果是目录，则递归处理该目录
            if os.path.isdir(filename):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_put_dir(self, local_dir, remote_dir):

        """
        /tmp/... => /home/gql/running  == /home/gql/running/...
        :param local_dir:
        :param remote_dir:
        :return:
        """
        sftp = self.connect()

        # 去掉路径字符穿最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取本地指定目录及其子目录下的所有文件
        local_files = self.__get_all_files_in_local_dir(local_dir)

        # all_files = self.__get_all_files_in_local_dir(local_dir)
        remote_files = self.__get_all_files_in_remote_dir(sftp, remote_dir)

        base_local_dir = ""
        local_files_set = set()
        remote_files_set = set()
        for file in local_files:
            base_local_dir = file.split("/resources/")[0]
            local_files_set.add(file.split("/resources/")[-1])
        for file in remote_files:
            remote_files_set.add(file.split("/resources/")[-1])

        # print("local_files_set", local_files_set)
        # print("remote_files_set", remote_files_set)
        # print("x", local_files_set.difference(remote_files_set))
        # print("base", base_local_dir)

        all_files = local_files_set.difference(remote_files_set)
        if len(all_files) == 0:
            sftp.close()
            print(":) 您的新跑步记录已不足，快去跑步哦~")
            return

        print(":) Running file uploading...")
        process_bar = ShowProcess(len(all_files), 'OK')

        # 依次put每一个文件
        is_mkdir = True
        for x in all_files:
            x = base_local_dir + "/resources/" + x
            # 'E:/PycharmProjects/hello/resources/udpdata/xx.csv'
            # filename = os.path.split(x)[-1]
            filename = x.replace(local_dir + "/", "")
            if len(filename.split("/")) >= 2:
                remote_filename = remote_dir + '/' + filename
                if is_mkdir:
                    self.mk_remote_dir(sftp, remote_filename[:remote_filename.rindex("/")], remote_dir)
                    is_mkdir = False
            else:
                filename = os.path.split(x)[-1]
                remote_filename = remote_dir + '/' + filename
            # print(':) Upload file %s ...' % filename)
            process_bar.show_process()
            sftp.put(x, remote_filename)
        sftp.close()
        print(":) Running file upload success!")


ip = '106.53.222.179'
port = 52113
user_name = "gql"
password = "su-root123456"

remote_path = '/home/gql/running/resources/run_record/src'
local_path = str(os.getcwd()).replace("\\", "/") + '/resources/run_record/src'
host = SFTPClient(ip=ip, port=port, username=user_name, password=password)


def upload_running_record():
    print()
    host.sftp_put_dir(local_path, remote_path)


def download_running_record():
    print()
    host.sftp_get_dir(remote_path, local_path)


def show():
    print()
    host.tree(host.connect(), remote_path)


if __name__ == '__main__':
    ip = '106.53.222.179'
    port = 52113
    user_name = "gql"
    password = "su-root123456"

    remote_path = '/home/gql/running/resources'
    local_path = str(os.getcwd()).replace("\\", "/") + '/resources'

    host = SFTPClient(ip=ip, port=port, username=user_name, password=password)

    # 将远端remote_path目录中的所有文件get到本地local_path目录
    host.sftp_get_dir(remote_path, local_path)

    # 将本地local_path目录中的所有文件put到远端remote_path目录
    host.sftp_put_dir(local_path, remote_path)

    host.tree(host.connect(), remote_path)


"""
rmdir(path) ：删除目录
remove(path) ：删除文件
rename(oldpath, newpath)
stat(path)：获取文件信息
listdir(path)：获取目录列表
getcwd()：查看当前所在目录
chdir(path)：切换当前目录
chmod(path , mode) ：修改目录或者文件权限
chown(path,uid ,gid)：修改目录或者文件的用户组

1. 上传自己新文件
2. 同步当前目录下的所有文件

def tree_dir(directory, layer=0):
    listdir = os.listdir(directory)
    for index, file in enumerate(listdir):
        file_path = os.path.join(directory, file)
        print("|  " * (layer - 1), end="")
        if layer > 0:
            print("`--" if index == len(listdir) - 1 else "|--", end="")
        print(file)
        if os.path.isdir(file_path):
            tree_dir(file_path, layer + 1)
"""
