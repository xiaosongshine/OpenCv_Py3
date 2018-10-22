import cv2

import numpy as np
import pandas as pd
facess = []
data = pd.read_csv("lables.csv")
datan = np.array(data)
print(type(datan[0]))



datas = pd.read_table("lables.csv",sep=",")
#print (data)
#print(datas)
print(type(datas))
faces = []
ids = []

#recognizer = cv2.face.LBPHFaceRecognizer_create()

"""
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()



recognizer.train(faces, np.array(ids))
recognizer.save('trainner/trainner.yml')

"""