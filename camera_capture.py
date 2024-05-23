import cv2
import os
import time

def capture_image(event, queue):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        event.wait()
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        timestamp = int(time.time())
        img_name = f"static/images/opencv_frame_{timestamp}.png"
        cv2.imwrite(img_name, frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            message = "You look awesome!"
        else:
            message = "Why are you hiding?"

        queue.put(('image', img_name, message))
        img_counter += 1
        event.clear()

    cam.release()
