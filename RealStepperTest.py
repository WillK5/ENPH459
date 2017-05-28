#Purpose:   This code is intended to be a proof of integration between the limit switch and the stepper motor.
#           While the limit switch is pressed the stepper motor will turn, when the stepper is released the stepper
#           stops.  

import RPi.GPIO as GPIO
import time

#Setting GPIO pins locations

switch = 18 #Input pin for switch
step = 17 #Step input
dirPin = 23 #Direction input
enable = 24 #Enable input

#GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(step, GPIO.OUT)
GPIO.output(step, GPIO.LOW)

GPIO.setup(dirPin, GPIO.OUT)
GPIO.output(dirPin, GPIO.LOW)

GPIO.setup(enable, GPIO.OUT)
GPIO.output(enable, GPIO.LOW)



#Declaration of global variables to be used

global pulseLength, timeBetween

pulseLength = 0.0000001 #In seconds
timeBetween = 1/(10*16*10) 


def main():

    GPIO.output(enable, GPIO.HIGH) #Enable the motor controller
    time.sleep(0.2)
    GPIO.output(step, GPIO.LOW)
    

    while(1):
        input_state = GPIO.input(switch)

        if input_state == True:
            print('button pressed')
            while GPIO.input(switch) == True:
                GPIO.output(step, GPIO.HIGH)
                time.sleep(pulseLength)
                GPIO.output(step,GPIO.LOW)
                time.sleep(timeBetween)
            print('out')
        
        

#Running Main programs

main()



    
