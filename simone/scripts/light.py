import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

state = False

def switch():
	global state
	if state == False:
		GPIO.output(2,GPIO.LOW)
		state = True
	else:
		GPIO.output(2,GPIO.HIGH)
		state = False

def run():
	try:
  while True:
    input_state = GPIO.input(18)
    if input_state == False:
      print("you pressed a button")
      switch()
      time.sleep(2)
      
except KeyboardInterrupt:
  print ("quitting...")
  GPIO.cleanup()
