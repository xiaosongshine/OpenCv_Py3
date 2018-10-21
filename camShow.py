
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    print(ret)

    cv2.imshow("capture1", frame)

    if(cv2.waitKey(1) & 0xff == ord("q")):

        cv2.imwrite("ptoho1.jpg", frame)

        break

cap.release()
cv2.destroyAllWindows()
