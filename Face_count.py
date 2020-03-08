import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
count=0
data=0
while True:

    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(gray,1.1,5)

    count=len(face)

    #data=count+data

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow("frame",frame)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break
cap.release()
if len(face)==0:
    print("no face found!!!")
else:
    print("Number of faces detected: " + str(face.shape[0]))
cv2.destroyAllWindows()
#print(data)