import serial

serial = serial.Serial("/dev/ttyUSB0" buadrate=9600)

code = ''

while TRUE:

    data = serial.read()
    if data == '
