import Testverzeichnis
import time 


px = Testverzeichnis.Picarx() # Auto Variable erstellt
def beschleunigen(z):
	global px
	global i
	while(i < 50):
		px.forward(i * 5)
		time.sleep(z) #je nach gegebenner Zeit beschleunigt er schneller
		px.stop()
		i += 5


def bremsen():
	global px
	global i
	if(i >= 0):
		px.forward(i *2)
	time.sleep(0.1) #je nach gegebener Zeit bremst er schneller
	px.stop()
	i -= 5
#Auto beschleunigt zuerst, dann bleibt es auf einer Geschwindigkeit und dann bremst es ab

def fahren(z):
	a = 100

	# global px
	global i
	while(a > 15):
		beschleunigen(z)
		a -= 1
	while(a > 5 and a <= 15):
		px.forward(i)
		time.sleep(0.1)
		px.stop()
		a -= 1
	while(a > 0 and a <=5):
		bremsen()
		a -= 1

#fährt eine acht
def acht():
	zeit = 0.1
	speed = 52
	#fährt den ersten Kreis
	for angle in range(0, 35):
		px.set_dir_servo_angle(angle)
		px.forward(speed)
		time.sleep(zeit)
	for angle in range(35, -35, -1):
		px.set_dir_servo_angle(angle)
		px.forward(speed)
		time.sleep(zeit)
	#fährt den zweiten Kreis
	for angle in range(-35, 0):
		px.set_dir_servo_angle(angle)
		px.forward(speed*1.5)
		time.sleep(zeit)
	px.stop()

#parkt das Auto vom Ende der Acht wieder in die Startposition ein 
def einparken():
	for angle in range(0, 35):
		px.set_dir_servo_angle(-angle)
		px.backward(80)
		time.sleep(0.05)
		

if __name__ == "__main__":
	z = 0.125 #der Faktor wird für einen Meter benötigt
	px.reset()
	fahren(z)
	time.sleep(2)
	acht()
	#einparken()
	px.stop()
	
	
