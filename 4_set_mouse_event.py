import cv2
import cv2 as cv
import numpy as np


# Draw circle using setMouseEvent()

def mouse_event(event, x, y, flag, pram):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), x + 50, (255, 0, 255), -1)


img = np.zeros((512, 512, 3), dtype=np.int8)
cv.namedWindow("OUTPUT")
cv.setMouseCallback("OUTPUT", mouse_event)

while True:
    cv.imshow("OUTPUT", img)
    if cv2.waitKey(0) == ord('q'):
        break
cv.destroyAllWindows()

