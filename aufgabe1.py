import Testverzeichnis 
import time 
i = 1

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

	global px
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

if __name__ == "__main__":
	z = 0.125 #der Faktor wird für einen Meter benötigt

	fahren(z*1.5)
