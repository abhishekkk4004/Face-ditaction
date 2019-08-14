import cv2

# For finding face
def find_mouth(img):
    # For finding face
    casscade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    casscade1 = cv2.CascadeClassifier("haarcascade_eye.xml")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = casscade.detectMultiScale(gray_img , scaleFactor=4, minNeighbors=5)
    eyes = casscade1.detectMultiScale(gray_img, scaleFactor=9,minNeighbors=2,)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    for x,y,w,h in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return cv2.imshow("Face and eyes",img)


def takeFrame(img):
    while True:
        ret, frame = img.read()
        find_mouth(frame)
        if cv2.waitKey(1) == 13:
            break


frame = cv2.VideoCapture(0)
takeFrame(frame)
frame.release()
cv2.destroyAllWindows()