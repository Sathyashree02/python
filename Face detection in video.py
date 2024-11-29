import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg) #Loading algorithm

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read() #Reading the frame FRM CAM
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color image to gray
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 9)  #Getting coordinates
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("FaceDetection", img)

    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
