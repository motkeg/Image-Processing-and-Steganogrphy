import cv2
import sys,os
import numpy as np

"--------------------------------------------------------------------"

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

"----------------------------------------------------------------------"
video_capture = cv2.VideoCapture(0)
 
while True:
    # Capture frame-by-frame
    #ret =video_capture.set(3,240)
    #ret = video_capture.set(4,240)
    ret, frame = video_capture.read()
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
   
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
