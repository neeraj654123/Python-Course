import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
column =img.shape[1]
row =img.shape[0]
center=(column/2,row/2)
angle=180
r =cv2.getRotationMatrix2D(center,angle,1)
rotated=cv2.warpAffine(img,r,(column,row))
cv2.imshow('Original image',img)
cv2.imshow('Rotated image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()