from steperAtest import stepA
from steperBtest import stepB
import time
a=24
b=40

def reset():
		stepA(False, 24000, 100)
		stepB(False, 40000, 100)

def duaxtiga():
		stepA(True, 12000, 150)
		time.sleep(2)
		stepA(True, 12000, 150)
		time.sleep(2)
		
		stepB(True, 18000, 150)
		time.sleep(2)
		
		stepA(False, 12000, 150)
		time.sleep(2)
		stepA(False, 12000, 150)
		time.sleep(2)
		
		stepB(True, 18000, 150)
		time.sleep(2)

		stepA(True, 12000, 150)
		time.sleep(2)
		stepA(True, 12000, 100)
		time.sleep(2)
		
def A8x1(dr):
		for i in range(a) :
			stepA(dr,1000, 90)
			time.sleep(0.5)

def B(dr): 
		for i in range(b) :
			if i%2==0: 
				dr = True
			else :
				dr = False
			
			A8x1(dr)
			stepB(True,1000, 90)
			time.sleep(0.5)
		
def c(dr):
		for i in range(b) :
			stepB(dr, 1000, 100)
			time.sleep(1)
		

		
if __name__=="__main__":
		
		#B(False)
		reset()
		#c(True)
		#stepA(True, 1000, 90)
		#duaxtiga()
