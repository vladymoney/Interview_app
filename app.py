import cv2
import os
import time
import threading
import queue
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from database import init_db, insert_data  # Ensure to import database functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

capture_queue = queue.Queue()
capture_event = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('mouse_click')
def handle_mouse_click(data):
    print(f"Mouse clicked at: {data}")
    insert_data('mouse_click', x=data['x'], y=data['y'])  # Insert mouse click data into the database
    capture_event.set()

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
        insert_data('image', image_path=img_name, message=message)  # Insert image capture data into the database
        img_counter += 1
        event.clear()

    cam.release()

def process_queue():
    while True:
        data = capture_queue.get()
        if data[0] == 'image':
            image_path = data[1]
            message = data[2]
            print(f"Emitting image_data event with image_path: /{image_path}")
            socketio.emit('image_data', {'image_path': '/' + image_path, 'message': message})

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts

    capture_thread = threading.Thread(target=capture_image, args=(capture_event, capture_queue))
    capture_thread.start()

    queue_thread = threading.Thread(target=process_queue)
    queue_thread.start()

    socketio.run(app, debug=True)
