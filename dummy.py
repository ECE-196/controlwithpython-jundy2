from serial import Serial, SerialException
from time import sleep

with Serial('COM5', 9600) as ser:
    ser.write(bytes([0x1]))
    print(ser.read() == bytes([0xaa]))

    sleep(1)

    ser.write(bytes([0x0]))
    print(ser.read() == bytes([0xaa]))

    sleep(1)

    ser.write(bytes([0x2]))
    print(ser.read() == bytes([0xff]))