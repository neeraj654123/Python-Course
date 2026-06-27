from cv2 import destroyAllWindows
import cv2

img=cv2.imread('C:/Users/asus/OneDrive/Pictures/asus.jpg')
print('dimensions of original image',img.shape)
img1=cv2.resize(img,(400,500))
print('dimensions of resized image',img1.shape)
# cv2.imshow('window',img)
cv2.imshow('resized image',img1)
cv2.imwrite('gray.jpg',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()