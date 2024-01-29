import pyfirmata
from pyfirmata import Arduino, SERVO, util
from time import sleep
port = 'COM3' #usb pin
pin = 10 #pin which servo is connected to on digital
board = pyfirmata.Arduino(port)
board.digital[pin].mode = SERVO#

def rotate_servo(pin,angle):
     board.digital[pin].write(angle)
     sleep(0.0015)


while True:
    user_angle = int(input("Enter your prefered angle:"))
    for i in range(0,user_angle):
        rotate_servo(pin, i)




