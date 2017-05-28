

# Assuming motor has been enabled and initialized beforehand

def operate():

    timeVar = 0 # Time variable initialization (starting at zero)
    accelTime = 0.0000003 # Amount of time to decrement between acceleration pulses for each iteration
    decelTime = 0.0000003 # Amount of time to decrement between deceleration pulses for each iteration

    endTime = 3000 # Time until the deceleration phase begins

    speedHi = 0.00001
    speedLo = 0.001

    # Checking last known state
    if (doorState == 1):    #Door was last open, closing
        direction = 1
        GPIO.output(directionPin, direction)
        limitSW = GPIO.input(limitL)

    if (doorState == 0):    #Door was last closed, opening
        direction = 0
        GPIO.output(directionPin, direction)
        limitSW = GPIO.input(limitR)


    while (limitSW != 1): #While limit switch is not pressed

        GPIO.output(step,1)
        time.sleep(highPulse)
        GPIO.output(step,0)
        time.sleep(abs(timeVar))

        if ( (timeVar > endTime) or !(timeVar <= speedHi) ):
            timeVar = timeVar - accelTime   #Decreasing gap between pulses until a certain amount of time
