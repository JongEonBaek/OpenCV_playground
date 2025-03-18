import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('recorded_video.avi', fourcc, 30.0, (640, 480))  # FPS를 30으로 조정

is_recording = False
is_flipped = False  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if is_flipped:
        frame = cv.flip(frame, 1)  

    if is_recording:
        out.write(frame)
        cv.circle(frame, (30, 30), 10, (0, 0, 255), -1)

    cv.imshow('Video Recorder', frame)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 32:
        is_recording = not is_recording
    elif key == ord('f'):
        is_flipped = not is_flipped  

cap.release()
out.release()
cv.destroyAllWindows()
