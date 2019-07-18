# coding=utf-8
import cv2
import numpy as np

"""http://zhaoxuhui.top/blog/2018/05/18/OpenCV_Contrib.html"""
# 读取图像
img0 = cv2.imread("E:\\data\\001test\\WIN.jpg")

# 创建对象
# 对于SIFT算子，可以通过nFeatures属性控制特征点数量
# 对于SURF算子，可以通过hessianThreshold属性控制特征点数量
# 更详细的用法见OpenCV官方API文档
SIFT = cv2.xfeatures2d_SIFT.create()
SURF = cv2.xfeatures2d_SURF.create()

# 提取特征并计算描述子
kps, des = cv2.xfeatures2d_SIFT.detectAndCompute(SIFT, img0, None)
kps2, des2 = cv2.xfeatures2d_SURF.detectAndCompute(SURF, img0, None)

# 新建一个空图像用于绘制特征点
img_sift = np.zeros(img0.shape, np.uint8)
img_surf = np.zeros(img0.shape, np.uint8)

# 绘制特征点
cv2.drawKeypoints(img0, kps, img_sift)
cv2.drawKeypoints(img0, kps2, img_surf)

# 展示
cv2.imshow("img", img0)
cv2.imshow("sift", img_sift)
cv2.imshow("surf", img_surf)
cv2.waitKey(0)
