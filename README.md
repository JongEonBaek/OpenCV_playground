# OpenCV Video Recorder

이 프로그램은 OpenCV를 활용하여 웹캠 영상을 실시간으로 화면에 표시하고, 녹화할 수 있는 간단한 비디오 레코더입니다.  
추가적으로 **Flip(좌우 반전) 기능**이 포함되어 있으며, 키보드를 통해 기능을 조작할 수 있습니다.

---

## 🎥 **기능**
- **카메라 영상 실시간 출력** (`cv.VideoCapture`)
- **비디오 녹화 (`cv.VideoWriter`)**
- **녹화 중 빨간색 원(`REC`) 표시**
- **`Space` 키를 눌러 녹화 시작/중지 가능**
- **`F` 키를 눌러 좌우 반전(Flip) 가능**
- **`ESC` 키를 눌러 프로그램 종료**

---

## 🔧 **설치 및 실행 방법**
### 1️⃣ **필요한 라이브러리 설치**
이 프로그램은 **Python**과 **OpenCV**를 사용합니다.  

### 2️⃣ **프로그램 실행**
아래 명령어를 실행하면 프로그램이 실행됩니다.

```bash
python main.py
```

---

## 🎮 **사용법**
| 키 | 기능 |
|----|------|
| `Space` | 녹화 시작 / 중지 |
| `F` | 화면 좌우 반전 (Flip) |
| `ESC` | 프로그램 종료 |

---

## 🛠️ **코덱 및 설정**
- **코덱(FourCC):** `XVID` 사용
- **파일 형식:** `AVI`
- **기본 해상도:** `640x480`
- **프레임 속도(FPS):** `30`

---

## 📄 **코드 설명**
```python
import cv2 as cv # OpenCV 라이브러리 불러오기

cap = cv.VideoCapture(0, cv.CAP_DSHOW) 웹캠을 열고 비디오 캡처
fourcc = cv.VideoWriter_fourcc(*'XVID') # XVID 코덱 설정
out = cv.VideoWriter('recorded_video.avi', fourcc, 30.0, (640, 480)) # 녹화 파일 설정 (FPS: 30, 해상도: 640x480)

is_recording = False # 녹화 여부
is_flipped = False   # 좌우 반전 여부

while True:
    ret, frame = cap.read() # 프레임을 가져오기
    if not ret:
        break # 프레임을 가져올 수 없으면 종료

    if is_flipped:
        frame = cv.flip(frame, 1)  # 좌우 반전 적용

    if is_recording:
        out.write(frame) # 녹화 중이면 프레임 저장
        cv.circle(frame, (30, 30), 10, (0, 0, 255), -1) # 녹화 중임을 나타내는 빨간색 원 표시

    cv.imshow('Video Recorder', frame) # 현재 프레임을 화면에 표시

    key = cv.waitKey(1) & 0xFF # 키 입력 감지
    if key == 27: # ESC 키를 누르면 종료
        break
    elif key == 32: # Space 키를 누르면 녹화 상태 토글 (ON/OFF)
        is_recording = not is_recording
    elif key == ord('f'):  # 'F' 키를 누르면 좌우 반전 토글 (ON/OFF)
        is_flipped = not is_flipped

# 자원 해제 및 프로그램 종료
cap.release()
out.release()
cv.destroyAllWindows()
```

---


https://github.com/user-attachments/assets/3584b33b-114f-484a-bcf2-c474bdf227d2




