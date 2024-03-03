import cv2 as cv

# Read the video
cap = cv.VideoCapture("photo/test_video.mp4")
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv.CAP_PROP_FPS)

# Create fourcc for save the video
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter("./saveAsset/output.avi", fourcc,fps, (720, 480))

if not cap.isOpened():
    print("can't open the camera . . .")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("video is finished . . . ")
        break
    frame = cv.resize(frame, (720, 480))
    cv.imshow("output", frame)
    writer.write(frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
