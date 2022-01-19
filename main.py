import cvzone
from cv2 import cv2
cap= cv2.VideoCapture(0) #to start capturing video
cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #used for face detection on greyscale

print("Which sticker you want press the number")
print(" 1 = beard \n 2 = cool \n 3 = native \n 4 = pirate \n 5= star glasses  \n 6 = sunglasses")
selected = int(input())

if(selected ==1):
    overlay =cv2.imread('beard.png', cv2.IMREAD_UNCHANGED)
elif(selected==2):
    overlay = cv2.imread('cool.png', cv2.IMREAD_UNCHANGED)
elif(selected==3):
    overlay = cv2.imread('native.png', cv2.IMREAD_UNCHANGED)
elif(selected==4):
    overlay = cv2.imread('pirate.png', cv2.IMREAD_UNCHANGED)
elif(selected==5):
    overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
elif(selected==6):
    overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
else:
    print("Wrong Input")
    exit(0)
while True:
    _, frame = cap.read() #read the video data
    gray_scale =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # creating video frame to gray scale (b/w) so that face detection is easy
    faces =cascade.detectMultiScale(gray_scale) #decides faces in frame
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #shows rectangle on faces. (given frame, x, y coordinates, w, h height width 0,255,0 is color of rectangle and 2 is thickness
        overlay_resize= cv2.resize(overlay, (int(w*1.8),int(h*1.9))) # resizing and adjusting sticker on face
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75]) # placing sticker on face
    cv2.imshow('Snap Chat', frame) #shows frame
    if cv2.waitKey(10) == ord('q'):
        break


