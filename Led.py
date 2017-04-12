import RPi.GPIO as GPIO
import threading
import time

class Led(threading.Thread):

	gpio = 0
	cmd = ""
	param = ""

	def __init__(self, gpio, cmd, param):
		threading.Thread.__init__(self)
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		
		self.gpio = int(gpio)
		self.cmd = cmd
		self.param = param 

		GPIO.setup(self.gpio, GPIO.OUT)

	def run(self):
		if self.cmd == "O":
			if self.param[1] == "1":
				self.on() 
			else:
				self.off()
		else:
			self.blink(int(self.param[0]), float(self.param[1]))

	def on(self):
		print "led %i on" %(self.gpio)
		GPIO.output(self.gpio, GPIO.HIGH)

	def off(self):
		print "led %i off" %(self.gpio)
		GPIO.output(self.gpio, GPIO.LOW)

	
	def blink(self, count, duration):
		for x in range(0, count):
			self.on()
			time.sleep(duration)
			self.off()
			time.sleep(duration)
