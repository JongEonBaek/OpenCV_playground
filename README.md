# OpenCV를 활용한 간단한 비디오 녹화 프로그램입니다. Flip기능을 제공하며 Space를 통해 녹화를 실행, 일시정지하고 ESC를 통해 종료할 수 있습니다.

import cv2 as cv  # OpenCV 라이브러리 불러오기

# 웹캠을 열고 비디오 캡처
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# 비디오 저장을 위한 코덱 및 파일 설정
fourcc = cv.VideoWriter_fourcc(*'XVID')  # XVID 코덱 설정
out = cv.VideoWriter('recorded_video.avi', fourcc, 30.0, (640, 480))  # 녹화 파일 설정 (FPS: 30, 해상도: 640x480)

# 녹화 상태 및 좌우 반전 상태 초기화
is_recording = False  # 녹화 여부
is_flipped = False  # 좌우 반전 여부

while True:
    ret, frame = cap.read()  # 프레임을 가져오기
    if not ret:
        break  # 프레임을 가져올 수 없으면 종료

    if is_flipped:
        frame = cv.flip(frame, 1)  # 좌우 반전 적용

    if is_recording:
        out.write(frame)  # 녹화 중이면 프레임 저장
        cv.circle(frame, (30, 30), 10, (0, 0, 255), -1)  # 녹화 중임을 나타내는 빨간색 원 표시

    cv.imshow('Video Recorder', frame)  # 현재 프레임을 화면에 표시

    key = cv.waitKey(1) & 0xFF  # 키 입력 감지
    if key == 27:  # ESC 키를 누르면 종료
        break
    elif key == 32:  # Space 키를 누르면 녹화 상태 토글 (ON/OFF)
        is_recording = not is_recording
    elif key == ord('f'):  # 'F' 키를 누르면 좌우 반전 토글 (ON/OFF)
        is_flipped = not is_flipped  

# 자원 해제 및 프로그램 종료
cap.release()
out.release()
cv.destroyAllWindows()


