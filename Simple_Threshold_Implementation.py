import cv2
image = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_project/gradient.jpg',1)
ret,thresh = cv2.threshold(image,125,255,cv2.THRESH_BINARY)
cv2.imshow('image',image)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()