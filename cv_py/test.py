import cv2
import numpy as np


if __name__ == '__main__':
    img = np.array([
        [0, 255, 0, 0],
        [0, 0, 0, 255],
        [0, 0, 0, 255],
        [255, 0, 0, 0],
        [255, 0, 0, 0]

    ], np.uint8)
    # cv2.imshow("1", img)
    # cv2.waitKey()
    cv2.getStructuringElement()

    _, labels = cv2.connectedComponents(img)
    print(1)
