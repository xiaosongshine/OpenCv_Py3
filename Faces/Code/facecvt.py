# coding:utf-8

#    __author__ = '郭 璞'

#    __date__ = '2016/9/5'

#    __Desc__ = 人脸检测小例子，以圆圈圈出人脸

import cv2

# 待检测的图片路径


# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# 读取图片
NUM = 20

path = []
image = []
facees = []

for i in range(11):
    path.append("WJJ/wjj"+str(i+1)+".jpg")
    image.append(cv2.imread(path[i]))

    # 探测图片中的人脸
    print(image[i].shape)

    faces = face_cascade.detectMultiScale(

        image[i],

        scaleFactor=1.3,

        minNeighbors=5,

        minSize=(5, 5)

    )

    #print("photo"+str(i+1)+":发现{0}个人脸!".format(len(faces)))
    imgcp = image[i].copy()
    for (x, y, w, h) in faces:
        # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

        cv2.rectangle(image[i], (x, y), (x + w, y + h), (0, 255, 0), 2)






    facees.append(imgcp[y:y+h, x:x+w])

    print(facees[i].shape)
    cv2.imwrite("../att_faces/s2/"+str(i+1)+".jpg", facees[i])



#cv2.imshow("Faces!", facees[0])
#cv2.waitKey(0)

cv2.destroyAllWindows()
