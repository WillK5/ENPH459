import serial

serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)
secureList = []

code = ''

while True:

    if serial.read() == b'\x02':
        data = serial.read()
        char = data.decode("utf-8")

        while data != b'\r':
            code += char
            data = serial.read()
            char = data.decode("utf-8")

        print(code)
        secureList += [code]
        code = ''
        print(secureList)

#    data = serial.read()
 #   print(data)
  #  char = data.decode("utf-8")
#
    #print(char)

 #   if char == '\r':
  #      print('String ending')
   #     print(code)

        # Storing code for later use
    #    secureList += [code]  
     #   code = ''
      #  print(secureList)
        
#    elif char == '\x02':
 #       print('String starting')
  #  else:
   #     code = code + char
