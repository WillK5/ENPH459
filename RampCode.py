

# Assuming motor has been enabled and initialized beforehand

def operate(doorState):

    timer = time.time()

    openLast = 1
    closedLast = 0

    closingDir = 1
    openingDir = 0

    accelStep = 0.0000003 # Amount of time to decrement between acceleration pulses for each iteration
    decelTime = 0.0000003 # Amount of time to decrement between deceleration pulses for each iteration

    endPulses = 3000 # Time until the deceleration phase begins

    speedHi = 0.00001
    speedLo = 0.001

    rampUpTime = 20 # Duration of ramp function in seconds

    timeVar = speedLo # Time variable initialization (starting at zero)

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

        elif ():
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
