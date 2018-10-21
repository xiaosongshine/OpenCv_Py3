import cv2
import numpy as np

bmp = cv2.imread("image/girl.bmp", cv2.IMREAD_UNCHANGED)
print(bmp.shape)
cv2.imshow("bmp0", bmp)
bmp[200:300, 200:300, 0:3] = [255, 255, 255]
cv2.imshow("bmp1", bmp)
#cv2.imshow("bmp", bmp)

cv2.waitKey(0)
cv2.destroyAllWindows()
