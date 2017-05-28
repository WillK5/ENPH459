#Goal:  

import RPi.GPIO as GPIO
import time

#Setting GPIO pins locations

step = 18 #Step input
dirPin = 23 #Direction input
disable = 24 #Disable input

#GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(step, GPIO.OUT)
GPIO.output(step, GPIO.LOW)

GPIO.setup(dirPin, GPIO.OUT)
GPIO.output(dirPin, GPIO.LOW)

GPIO.setup(disable, GPIO.OUT)
GPIO.output(disable, GPIO.LOW)



#Declaration of global variables to be used

global stepRate, timeBetween

pulseLength = 0.0000001 #In seconds
timeBetween = 1/(200*16*10)


def main():

    GPIO.output(disable, GPIO.HIGH) #Enable the motor controller
    GPIO.output(step, GPIO.LOW)

    while(1):
        GPIO.output(step, GPIO.HIGH)
        time.sleep(pulseLength)
        GPIO.output(step,GPIO.LOW)
        time.sleep(timeBetween)

#Running Main programs

main()


    

    
