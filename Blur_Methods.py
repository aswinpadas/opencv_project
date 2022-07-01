import cv2
import numpy as np


image = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_project/sample.jpg',1)
blur=cv2.blur(image,(5,5))\

gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('Blur Image : Method 1',blur)
cv2.imshow('Gaussian Blur  : Method 2',gaussian_blur)
cv2.waitKey(30000)
cv2.destroyAllWindows()