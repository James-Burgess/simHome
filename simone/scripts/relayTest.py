#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [25, 4, 17, 18, 27, 22, 19, 26]

# loop through pins and set mode and state to 'off'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

SleepTimeL = .5 # time to sleep between operations in the main loop

def main():
  #turn on one at a time then all off
  for i in pinList:
    GPIO.output(i, GPIO.LOW)
    print i  

    time.sleep(SleepTimeL);

  for i in pinList:
    GPIO.output(i, GPIO.HIGH)
    print i   

  time.sleep(SleepTimeL);

  #Flash all 5 times
  for j in range (4):

    #all on
    for i in pinList:
      GPIO.output(i, GPIO.LOW)
      print i 

    time.sleep(SleepTimeL);

    #all off
    for i in pinList:
      GPIO.output(i, GPIO.HIGH)
      print i 

    time.sleep(SleepTimeL);

  #clean exit
  print "Good bye!"
  GPIO.cleanup()

main()
