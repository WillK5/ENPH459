def linMov(distance, linRate):
    
    pulses = distance * (360/105) * (1/1.8)
    pulses = int(pulses)
    
    pulseLength = 0.0000001
    timeBetween = period - pulseLength
    stepNumber = 0

    pulps = linRate * (360/105) * (1/1.8) 
    period = 1/(pulps) #Period in seconds

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
