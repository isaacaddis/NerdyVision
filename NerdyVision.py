import numpy as np
import argparse 
import cv2
__author__ = "Isaac Addis"

#Video stream (webcam)
cap = cv2.VideoCapture(0)
while(687):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([40,20,20])
    upperBound = np.array([80, 220, 220])
    mask = cv2.inRange(hsv, lowerBound, upperBound)
    output = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('Super Cool Vision Box',np.hstack([frame,output]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
def findAllContours(image):
    print "lol"
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
