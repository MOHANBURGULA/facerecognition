# pip install opencv-python
# for the face the library is used
# haarcascade_frontalface_default.xml
# from platform import release


import cv2
import opencv

# Load face cascade from OpenCV's built-in data
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

    cv2.imshow('Face Detection', frame)

    key = cv2.waitKey(40) & 0xFF
    if key == 40:  # Press Down Arrow key to quit
        break

video_capture.release()
cv2.destroyAllWindows()
