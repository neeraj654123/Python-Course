import cv2

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg')
widht=600
height=550
dim =(widht,height)
resized=cv2.resize(img,dim)
# cv2.imshow('Original image',resized)
print('Size in bytes:',img.size)
flip=cv2.flip(resized,1)
# cv2.imshow('Flipped image 1',flip)

flip_1=cv2.flip(resized,0)
# cv2.imshow('Flipped image 2',flip_1)

flip_2= cv2.flip(resized,-1)
# cv2.imshow('Flipped image 3',flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()