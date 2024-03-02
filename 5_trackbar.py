import cv2 as cv
import numpy as np


def nothing(x):
    pass


# create a blank image
img = np.zeros((512, 512, 3), dtype=np.int8)
cv.namedWindow('image')
# trackBar:
cv.createTrackbar("R", 'image', 0, 255, nothing)
cv.createTrackbar("G", 'image', 0, 255, nothing)
cv.createTrackbar("B", "image", 0, 255, nothing)

# create a on off switch
switch = "ON:1 \n OFF:0"
cv.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    cv.imshow("image", img)
    if cv.waitKey(1) == ord('q'):  # for realtime waitKey() parameter value should be 1:
        break
    r = cv.getTrackbarPos("R", 'image')
    g = cv.getTrackbarPos("G", 'image')
    b = cv.getTrackbarPos("B", 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()
