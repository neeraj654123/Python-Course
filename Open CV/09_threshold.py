import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
threshold_val=100
_,binary_thresh = cv2.threshold(img,threshold_val,255,cv2.THRESH_BINARY)
cv2.imshow('Original image',img)
cv2.imshow('Binary threshold image',binary_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows() 