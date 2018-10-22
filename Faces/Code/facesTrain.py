import cv2

import numpy as np
import pandas as pd
faces = []
lables = []
datas = pd.read_csv("lables111.csv", header=None)
datan = np.array(datas)

for i in range(len(datan)):

    faces.append(datan[i][0])

for j in range(len(datan)):
    lables.append(datan[j][1])

print(type(faces))
print(type(lables))

recognizer = cv2.face.LBPHFaceRecognizer_create()
# 有可能是 recognizer = cv2.createLBPHFaceRecognizer()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

images = []

for k in range(len(faces)):
    imagetemp = cv2.imread(faces[k])
    imagetemp = cv2.cvtColor(imagetemp, cv2.COLOR_BGR2GRAY)
    #print((imagetemp).shape)
    image_np = imagetemp
    images.append(image_np)

    print(k)

recognizer.train(images, np.array(lables))
recognizer.save('trainner.yml')


#recognizer = cv2.face.LBPHFaceRecognizer_create()

"""
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()



recognizer.train(faces, np.array(ids))
recognizer.save('trainner/trainner.yml')

"""