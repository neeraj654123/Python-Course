import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
resize = cv2.resize(img,(400,400))
gausian = cv2.GaussianBlur(resize,(5,5),5)
cv2.imshow('Resize image',resize)
cv2.imshow('Gaussian blur image',gausian)
cv2.waitKey(0)
cv2.destroyAllWindows()