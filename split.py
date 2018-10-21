import cv2
import numpy as np
import tensorflow as tf

print(tf.__version__)


img = cv2.imread("image/Demo1.jpg")

row, lo, canl = img.shape

b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]
#r = np.ones(shape=(row, lo),dtype=img.dtype)
img2 = cv2.merge(mv=[b, g, r])
cv2.imshow("ori", img)
cv2.imshow("B", b)
cv2.imshow("merge", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
