import glob
import cv2

file_directory = 'E:\\data\\0719-200-right'
file_type = '.bmp'
if __name__ == '__main__':
    file_name_list = glob.glob(file_directory + '/*' + file_type)
    img = cv2.imread(file_name_list[0])
    img = cv2.resize(img, None, fx=0.1, fy=0.1)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    # if cv2.waitKey(1) & 0xff == 27:
    #     # cv2.destroyAllWindows()
    #     break
