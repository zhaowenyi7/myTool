# -*- coding:utf-8 -*-

import numpy as np
import cv2
import config

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(threeD[y][x])


def BM_update(val=0):
    # 两个trackbar用来调节不同的参数查看效果
    global threeD
    global BM_num
    global blockSize

    BM_num = cv2.getTrackbarPos("num_disp", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    if BM_num < 1:
        BM_num = 1
    num_disp = BM_num * 16
    stereo.setNumDisparities(num_disp)
    stereo.setBlockSize(blockSize)
    print('computing SGBM_disparity...')

    disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离, 世界坐标系的原点是左摄像头凸透镜的光心
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., config.Q)

    cv2.imshow("depth", disp)
if __name__ == '__main__':

    y0 = 1400
    y1 = 2000
    x0 = 1044
    x1 = 1644
    down_size = 0.25
    # 从摄像头获取像素
    frame1 = cv2.imread('../file_dir/left.bmp')
    frame2 = cv2.imread('../file_dir/right.bmp')

    frame1 = cv2.rectangle(frame1, (x0, y0), (x1, y1), (0, 0, 200,), 7)
    frame2 = cv2.rectangle(frame2, (x0 - 60, y0), (x1 - 60, y1), (0, 0, 200,), 7)

    w = frame1.shape[1]
    h = frame1.shape[0]
    # joint_img = np.zeros((h, w * 2 + 1), np.int8)
    # joint_img[:, :int(w)] = frame1
    # joint_img[:, int(w) + 1:] = frame2

    image = np.concatenate([frame1, frame2], axis=1)

    # joint_img = cv2.cvtColor(joint_img, cv2.COLOR_BGR2GRAY)
    for i in range(y0, y1, 60):
        image = cv2.line(image, (x0, i), (w + x1 - 60, i), (0, 255, 0), 3)
    image = cv2.resize(image, None, fx=down_size, fy=down_size)
    cv2.imshow('01', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("../file_dir/out.bmp", image)
    # 从文件夹中获取图像进行校正，获取深度图
    # 根据更正map对图片进行重构, 使用标定后的双目矫正映射矩阵 矫正 左右相机图像
    # img1_rectified = cv2.remap(frame1, config.left_map1, config.left_map2, cv2.INTER_LINEAR)
    # img2_rectified = cv2.remap(frame2, config.right_map1, config.right_map2, cv2.INTER_LINEAR)

    frame1 = cv2.resize(frame1, None, fx=down_size, fy=down_size)
    frame2 = cv2.resize(frame2, None, fx=down_size, fy=down_size)
    img1_rectified = frame1
    img2_rectified = frame2

    cv2.imshow('left_rectified', img1_rectified)
    cv2.imshow('right_rectified', img2_rectified)
    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)



    blockSize = 5  # 一个匹配块的大小,大于1的奇数
    BM_num = 2
    # disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # # 将图片扩展至3d空间中，其z方向的值则为当前的距离, 世界坐标系的原点是左摄像头凸透镜的光心
    # threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., config.Q)

    cv2.namedWindow('depth')
    cv2.setMouseCallback("depth", callbackFunc, None)
    cv2.createTrackbar('blockSize', 'depth', blockSize, 21, BM_update)
    cv2.createTrackbar('num_disp', 'depth', BM_num, 20, BM_update)

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    stereo = cv2.StereoBM_create(numDisparities=16 * BM_num, blockSize=blockSize)


    BM_update()
    # cv2.imshow("depth", disp)
    cv2.waitKey(0)
