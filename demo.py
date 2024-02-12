import cv2 as cv

img = cv.imread("assest/python.jpg")

img_size = cv.resize(img,(600,400))

cv.imshow("demo windows",img_size)

k = cv.waitKey(0)

if k==ord('q'):
    cv.destroyAllWindows()

