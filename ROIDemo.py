import cv2
import numpy as np

img = cv2.imread("image/Demo1.jpg")

head = np.ones(shape=(100, 100, 3))

head = img[200: 300, 200: 300]

img[:100, :100] = head

cv2.imshow("ori", img)
cv2.imshow("head", head)
cv2.waitKey(0)
cv2.destroyAllWindows()