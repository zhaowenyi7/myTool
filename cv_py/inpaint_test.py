#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time       : 2019/10/12 15:32
@Author     : WenyiZhao
@Descripion : 
@File       : inpaint_test.py
@Software   : PyCharm
"""
import numpy as np
import cv2


def inpaint_t():
    img = cv2.imread('11.jpg')
    # a, img_dot = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
    # cv2.imshow('', img_dot)
    # cv2.waitKey()
    # cv2.imwrite('2.jpg', img_dot)
    mask = cv2.imread('3.jpg', 0)
    a, img_dot = cv2.threshold(mask, 190, 255, cv2.THRESH_BINARY)
    # cv2.imshow('', img_dot)
    # cv2.waitKey()

    dst = cv2.inpaint(img,img_dot,3,cv2.INPAINT_TELEA)

    cv2.imshow('dst',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test2():
    # -*- coding: utf-8 -*-
    import cv2
    import numpy

    src = cv2.imread('11.jpg')
    mask = cv2.imread('3.jpg')
    # src = cv2.resize(src, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    # mask = cv2.resize(mask, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    save = numpy.zeros(src.shape, numpy.uint8)  # 创建一张空图像用于保存

    for row in range(src.shape[0]):
        for col in range(src.shape[1]):
            for channel in range(src.shape[2]):
                if mask[row, col, channel] == 0:
                    val = 0
                else:
                    reverse_val = 255 - src[row, col, channel]
                    val = 255 - reverse_val * 256 / mask[row, col, channel]
                    if val < 0: val = 0
                save[row, col, channel] = val

    cv2.imshow('src', src)
    cv2.imshow('mask', mask)
    cv2.imshow('save', save)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test2()