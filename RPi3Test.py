#Purpose:   This code is intended to be a proof of integration between the limit switch and the stepper motor.
#           While the limit switch is pressed the stepper motor will turn, when the stepper is released the stepper
#           stops.  

import RPi.GPIO as GPIO
import time
import serial
import Tkinter as tk


#Setting GPIO pins locations

openSwtch = 17 #Input pin for switch
closeSwtch = 27

step = 2 #Step input
dirPin = 3 #Direction input
enable = 4 #Enable input

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

global secureList
secureList = []

global pulseLength, speedHi, speedLo

# Motor Characteristics
pulseLength = 0.0000001
speedLo = 0.3   #Low speed limit
speedHi = 0.01  #High speed limit


def main():

    #initialization():
    # Used to check the initial state of the door, checks limit switches first, moves door to bump into closed
    # switch to ensure closed, when done it exits.  Sets initial TK scene.  

#    myFont = "something"
#    win = tk.Tk()
#    win.title("User Interface")

#    while(1):
#        input_state = GPIO.input(openSwtch)
#
#        if input_state == True:
#            linMov(distance, linRate)
        
    rampUpDist(100)

            
def linMov(distance, linRate):
    # distance in mm, linRate in mm/s

    pulses = int(distance * (360/105) * (1/1.8))
    
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

def rampUpTime(duration):
    
    accel = 0.001
    timeVar = speedLo

    t0 = time.time()

    while(not(GPIO.input(openSwtch))):

        #Checking safety switches

        timer = time.time()

        if(timer - t0 > duration):
            return

        GPIO.output(step,1)
        time.sleep(pulseLength)
        GPIO.output(step,0)
        time.sleep(abs(timeVar))

        timeVar = timeVar - accel

    print("limit switch hit")
    return

def rampUpDist(distance):

    accel = 0.00001
    timeVar = speedLo

    GPIO.output(enable, GPIO.HIGH) #Enable the motor controller
    time.sleep(0.2)
    GPIO.output(step, GPIO.LOW)

    x = 0
    pulses = int(distance * (360/105) * (1/1.8))
    print(pulses)

    while(not(GPIO.input(openSwtch)) and not(GPIO.input(closeSwtch))):

        if(pulses < x):
            return

        GPIO.output(step,1)
        time.sleep(pulseLength)
        GPIO.output(step,0)
        time.sleep(abs(timeVar))

        timeVar = timeVar - accel
        print(timeVar)

        x = x + 1

    limit()

def rampDownDist(distance, timeVar):

    deccel = 0.00001

    x = 0
    pulses = int(distance * (360/105) * (1/1.8))
    print(pulses)

    while(not(GPIO.input(openSwtch)) and not(GPIO.input(closeSwtch))):

        if(pulses < x):
            return

        GPIO.output(step,1)
        time.sleep(pulseLength)
        GPIO.output(step,0)
        time.sleep(abs(timeVar))

        timeVar = timeVar + deccel

        x = x + 1

    limit()

# Purpose:  Drives the stepper motor at some existing rate defined by timeVar, for a specific distance
#			Looks for limit switches during actuation, calling limit function when hit
def plateau(distance, timeVar):

	x = 0
	pulses = int(distance * (360/105) * (1/1.8))

	while(not(GPIO.input(openSwtch)) and not(GPIO.input(closeSwtch))):

		if(pulses < x):
			return

		GPIO.output(step,1)
		time.sleep(pulseLength)
		GPIO.output(step,0)
		time.sleep(abs(timeVar))

		x = x + 1

	limit()

def rampDown(duration):

    deccel = 0.00001
    timeVar = speedLo

    duration = 10
    t0 = time.time()

    while(not(GPIO.input(openSwtch))):

        timer = time.time()

        if(timer - t0 > duration):
            return

        GPIO.output(step,1)
        time.sleep(pulseLength)
        GPIO.output(step,0)
        time.sleep(abs(timeVar))

        timeVar = timeVar + deccel

    limit()

def RFIDAuthenticate():

    serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)


    code = ''
    timeout = 10000 #Time it takes for RFID read to timeout
    t0 = time.time()

    while True:

        # Checking for timeout
        if (time.time()-t0 >= timout):
            # Return to main screen
            return False

        # Getting RFID code
        if serial.read() == b'\x02':
            code = ''
            data = serial.read()
            char = data.decode("utf-8")

            while data != b'\r':
                code += char
                data = serial.read()
                char = data.decode("utf-8")
                
            print(code)
            print(secureList)

        # Checking for authentication
        if code in secureList:        # open the door immediately, stand back image written
            print("opening")
            return True

        else: 
            # Send to payment image, wait for user to imput the image
            print("not registered")
            print("Payment")
            if paymentFunc():
                secureList += [code]
                return True

            else:
                return False


#Running Main programs

main()



    
