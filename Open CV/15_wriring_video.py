import cv2

video=cv2.VideoCapture('C:/Users/asus/OneDrive/Desktop/bird.mp4')
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
output=cv2.VideoWriter('output.mp4',fourcc,30.0,(800,600),True)
while video.isOpened():
    ret,frame=video.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    else:
        break
video.release()
output.release()
cv2.destroyAllWindows()
