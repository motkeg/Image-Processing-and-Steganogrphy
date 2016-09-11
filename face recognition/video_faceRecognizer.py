
import numpy as np
import cv2
from Tkinter import *
import tkFileDialog as fd


def videoCpture():
    "--------------------------------------------------------------------"

    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    "----------------------------------------------------------------------"
    #choose file from your computer
    
    '''root2 = Tk()
    root2.title("Select video to detact")
    root2.withdraw()
    file_path = fd.askopenfilename()
    video_capture = cv2.VideoCapture(file_path)'''
    
    video_capture = cv2.VideoCapture("face.mp4")
    while video_capture.isOpened():
        # Capture frame-by-frame
        ret,frame = video_capture.read()
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
   
            cv2.imshow('calculating...',frame)
    

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

        # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
        





#videoCpture()    
#test()