import Testverzeichnis
import time
from vilib import Vilib
import threading 

px = Testverzeichnis.Picarx()
current_state = None
px_power = 20
offset = 35
last_state = "stop"

# Lock für die Kamera
camera_lock = threading.Lock()

# Kamera einmal starten (außerhalb der Threads)
Vilib.camera_start()
Vilib.display()

# Flag für erkannte Schilder
sign_detected = False

def set_angle(direction: str, offset: int):
    increment = 5
    start_from = 10

    if direction == "left":
        for i in range(start_from, offset, increment):
            if get_status(gm_val_list) == 'stop' or get_status(gm_val_list) == 'right':
                break
            px.set_dir_servo_angle(i)
            px.forward(15) 
            time.sleep(0.02) 
        px.set_dir_servo_angle(0)
    elif direction == "right":
        for i in range(start_from, offset, increment):
            if get_status(gm_val_list) == 'stop' or get_status(gm_val_list) == 'left':
                break
            px.set_dir_servo_angle(-i)
            px.forward(15)
            time.sleep(0.02)
        px.set_dir_servo_angle(0)

def lost_line(last_state: str):
    if last_state == "left":
        px.set_dir_servo_angle(-offset)
        px.backward(10)
        time.sleep(0.3)
    elif last_state == "right":
        px.set_dir_servo_angle(offset)
        px.backward(10)
        time.sleep(0.3)

def get_status(val_list):
    _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
    if _state == [0, 0, 0]:
        return 'stop'
    elif _state[1] == 1:
        return 'forward'
    elif _state[0] == 1:
        return 'right'
    elif _state[2] == 1:
        return 'left'

# Thread für die Kameraprüfung
def camera_thread():
    global sign_detected
    while True:
        with camera_lock:
            Vilib.color_detect("purple")
            if Vilib.detect_obj_parameter['color_n'] != 0:
                sign_detected = True
                print("Schild erkannt!")
                time.sleep(2)
            else:
                sign_detected = False
            time.sleep(0.1)  # Vermeidet übermäßige CPU-Auslastung

if __name__ == '__main__':
    # Kamera-Thread starten
    camera_thread_instance = threading.Thread(target=camera_thread, daemon=True)
    camera_thread_instance.start()

    try:
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("gm_val_list: %s, %s" % (gm_val_list, gm_state))

            if gm_state != "stop" and not sign_detected:
                last_state = gm_state

            if gm_state == 'forward' and not sign_detected:
                px.set_dir_servo_angle(0)
                px.forward(100)
            elif gm_state == 'left' and not sign_detected:
                set_angle("left", offset)
                px.forward(px_power)
            elif gm_state == 'right' and not sign_detected:
                set_angle("right", offset)
                px.forward(px_power)
            else:
                px.stop()
                lost_line(last_state)

            # Wenn ein Schild erkannt wurde
            if sign_detected:
                px.stop()
                print("Schild erkannt, Auto hält an.")
                time.sleep(2)  # Haltezeit bei Schild

    finally:
        px.stop()
        print("stop and exit")
        time.sleep(0.1)
