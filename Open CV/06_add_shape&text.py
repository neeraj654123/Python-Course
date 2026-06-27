import cv2
import numpy as np 

img=cv2.imread('C:/Users/asus/OneDrive/Desktop/traffic.jpg',cv2.IMREAD_COLOR)
# img =np.zeros((512,512,3),np.uint8)
cv2.line(img,(100,100),(200,200),(0,0,255),2)
cv2.rectangle(img,(100,100),(200,200),(0,0,255),2)
cv2.circle(img,(100,100),200,(0,0,255),3)
cv2.ellipse(img, (500, 250), (100, 50), 0, 0, 360, (0, 0, 255), 3)
pts= np.array([[100,50],[100,300],[500,50]],np.int32)
cv2.polylines(img,[pts],isClosed=True,color=(0,255,255),thickness=2)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'BMW',(10,100),fontFace=font,fontScale=3,color=(220,255,255),thickness=8,lineType=cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
