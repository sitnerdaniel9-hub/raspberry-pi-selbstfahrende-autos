#Daniel Sitner, Raphael Colin, Abdulkarim Bashir Termanini, Niklas Wagner, Awat Hasan, Mariam Alwaas

import Testverzeichnis
import time


px = Testverzeichnis.Picarx()
# px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

# Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
# or manual modify reference value by follow code
#px.set_line_reference([1000, 1000, 1000])

current_state = None
px_power = 20
offset:int = 35
last_state = "stop"

#setzt die Servolenkung in Abhängigkeit des aktuellen Zustands(left, right, stop)
#bremst das Auto ab wenn es in der Kurve ist
def set_angle(direction:str, offset:int):
    increment:int = 5
    start_from:int = 10

    if direction == "left":
        for i in range(start_from, offset, increment):
            #prüft ob der Zustand noch aktuell ist
            if get_status(gm_val_list) == 'forward' or get_status(gm_val_list) == 'left':
                #px.set_dir_servo_angle(0)
                break
            px.set_dir_servo_angle(i)
            px.forward(10) 
            time.sleep(0.05)
        px.set_dir_servo_angle(0)
    elif direction == "right":
        for i in range(start_from, offset, increment):
            #prüft ob der Zustand noch aktuell ist
            if get_status(gm_val_list) == 'forward' or get_status(gm_val_list) == 'right':
                #px.set_dir_servo_angle(0)
                break
            px.set_dir_servo_angle(-i)
            px.forward(10)
            time.sleep(0.05)
        px.set_dir_servo_angle(0)

#findet die Linie wieder, wenn das Auto die Linie verlässt
def lost_line(last_state:str):
    if last_state == "left":
        px.set_dir_servo_angle(offset)
        px.backward(10)
        time.sleep(0.8)
    elif last_state == "right":
        px.set_dir_servo_angle(-offset)
        px.backward(10)
        time.sleep(0.8)

#gibt Informationen zum aktuellen Zustand
def get_status(val_list):
    _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
    if _state == [0, 0, 0]:
        return 'forward'
    elif _state == [1, 1, 1]:
        return 'reverse'
    elif _state[0] == 1:
        return 'right'
    elif _state[2] == 1:
        return 'left'
    elif _state[1] == 1:
        return 'stop'
#führt das Programm aus in Abhängigkeit des Zustands aus
if __name__=='__main__':
    #px.set_dir_servo_angle(0)
    #px.reset()
    try:
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

            if gm_state != "stop":
                last_state = gm_state

            if gm_state == 'forward':
                # px.set_dir_servo_angle(0)
                px.forward(50) 
            elif gm_state == 'left':
                set_angle("right", offset)
                # px.set_dir_servo_angle(offset)
                px.forward(px_power)
            elif gm_state == 'right':
                set_angle("left", offset)
                # px.set_dir_servo_angle(-offset)
                px.forward(px_power)

            elif gm_state == 'stop' and last_state == 'left':
                set_angle("right", offset)
                # px.set_dir_servo_angle(-offset)
                px.forward(px_power)
            elif gm_state == 'stop' and last_state == 'right':
                set_angle("left", offset)
                px.forward(px_power)

            else:
                if last_state == 'left':
                    lost_line("right")
                elif last_state == 'right':
                    lost_line("left")
                else:
                    px.backward(20)
                    time.sleep(0.6)

    finally:
        px.stop()
        print("stop and exit")
        time.sleep(0.1)
