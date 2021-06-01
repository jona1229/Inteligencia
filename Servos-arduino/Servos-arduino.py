import cv2
import numpy as np
import serial
import time
ser = serial.Serial('COM5',9600)
cap = cv2.VideoCapture(0)

while True:
    
    
	_,frame = cap.read() 
    #time.sleep(3)
    #background = 0
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	grayImage=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Red color
    #Green color
    #low_green = np.array([25, 52, 72])
    #high_green = np.array([102, 255, 255])
    #green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    #green = cv2.bitwise_and(frame, frame, mask=green_mask)
    #low_red = np.array([161, 155, 84])
    #high_red = np.array([179, 255, 255])
    #red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    #red = cv2.bitwise_and(frame, frame, mask=red_mask)
    #Blue color
	low_blue = np.array([94,80,2])
	high_blue = np.array([126,255,255])
	height = frame.shape[0]
	width = frame.shape[1]
	channels = frame.shape[2]
    #cv2.imshow("Blue", blue)
	largo=height/3
	ancho=width/3
	
	output=frame.copy()
    
	circles=cv2.HoughCircles( grayImage,cv2.HOUGH_GRADIENT,2,4000, param1=50,param2=30,minRadius=40, maxRadius=90)
	circles=np.uint16(np.around(circles))
	for circuloActual in circles[0,:]:
		centroX=circuloActual[0]
		centroY=circuloActual[1]
		radio=circuloActual[2]
		cv2.circle(output,(centroX,centroY),radio,(50,255,50),2)
	cv2.imshow('Video',output)
	movx=int(centroX)-int(ancho)
	movy=int(centroY)-int(largo)
	if(movx<=0):
		ser.write(b'L')
		time.sleep(1)
	else:
		if(movx>=0):
			ser.write(b'R')
			time.sleep(1)
		else:
			ser.write(b' ')
			time.sleep(1)
	if(movy<=0):
		ser.write(b'U')
		time.sleep(1)
	else:
		if(movx>=0):
			ser.write(b'D')
			time.sleep(1)
		else:
			ser.write(b' ')
			time.sleep(1)
	tecla = cv2.waitKey(5) & 0xFF
	if tecla == 27:
		break
	 
mask = cv2.inRange( hsv_frame, low_blue, high_blue)
cv2.imshow("Frame",frame)
cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()