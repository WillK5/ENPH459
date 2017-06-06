import serial
import time
import Tkinter as tk

serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)
global secureList

secureList = []

##################### MAIN CODE ###############################

# Starting Scene (waiting for user to press button)
    # Button pressed, calling RFIDAuthenticate
    # If RFIDAuthenticate returns True -> Loading procedure begins
    #                     returns False -> Call error message -> send to starting scene
    # LoadingProcedure:

if RFIDAuthenticate():
    #Calling loading procedure
    if operate(doorState):
    	
else: 
    #calling starting scene 

################# RFID Authenticate #################

## Purpose:  Authenticate the key provided by an RFID serial tag.  

## Method:  Waits to RFID tag to be read, interprets the resulting bytes or information into a string
##          and checks a secure list (global variable) for the same tag, if the tag exists the function
##          returns True, if its not in the list the function calls the payment function, if payment is 
##          provided the function returns True, otherwise the function returns false

def RFIDAuthenticate():
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
            #doorOpen()

        else: 
            # Send to payment image, wait for user to imput the image
            print("not registered")
            print("Payment")
            if paymentFunc():
                secureList += [code]
                return True

            else:
                return False
            #     #Write error message, return to main screen


def paymentFunc():
    # Tkinter scene prompting user to indicate they made payment

    win = tk.Tk()
    win.title("Payment scene")


    while True:    
        payButton = tk.Button(win, text='Payment', font=myFont, command= (result=True) # To be completed
        notPayButton = tk.Button(win, text='No Payment', font=myFont, command= (result=False))

    return result



# Assuming motor has been enabled and initialized beforehand

def operate(doorState):

    speedHi = 300 #mm/s
    speedLo = 10 #mm/s

    highPulse = 0.0000001 #Seconds

    speedHi = (1.0/(speedHi * (360.0/105.0) * (1.0/1.8))) - highPulse
    speedLo = (1.0/(speedLo * (360.0/105.0) * (1.0/1.8))) - highPulse

    # Considering states and setting directions for states
    openLast = 1
    closedLast = 0

    closingDir = 1
    openingDir = 0

    rampUpTime = 20 # Duration of ramp function in seconds

    timeVar = speedLo # Time variable initialization (starting at zero)

    accelStep = 0.0000003 # Amount of time to decrement between acceleration pulses for each iteration
    decelTime = 0.0000003 # Amount of time to decrement between deceleration pulses for each iteration

    # Checking last known state
    if (doorState == openLast):    #Door was last open, closing
        GPIO.output(directionPin, closingDir)
        limitSW = GPIO.input(limitL)

    if (doorState == closedLast):    #Door was last closed, opening
        GPIO.output(directionPin, openingDir)
        limitSW = GPIO.input(limitR)

    t0 = time.time() # Starting time for actuation

    while (limitSW != 1): #While limit switch is not pressed

        timer = time.time()

        if (((timer-t0) < rampUpTime) and (timeVar > speedHi)): # Ramp up function          
            GPIO.output(step,1)
            time.sleep(highPulse)
            GPIO.output(step,0)
            time.sleep(abs(timeVar))
            timeVar = timeVar - accelStep   #Decreasing gap between pulses

        elif ((timer-t0) >= rampUpTime):
            GPIO.output(step,1)
            time.sleep(highPulse)
            GPIO.output(step,0)
            time.sleep(abs(timeVar))

        elif ():
            GPIO.output(step,1)
            time.sleep(highPulse)
            GPIO.output(step,0)
            time.sleep(abs(timeVar))

            timeVar = timeVar + decelTime

        else:

            print("Error")
            return False

    # Backoff limit switch until correct point

    print("Open/closing complete")

    return True
