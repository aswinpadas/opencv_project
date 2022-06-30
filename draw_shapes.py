from builtins import int

import cv2


image = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_project/duck.png',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),3)
cv2.circle(image,(200,200),200,(0,0,255),-1)
cv2.circle(image,(200,200),100,(0,255,0),-1)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(image,'hello',(200,200),font,2,(255,255,255),cv2.LINE_AA)


cv2.imshow('shapes',image)
cv2.waitKey(0)