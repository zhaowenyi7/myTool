import os
from PIL import Image
import numpy as np
import cv2
import os


def get_imlist(path):
    """返回目录中所有JPG图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """使用PIL重新定义图像数组的大小"""
    pil_im = Image.fromarray(im)
    return np.array(pil_im.resize(sz))