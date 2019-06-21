import numpy as np
import cv2
from pygame import mixer

static_back = None
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    motion = 0
##  frame = cv2.GaussianBlur(frame, (21,21), 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if static_back is None: 
        static_back = gray 
        continue
    diff_frame = cv2.absdiff(static_back, frame)

    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(),  
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts: 
        if cv2.contourArea(contour) < 10000: 
            continue
        motion = 1
  
        (x, y, w, h) = cv2.boundingRect(contour) 
        # making green rectangle arround the moving object 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        

    
    
    
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    if  motion == 1:
        mixer.init()
        mixer.music.load("D:\Shubham\Python Program\Open CV Projects\Open_CV_Projects\Media\Biba.mp3")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
