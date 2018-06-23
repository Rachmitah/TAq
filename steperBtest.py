import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
usleep = lambda x : time.sleep(x/1000000.0)

GPIO_steppin = 7	
GPIO_dirpin  = 5	
GPIO_enpin   = 3	

GPIO.setup(GPIO_steppin, GPIO.OUT)
GPIO.setup(GPIO_dirpin, GPIO.OUT)
GPIO.setup(GPIO_enpin, GPIO.OUT)

GPIO.output(GPIO_enpin, True)
GPIO.output(GPIO_dirpin, False)
usleep(500)
def step():
	GPIO.output(GPIO_enpin, False)
	GPIO.output(GPIO_dirpin, False)
	
	n=0
	print("Kiri")
	while n<=3200:
		n+=1
		GPIO.output(GPIO_steppin, False)
		GPIO.output(GPIO_steppin, True)
		usleep(500)
	GPIO.output(GPIO_dirpin, True)
	n=0
	print("Kanan")
	while n<=800:
		n+=1
		GPIO.output(GPIO_steppin, True)
		GPIO.output(GPIO_steppin, False)
		usleep(500)
	
if __name__=="__main__":
	while True :
		step()
