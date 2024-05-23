import pyautogui
import time

def monitor_mouse(queue):
    try:
        while True:
            x, y = pyautogui.position()
            queue.put(('mouse', x, y))
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
