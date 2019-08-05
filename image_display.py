import glob
import cv2


file_directory = 'E:\\data\\0719-200-left'
file_type = '.bmp'
if __name__ == '__main__':
    file_name_list = glob.glob(file_directory + '/*' + file_type)
    for index in range(len(file_name_list)):
        img = cv2.imread(file_name_list[index])
        img = cv2.resize(img, None, fx=0.25, fy=0.25)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xff == 27:
            # cv2.destroyAllWindows()
            break
    cv2.destroyAllWindows()
    cap = cv2.VideoCapture(0)
    cap.set(3, 160)
