import cv2

import time

import tinys3

import sys

from Tkinter import *

import sys

import boto3

conn = tinys3.Connection('AKIAJYLBEXSSEFJBCNHA','sxaBTWJ2lXJcFRM9sVUxL2ToWCbUxhTkLJNRTJfw',tls=True)

cv2.namedWindow("Preview")
vc=cv2.VideoCapture(1)

#cap=cv2.VideoCapture(0)
if vc.isOpened():
	rval,frame=vc.read()
	
else:
	rval=False
p=0


while rval:
	global i
	file=open("akki.txt","r")
	outfile=file.read(-1)
	i=int(outfile)+1
	#print(i)
	file.close()
	file=open("akki.txt","w")
	infile=file.write(str(i))
	file.close()

	cv2.imshow("preview",frame)
	rval,frame=vc.read()
        time.sleep(1)
        p=p+1
	n=str(i)+'.jpg'
        cv2.imwrite(n,frame)
	key=cv2.waitKey(20)
	f = open(n,'rb')
	conn.upload(n,f,'swarnam')
	time.sleep(1)
	if __name__ == "__main__":
    		fileName=n
    		bucket='swarnam'
    
    		client=boto3.client('rekognition','eu-west-1')

    		response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})
  
    		b='Finger'
    		print('Detected labels for ' + fileName)    
    		for label in response['Labels']:
       # print (label['Name'])
        		a=(label['Name'])
			a=a.rstrip()

			print a
			if(a == b):
				print('intruder detected')
				def clickAbout(): 
    					name = ("Thanks for the click")
   					return
				app = Tk()
				app.title("SOME INTRUDER DETECTED")
				app.geometry("500x300+200+200")
				labelText = StringVar()
				labelText.set ("Please check the image number provided below\n as some human is detected in the image")
				labelText2 = StringVar()
				labelText2.set(n)
				label1 = Label(app, textvariable=labelText, height=0, width=100)
				label1.pack()

				label1 = Label(app, textvariable=labelText2, height=0, width=100)
				label1.pack()
				b = Button(app, text="Quit", width=20, command=app.destroy)
				b.pack(side='bottom',padx=0,pady=0)
				app.mainloop()
	if key==27:
		break
	if p==2:
	  sys.exit()

cv2.destroyWindow("preview")
vc.release()
