import threading

import RPi.GPIO as GPIO
import time

from NetworkMotor import NetworkMotor
from Stepper import Stepper

GPIO.setmode(GPIO.BCM)

speed = .001
s0 = Stepper(23, 3, 21, speed)
s1 = Stepper(4, 17, 20, speed, reversed=True)

s2 = Stepper(24, 25, 16, speed)
s3 = Stepper(27, 22, 12, speed, reversed=True)

motors = [
    NetworkMotor(50000, s0),
    NetworkMotor(50001, s1),
    NetworkMotor(50002, s2),
    NetworkMotor(50003, s3),
]
# while True:
time.sleep(1000)
for nm in motors:
    nm.shutdown()

# s1.moveForward(10000)
# s2.moveBackward(1000)
# s3.moveForward(10000)
# s4.moveForward(10000)

# time.sleep(2)
# s1.moveBackward(5000)
# s2.moveBackward(5000)
