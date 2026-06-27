import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
resize = cv2.resize(img,(400,400))
kernel=5
median =cv2.medianBlur(resize,ksize=kernel)
cv2.imshow('Resize image',resize)
cv2.imshow('Median blur image',median)
cv2.waitKey(0)
cv2.destroyAllWindows()