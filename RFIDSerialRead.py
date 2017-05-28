import serial

serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)
secureList = []

code = ''

while True:

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

    if code in secureList:        # open the door immediately, stand back image written
        print("opening")
        #doorOpen()

    else: 
        # Send to payment image, wait for user to imput the image
        print("not registered")
        print("Payment")
        secureList += [code]
        # if paymentFunc():
        #     doorOpen()
        # else:
        #     #Write error message, return to main screen


    
