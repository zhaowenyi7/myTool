from PIL import Image
import numpy as np
import os
import cv2

img = cv2.imread('0507-107.tif')
# print(img)
cv2.imshow('1', img)
cv2.waitKey(0)
