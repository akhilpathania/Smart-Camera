import cv2

cap=cv2.VideoCapture(0)#Pass '0' to access default WebCam

while(True):
    
    f,frame=cap.read()
    frame=cv2.resize(frame,(640,480)) 
    cv2.imshow('Video',frame)
    ch=cv2.waitKey(20)
    
    if ch==27:
        break

cap.release()

cv2.destroyAllWindows()