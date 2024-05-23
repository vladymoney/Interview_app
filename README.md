# Interview_app
 
# Mouse and Webcam Capture

This project captures mouse clicks and webcam images using Flask and Flask-SocketIO. When a user clicks on the browser window, the server captures an image from the webcam, processes it, and sends the image along with a message back to the client to be displayed.

## Features

- Display mouse coordinates on mouse movement.
- Capture and display mouse click coordinates.
- Capture an image from the webcam on mouse click.
- Display the captured image along with a message.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vladymoney/Interview_app.git
    cd Interview_app
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your browser and navigate to:**

    ```bash
    http://localhost:5000
    ```

## Project Structure

Interview_app/
│
├── static/
│   ├── images/
│   └── styles.css  # CSS file for styling
│
├── templates/
│   └── index.html  # HTML file for the front end
│
├── app.py  # Main Flask application
├── camera_capture.py  # Script for capturing images from the webcam
├── database.py  # Script for handling database interactions
├── mouse_monitor.py  # Script for monitoring mouse events
├── README.md  # Project documentation
├── requirements.txt  # List of required Python packages
└── view_database.py  # Script for viewing database entries


## How It Works

1. **Client-Side:**

    - The browser listens for mouse clicks and mouse movements.
    - On mouse click, it sends the coordinates to the server using Socket.IO.
    - It updates the mouse coordinates display on mouse movement.

2. **Server-Side:**

    - The server listens for `mouse_click` events.
    - When a `mouse_click` event is received, it captures an image from the webcam.
    - It processes the image to check for faces.
    - It saves the image to the `static/images` directory.
    - It sends the image path and a message back to the client using Socket.IO.

3. **Display:**

    - The client receives the image path and message.
    - It updates the image element to display the captured image.
    - It shows the accompanying message.

## Requirements

- Python 3.6 or higher
- Flask
- Flask-SocketIO
- OpenCV
- Eventlet