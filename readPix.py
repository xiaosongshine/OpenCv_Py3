

import cv2

img = cv2.imread("image/Demo1.jpg")

p = img[100, 100]

print(p)
img[100, 100] = [0, 0, 0]
while(True):
    cv2.imshow("Demo1", img)
    if(cv2.waitKey(1) & 0xff == ord("q")):
        break

cv2.destroyAllWindows()
