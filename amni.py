import cv2 as cv

def mouse_event(event,x,y,flag,pram):
    if event==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),x+20,(250,225,225),-1)

