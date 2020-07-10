#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time       : 2019/11/4 13:22
@Author     : WenyiZhao
@Descripion : 
@File       : npy_load.py
@Software   : PyCharm
"""
import numpy as np
import glob
import cv2
file_directory = 'F:/dataset/A_part1'
file_type = '.npy'
file_name_list = glob.glob(file_directory + '/*' + file_type)
for n in range(0, 10):
    c = np.load(file_name_list[n])
    c = cv2.resize(c, None, fx=0.4, fy=0.4)
    # cv2.imshow('', c)
    cv2.imwrite(file_name_list[n] + '.png', c)
    # if cv2.waitKey(1) & 0xff == 27:
    #     break
