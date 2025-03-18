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
import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('recorded_video.avi', fourcc, 30.0, (640, 480))

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
```
