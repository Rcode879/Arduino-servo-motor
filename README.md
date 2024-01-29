# Arduino-servo-motor
Uses python to control servo motor connected to arduino microcontroller.It uses python rather than the traditional arduino IDE language. You input and angle of choice and your servo motor will turn to that angle.

Required:

-pyfirmata

-Arduino IDE 

-Arduino IDE in built firmata custom library

Key information:

-Before starting, upload the firmata code (this can be found in your arduino IDE custom libraries in "Firmata/StandardFirmata") from the arduino IDE into your arduino microcontroller

-The COM port is the usb location where your arduino device is connected

-When the code is run your code will upload to the arduino 

-Servo motors do not turn beyond 180 degress so entering a number above that is useless

-No wiring diagram is provided

Troubleshooting:

-Check your computer COM port which the arduino is connected to

-Check is you have wired your physical servo motor to the Arduino correctly

-Check is you have selected the correct Arduino board on the Arduino IDE

-Check you have uploaded the "StandardFirmata" code to the arduino before running the python code

