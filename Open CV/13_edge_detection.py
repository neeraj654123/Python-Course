import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
resize = cv2.resize(img,(400,400))
min_thresh=100
max_thresh=200
edge = cv2.Canny(resize,min_thresh,max_thresh)
cv2.imshow('Original image',resize)
cv2.imshow('Edge image',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()