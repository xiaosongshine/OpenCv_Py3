
#import numpy as np
import cv2


img = cv2.imread("image/lena256.bmp", cv2.IMREAD_UNCHANGED)
print(img.dtype)

x = img.item(100, 100)
print(x)
img.itemset((100, 100), 255)
print(img.item(100, 100))
