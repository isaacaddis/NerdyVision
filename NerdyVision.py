import numpy as np
import argparse 
import cv2
i = 1
j = 1
s = 0
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (i,j), s)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    boundaries = [
    	([17, 15, 100], [50, 56, 200]),
    	([86, 31, 4], [220, 88, 50]),
    	([25, 146, 190], [62, 174, 250]),
    	([103, 86, 65], [145, 133, 128])
    ]
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