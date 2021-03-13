import os
import tkinter
import tkinter.messagebox

from PIL import Image, ImageTk

base_path = 'E:\\MyPictures\\照片\\大学活动\\工大'
root_geometry = '430x650+40+30'
inner_pic_w = 400
inner_pic_h = 600
# root_geometry = '1000x750+40+30'
# inner_pic_w = 700
# inner_pic_h = 600

root = tkinter.Tk()  # 创建tkinter应用程序窗口
root.geometry(root_geometry)  # 设置窗口的大小和位置
root.resizable(False, False)  # 不允许改变窗口的大小
root.title('时光机')  # 设置窗口主题

suffix = ('.jpg','.jpeg', '.bmp', '.png')  # 获取当前文件夹中所有图片文件列表
pics = [p for p in os.listdir(base_path) if p.endswith(suffix)]
# pics.sort(key=lambda item: str(item[:item.index('.')]))

# 用来显示图片的Label组件
lb_pic = tkinter.Label(root, text='test', width=inner_pic_w, height=inner_pic_h)
lb_pic.place(x=20, y=100, width=inner_pic_w, height=inner_pic_h)

current = 0


def change_pic(flag):
    """
    flag参数作为上下图片的调节 -1代表上一张 1代表下一个
    :param flag: 
    :return: 
    """
    global current
    new = current + flag

    if new < 0:
        tkinter.messagebox.showerror('', '这已经是第一张图片了')
    elif new >= len(pics):
        tkinter.messagebox.showerror('', '这已经是最后一张图片了')
    else:
        # 获取要切换图片文件名
        pic = pics[new]

        # 创建Image对象并进行缩放
        im = Image.open('{}/{}'.format(base_path, pic))
        w, h = im.size

        # 这里假设用来显示图片的Label组件尺寸为 400x600
        if w > inner_pic_w:
            h = int(h * inner_pic_w / w)
            w = inner_pic_w
        if h > inner_pic_h:
            w = int(w * inner_pic_h / h)
            h = inner_pic_h

        im = im.resize((w, h))

        # 创建image对象，并设置Label组件图片
        im1 = ImageTk.PhotoImage(im)
        lb_pic['image'] = im1
        lb_pic.image = im1

        current = new


def btn_pre_click():
    """
    上一张的按钮
    :return:
    """
    change_pic(-1)


def btn_next_click():
    """
    下一张按钮
    :return:
    """
    change_pic(1)


def main():
    btn_pre = tkinter.Button(root, text='上一张', command=btn_pre_click)
    btn_pre.place(x=100, y=20, width=80, height=30)

    btn_next = tkinter.Button(root, text='下一张', command=btn_next_click)
    btn_next.place(x=230, y=20, width=80, height=30)

    change_pic(0)

    # 启动
    root.mainloop()


if __name__ == '__main__':
    main()
