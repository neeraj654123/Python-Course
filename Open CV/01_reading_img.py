from cv2 import destroyAllWindows
import cv2

img=cv2.imread('C:/Users/asus/OneDrive/Pictures/asus.jpg',1)
cv2.imshow('window',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()