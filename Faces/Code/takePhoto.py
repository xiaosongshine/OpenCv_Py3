import cv2



cam = cv2.VideoCapture(0)
count = 0
while True:
    ret, img = cam.read()
    if ret == False:
        print("Read cam error")
        break
    imag = cv2.resize(img,(400,300))
    image = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Ori", img)
    cv2.imshow("deal1", imag)
    cv2.imshow("deal2", image)

    if (cv2.waitKey(1) & 0xff == ord("p")):
        count += 1
        cv2.imwrite("../att_faces/ss/"+str(count)+".jpg", image)
        print("Take photo %d" % count)
        continue

    if(cv2.waitKey(1) & 0xff == ord("q")):
        print("quit cam")
        break


    pass

cv2.destroyAllWindows()
print("colse all windows")
