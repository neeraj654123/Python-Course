import cv2


img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')

print('dimensions of original image',img.shape)
scale=50
width =int(img.shape[1]*scale/100)
height =int(img.shape[0]*scale/100)
dim=(width,height)

resized_img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('dimensions of resized image',resized_img.shape)
cv2.imshow('original image',img)
cv2.imshow('resized image',resized_img) 

cv2.waitKey(0)
cv2.destroyAllWindows()