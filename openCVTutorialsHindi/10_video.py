import cv2 as cv

cap = cv.VideoCapture(r'photo/test_video.mp4')

if not cap.isOpened():
    print("Can't open the camera.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    fps = cap.get(cv.CAP_PROP_FPS)
    print(f"height:{height} \n width:{width} \n fps:{fps}")
    if not ret:
        print("video is finished . . . ")
        break
    frame = cv.resize(frame, (720, 480))
    cv.imshow("output", frame)
    if cv.waitKey(1) == ord('q'):
        print("exiting . . .")
        break
cap.release()
cv.destroyAllWindows()
