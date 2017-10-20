#!/usr/bin/python 
import RPi.GPIO as g
from time import sleep

#Setup Board
g.setmode(g.BCM)

#Setup Pins
pinList = [18, 22, 27, 17]
#4 bed #17 bath #18 Lounge
for i in pinList: 
    g.setup(i, g.OUT) 

switchList = [21, 20, 16, 12] #, 25] 
#23 bed #24 bath #25 extra
for i in switchList:
        g.setup(i, g.IN, pull_up_down=g.PUD_UP)

#Switch
def lightSwitch(num):
    if (g.input(num) == 0):
      g.output(num,g.HIGH)
      print("%s is off" %num)
    else:
      g.output(num,g.LOW)
      print("%s is on" %num)

    

def main():
        state = 0
        while True:
                try:
                    bed_input_state = g.input(21)
                    bath_input_state = g.input(20)
                    lounge_input_state = g.input(16)
                    outside_input_state = g.input(12)

                    if bed_input_state == False:
                            lightSwitch(18)
                    if bath_input_state == False:
                            lightSwitch(22)
                    if lounge_input_state == False:
                             lightSwitch(17)
                    if outside_input_state == False:
                             lightSwitch(27)

                except KeyboardInterrupt:
                        print("Outies")
                        g.cleanup()

                sleep(.5)

if __name__ == "__main__":
        main()
