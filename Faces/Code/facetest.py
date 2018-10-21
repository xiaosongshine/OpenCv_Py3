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

for i in range(1):
    path.append("../att_faces/ss/"+str(i+1)+".jpg")
    image.append(cv2.imread(path[i]))

    # 探测图片中的人脸
    print(image[i].shape)

    faces = face_cascade.detectMultiScale(

        image[i],

        scaleFactor=1.2,

        minNeighbors=3,

        minSize=(5, 5)

    )

    #print("photo"+str(i+1)+":发现{0}个人脸!".format(len(faces)))
    imgcp = image[i].copy()
    for (x, y, w, h) in faces:
        # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

        cv2.rectangle(image[i], (x, y), (x + w, y + h), (0, 255, 0), 2)

    xii,yii = int((x + w//2)*0.67),int((y+h//2)*0.67)

    imgcp = cv2.resize(imgcp, None, fx=0.67, fy=0.67)

    cv2.imshow("win",image[i])
    cv2.waitKey(0)

    xi2, yi2 = imgcp.shape[:2]

    xi, yi = xi2//2-6 , yi2//2 + 8


    facees.append(imgcp[yii-56:yii+56, xii-46:xii+46])

    print(facees[i].shape)
    ##cv2.imwrite("../att_faces/s0/"+str(i+1)+".png", facees[i])



#cv2.imshow("Faces!", facees[0])
#cv2.waitKey(0)

cv2.destroyAllWindows()
