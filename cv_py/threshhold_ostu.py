import cv2
import numpy


if __name__ == '__main__':
    image = cv2.imread("2019-07-01-08-38-45-789.bmp")
    image = cv2.resize(image, None, fx=0.25, fy=0.25)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 方法选择为THRESH_OTSU
    cv2.imshow('', th1)
    cv2.waitKey()
    cv2.imwrite('threshhold_ostu.jpg', th1)

