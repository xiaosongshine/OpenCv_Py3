#code 1017 opencv2

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/Demo1.jpg")*1
print(type(img))
print(img.shape)

cv2.imshow("Demo1", img)

plt.hist(img.ravel(), 256)
plt.show()

#print(type(imsw))
cv2.waitKey()
cv2.destroyAllWindows()

