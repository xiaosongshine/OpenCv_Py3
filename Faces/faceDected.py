# coding:utf-8

#    __author__ = '郭 璞'

#    __date__ = '2016/9/5'

#    __Desc__ = 人脸检测小例子，以圆圈圈出人脸

import cv2

# 待检测的图片路径

imagepath = r'beauty.jpg'

# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# 读取图片

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    image = frame

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸

    faces = face_cascade.detectMultiScale(

        gray,

        scaleFactor=1.15,

        minNeighbors=5,

        minSize=(5, 5)

    )

    #print("发现{0}个人脸!".format(len(faces)))

    for (x, y, w, h) in faces:
        # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Faces!", image)

    print("x,y: %d,%d " % (x+w//2, y+h//2))

    if(cv2.waitKey(100) & 0xff == ord("q")):

        cv2.imwrite("ptoho1.jpg", frame)
        break

cv2.destroyAllWindows()
