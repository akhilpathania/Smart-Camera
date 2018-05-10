import cv2
import time
cv2.namedWindow("Preview")
vc=cv2.VideoCapture(0)

#cap=cv2.VideoCapture(0)
if vc.isOpened():
	rval,frame=vc.read()
	
else:
	rval=False
i=0
while rval:
	cv2.imshow("preview",frame)
	rval,frame=vc.read()
        time.sleep(1)
        i=i+1
	n=str(i)+'.jpg'
        cv2.imwrite(n,frame)
	key=cv2.waitKey(20)
	if key==27:
		break

cv2.destroyWindow("preview")
vc.release()
		
