from PIL import Image
import numpy as np
import os


# file_name = "微信图片_20210213194550.jpg"
file_name = "111.jpg"
# a = np.array(Image.open("./pic/微信图片_20210213194507.jpg").convert('L')).astype('float')
a = np.array(Image.open("./pic/" + file_name).convert('L')).astype('float')


for i in range(1, 8):
    depth = i         # (0-100)
    grad_x, grad_y = np.gradient(a)     # 对图像灰度的梯度值，分别取横纵图的梯度值
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    vec_el = np.pi / 2.2                # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.                 # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)# 光源对x轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)# 光源对x轴的影响
    dz = np.sin(vec_el)  # 光源对x轴的影响

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)    # 光源归一化
    b = b.clip(0, 255)

    im = Image.fromarray(b.astype('uint8'))

    save_path = './' + file_name + "_"
    im.save(save_path + str(i) + ".jpg")
    print("save success!")
