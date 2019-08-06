import cv2
import numpy as np

# from psd_tools import PSDImage

"""https://blog.csdn.net/g11d111/article/details/79925827
https://blog.csdn.net/xq920831/article/details/86715186
"""
# 1) psd to png
# psd1 = PSDImage.load('200x800.ai.psd')
# psd1.as_PIL().save('psd_image_to_detect1.png')
#
# psd2 = PSDImage.load('800x200.ai.psd')
# psd2.as_PIL().save('psd_image_to_detect2.png')
# 2) 以灰度图的形式读入图片

psd_img_1 = cv2.imread('F:\\test1.bmp', cv2.IMREAD_GRAYSCALE)
psd_img_2 = cv2.imread('F:\\test1.bmp', cv2.IMREAD_GRAYSCALE)

# 3) SIFT特征计算
# sift = cv2.xfeatures2d.SIFT_create()
# psd_kp1, psd_des1 = sift.detectAndCompute(psd_img_1, None)
# psd_kp2, psd_des2 = sift.detectAndCompute(psd_img_2, None)

# 3-2) SURF试验
SURF = cv2.xfeatures2d_SURF.create()
psd_kp1, psd_des1 = cv2.xfeatures2d_SURF.detectAndCompute(SURF, psd_img_1, None)
psd_kp2, psd_des2 = cv2.xfeatures2d_SURF.detectAndCompute(SURF, psd_img_2, None)

bf = cv2.BFMatcher_create(crossCheck=True)
matches = bf.match(psd_des1, psd_des2)
matches = sorted(matches, key=lambda x: x.distance)

img_out = cv2.drawMatches(psd_img_1, psd_kp1, psd_img_2, psd_kp2, matches[:15], None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
img_out = cv2.resize(img_out, None, fx=0.25, fy=0.25)

cv2.imshow('no FLANN', img_out)  # 展示图片
cv2.waitKey(0)  # 等待按键按下
cv2.destroyAllWindows()  # 清除所有窗口
