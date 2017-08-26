import RPi.GPIO as g
from time import sleep
import os

g.setmode(g.BCM)
#Setup Pins
lightList = [4, 17, 18] 
#4 bed #17 bath #18 Lounge
for i in lightList: 
    g.setup(i, g.OUT) 


def main():
	while True:
		try:
			bed_input_state = g.input(4)
			bath_input_state = g.input(17)
			beyond_input_state = g.input(18)

			if bed_input_state == False: 
				bed_state = 'on'
			else: 
				bed_state = 'off'
			if bath_input_state == False: 
				bath_state = 'on'
			else: 
				bath_state = 'off'
			if beyond_input_state == False: 
				beyond_state = 'on'
			else: 
				beyond_state = 'off'
			state = "echo bedroom: " + bed_state + " Bathroom: " + bath_state + " Beyond: " + beyond_state + " | cowsay | lolcat "
			sleep(1)
			
			os.system('clear')
			
			os.system(state)

		except KeyboardInterrupt:
			print("Outies")
			break

if __name__ == "__main__":
	main()