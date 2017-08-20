#!/usr/bin/python 
import RPi.GPIO as g
from time import sleep

#Setup Board
g.setmode(g.BCM)

#Setup Pins
lightList = [4, 17, 18] 
#4 bed #17 bath #18 Lounge
for i in lightList: 
    g.setup(i, g.OUT) 
    g.output(i, g.HIGH)

switchList = [23, 24, 25] 
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
    sleep(.5)

def main():
        while True:
                try:
                        bed_input_state = g.input(23)
                        bath_input_state = g.input(24)
                        lounge_input_state = g.input(25)

                        if bed_input_state == False:
                                lightSwitch(4)


                        if bath_input_state == False:
                                lightSwitch(17)

                        if lounge_input_state == False:
                                lightSwitch(18)


                except KeyboardInterrupt:
                        print("Outies")
                        g.cleanup()
                sleep(.5)

if __name__ == "__main__":
        main()
