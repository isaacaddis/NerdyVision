import numpy as np
import argparse 
import cv2
__author__ = "Isaac Addis"

parser = argparse.ArgumentParser(description='Lowkey do vision')
parser.add_argument('-l','--l', type = list, help = 'Lower bound')
parser.add_argument('-u','--u', type = list, help = 'Upper bound')
args = parser.parse_args()
#Video stream (webcam)
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = args.l
    upperBound = args.u
    for(lower, upper) in boundaries:
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")
    	mask = cv2.inRange(hsv, lower, upper)
    	output = cv2.bitwise_and(frame,frame,mask=mask)
    	cv2.imshow('Super Cool Vision Box',np.hstack([frame,output]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
