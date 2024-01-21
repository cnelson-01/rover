import threading

import RPi.GPIO as GPIO
import time

from Stepper import Stepper

GPIO.setmode(GPIO.BCM)


speed = .005
s1 = Stepper(23, 3, 21, speed)
s2 = Stepper(4, 17, 20, speed, reversed=True)

s3 = Stepper(24, 25, 16, speed)
s4 = Stepper(27, 22, 12, speed, reversed=True)

s1.moveForward(10000)
#s2.moveBackward(1000)
#s3.moveForward(10000)
#s4.moveForward(10000)

# time.sleep(2)
# s1.moveBackward(5000)
# s2.moveBackward(5000)
