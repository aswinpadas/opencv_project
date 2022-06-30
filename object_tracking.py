import cv2
import numpy as np


image = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_project/shapes.png', 1)
cv2.imshow('original image',image)
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image',new_image)


lower_bound =np.array([110,50,50])
upper_bound = np.array([130,252,252])
mask = cv2.inRange(new_image,lower_bound,upper_bound)
cv2.imshow('mask',mask)

result = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()