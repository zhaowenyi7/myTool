import time

import cv2
import cv2.aruco as aruco

dic = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
dp = aruco.DetectorParameters_create()
down_size = 0.25

if __name__ == '__main__':
    img = cv2.imread("2019-07-01-08-38-45-789.bmp")

    time_0 = time.time()
    src_small = cv2.resize(img, None, fx=down_size, fy=down_size, interpolation=cv2.INTER_AREA)
    corners_small, ids, rejected_img_points = aruco.detectMarkers(src_small, dic, None, None, dp)
    time_01 = time.time()
    print(ids, time_01 - time_0)

    time_1 = time.time()
    img2 = cv2.UMat(img)
    src_small2 = cv2.resize(img2, None, fx=down_size, fy=down_size, interpolation=cv2.INTER_AREA)
    # cv2.imshow("", src_small2)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    corners_small2, ids2, rejected_img_points2 = aruco.detectMarkers(src_small2, dic, None, None, dp)
    ids2mat = cv2.UMat.get(ids2)
    time_11 = time.time()
    print(ids2mat, time_11 - time_1)
