import Testverzeichnis
import time

px = Testverzeichnis.Picarx()
# px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

# Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
# or manual modify reference value by follow code
# px.set_line_reference([1400, 1400, 1400])

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
            if get_status(gm_val_list) == 'stop' or get_status(gm_val_list) == 'right':
                break
            px.set_dir_servo_angle(i)
            px.forward(15) 
            time.sleep(0.02) 
        px.set_dir_servo_angle(0)
    elif direction == "right":
        for i in range(start_from, offset, increment):
            #prüft ob der Zustand noch aktuell ist
            if get_status(gm_val_list) == 'stop' or get_status(gm_val_list) == 'left':
                break
            px.set_dir_servo_angle(-i)
            px.forward(15)
            time.sleep(0.02)
        px.set_dir_servo_angle(0)
#findet die Linie wieder, wenn das Auto die Linie verlässt
def lost_line(last_state:str):
    if last_state == "left":
        px.set_dir_servo_angle(-offset)
        px.backward(10)
        time.sleep(0.1)
    elif last_state == "right":
        px.set_dir_servo_angle(offset)
        px.backward(10)
        time.sleep(0.3)
#gibt Informationen zum aktuellen Zustand
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
        
def checkWall():
    dangerDistance = 35 
    imminentimpact = 20
    distance = round(px.ultrasonic.read(), 2)
    print(distance)
    if distance < imminentimpact and distance > 0:
         return 2
    elif distance < dangerDistance and distance > imminentimpact:
         px.stop()
         time.sleep(2)
         return 1
    return 0
 
def spurwechsel():
    px.set_dir_servo_angle(0)
    data = px.get_grayscale_data()
    dis = checkWall()
    state = px.get_line_status(data) 
    if dis == 1:
         px.set_dir_servo_angle(45)
         for i in range(0,10):
             px.forward(20)
             time.sleep(0.1)
         while(state[0] != 0 or state[1] != 0 or state[2] != 0):
             print(state)
             data = px.get_grayscale_data()
             state = px.get_line_status(data) 
             px.forward(40)
             
    elif dis == 2:
        for i in range(1, 10):
            px.backward(20)
            time.sleep(0.1)
    px.set_dir_servo_angle(0)
                
         
    #führt das Programm aus in Abhängigkeit des Zustands aus
if __name__=='__main__':
    try:
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

            if gm_state != "stop":
                last_state = gm_state

            if gm_state == 'forward':
                
                px.set_dir_servo_angle(0)
                px.forward(70) 
                spurwechsel()
            elif gm_state == 'left':
                
                set_angle("left", offset)
                px.forward(px_power)
                spurwechsel() 
            elif gm_state == 'right':
               
                set_angle("right", offset)
                px.forward(px_power)
                spurwechsel()
            else:
                
                lost_line(last_state)
                
    finally:
        px.stop()
        print("stop and exit")
        time.sleep(0.1)
