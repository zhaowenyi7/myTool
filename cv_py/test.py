import cv2
import numpy as np

if __name__ == '__main__':
    psd_img_01 = cv2.imread('F:\\test\\2019-07-01-08-37-40-884.bmp', cv2.IMREAD_COLOR)
    psd_img_02 = cv2.imread('F:\\test\\2019-07-01-08-37-40-884.bmp', cv2.IMREAD_COLOR)
    lenx = psd_img_02.shape[1]
    leny = psd_img_02.shape[0]
    psd_img_01 = psd_img_01[:, int(lenx/2):]
    psd_img_02 = psd_img_02[:, int(lenx/2) - 60:lenx - 60]
    cv2.imwrite("../file_dir/left.bmp", psd_img_02)
    cv2.imwrite("../file_dir/right.bmp", psd_img_01)

    psd_img_1 = cv2.cvtColor(psd_img_01, cv2.COLOR_RGB2GRAY)
    psd_img_2 = cv2.cvtColor(psd_img_02, cv2.COLOR_RGB2GRAY)

    y0 = 1400
    y1 = 2000
    x0 = 1044
    x1 = 1644

    roiImg = psd_img_2[y0:y1, x0:x1]
    temp_img = np.zeros((psd_img_2.shape[0], psd_img_2.shape[1]), np.uint8)
    temp_img[y0:y1, x0:x1] = roiImg
