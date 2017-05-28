#Purpose:   This code is intended to be a proof of integration between the limit switch and the stepper motor.
#           While the limit switch is pressed the stepper motor will turn, when the stepper is released the stepper
#           stops.  

import RPi.GPIO as GPIO
import time

#Setting GPIO pins locations

openSwtch = 18 #Input pin for switch
closeSwtch = ## Need to find IO pin

step = 17 #Step input
dirPin = 23 #Direction input
enable = 24 #Enable input


#GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(openSwtch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(closeSwtch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(step, GPIO.OUT)
GPIO.output(step, GPIO.LOW)

GPIO.setup(dirPin, GPIO.OUT)
GPIO.output(dirPin, GPIO.LOW)

GPIO.setup(enable, GPIO.OUT)
GPIO.output(enable, GPIO.LOW)



#Declaration of global variables to be used

global pulseLength, period

distance = 1000 #in mm's

linRate = 300 # in mm/s

def main():

    while(1):
        input_state = GPIO.input(openSwtch)

        if input_state == True:
            linMov(distance, linRate)
        
            
def linMov(distance, linRate):
    
    pulses = distance * (360/105) * (1/1.8)
    pulses = int(pulses)
    
    pulseLength = 0.0000001
    stepNumber = 0

    pulps = linRate * (360/105) * (1/1.8) 
    period = 1/(pulps) #Period in seconds
    
    timeBetween = period - pulseLength
    #Preparing motor for startup

    GPIO.output(enable, GPIO.HIGH) #Enable the motor controller
    time.sleep(0.2)
    GPIO.output(step, GPIO.LOW)
    stepNumber = 0
    
    #Moving stage  
    
    while stepNumber < pulses:
        GPIO.output(step, GPIO.HIGH)
        time.sleep(pulseLength)
        GPIO.output(step,GPIO.LOW)
        time.sleep(timeBetween)
        stepNumber = stepNumber + 1
    print('out')
    print(stepNumber)

#Running Main programs

main()



    
