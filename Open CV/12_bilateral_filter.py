import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
resize = cv2.resize(img,(400,400))
d=7
sigmaColor=100
sigmaSpace=100
bilateral = cv2.bilateralFilter(resize,d,sigmaColor,sigmaSpace)
cv2.imshow('Resize image',resize)
cv2.imshow('Bilateral filter image',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows() 