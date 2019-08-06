# -*- coding:utf-8 -*-

'''
    存储双目相机标定参数
'''
import cv2
import numpy as np


#左摄像头参数
left_camera_matrix = np.array([[ 961.9777102685413, 0, 359.3694937020364],
                               [0, 963.0289170116566, 268.4365743952479],
                               [0, 0, 1]])
left_distortion = np.array([[0.0863893142462225, -0.2279292331475535, 0.001465888376839634, 0.0001941536455047409, 0]])

#右摄像头参数
right_camera_matrix = np.array([[966.8194296204734, 0, 298.392098004296],
                                [0, 967.6572256241711, 271.0356319993813],
                                [0, 0, 1]])

right_distortion = np.array([[0.0681946877009692, 0.00241295814845837, -0.000478616066889593, -0.00047737842536893, 0]])



R = np.array([[0.99999428234053789, 0.0026972654153306912, 0.0020396189624285648],
     [-0.0027020275730109725, 0.99999362178553286, 0.0023356873179831272],
     [-0.0020333059846775782, -0.0023411850699933427, 0.9999951922480631]])
T = np.array([-23.96263041776482, 0.05050823328778996, 0.2526111940936329])
size = (640, 480)# 图像尺寸

# 进行立体更正, bouguet标定方法
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion, right_camera_matrix, right_distortion, size, R, T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)