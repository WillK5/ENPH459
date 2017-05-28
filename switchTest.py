#Goal:  

import RPi.GPIO as GPIO
import time

#Setting GPIO pins locations

switch = 18 #Input pin for switch

#GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:

    input_state = GPIO.input(switch)
    if input_state == True:
        print('button pressed')
        while GPIO.input(switch) == True:
            time.sleep(0.3)
        print('out')
