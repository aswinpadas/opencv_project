import cv2

image = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_project/sunflower.jpg', 1)
print(image)
cv2.imshow('image', image)
cv2.waitKey(10000)
cv2.imwrite('C:/Users/aswin/PycharmProjects/opencv_project/sunflower.png', image)
cv2.destroyAllWindows()
