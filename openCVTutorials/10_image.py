import cv2 as cv

# Check the version:
print(cv.__version__)

img = cv.imread("photo/photoOne.jpeg")
image = cv.imread("photo/photoOne.jpeg", cv.IMREAD_GRAYSCALE)
cv.imshow("output", img)

# wait 2 second
cv.waitKey(2000)

cv.imshow("outputTwo", image)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()
