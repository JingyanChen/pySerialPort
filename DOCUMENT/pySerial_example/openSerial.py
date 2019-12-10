#Example : Open the serial port method , Output opened successfully through the console

import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM10'
ser.open()


if ser.is_open:
    print("open port",ser.port,"is suceess","baudrate:",ser.baudrate)
else:
    print("open port",ser.port,"is failed","baudrate:",ser.baudrate)