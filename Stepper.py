import threading
import time

from RPi import GPIO


class Stepper:
    def __init__(self, stepPin, dirPin, enaPin, speed, reversed=False):
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.enaPin = enaPin

        self.speed = speed
        self.reversed = reversed
        self.threads = []
        GPIO.setup(self.stepPin, GPIO.OUT)
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.setup(self.enaPin, GPIO.OUT)

        self.enable(False)

    def moveForward(self, amount):
        self.setForward(True)
        self.threads.append(threading.Thread(target=self.move, args=[amount]))
        # self.threads[-1].daemon = True
        self.threads[-1].start()

    def moveBackward(self, amount):
        self.setForward(False)
        self.threads.append(threading.Thread(target=self.move, args=[amount]))
        # self.threads[-1].daemon = True
        self.threads[-1].start()

    def move(self, amount):
        self.enable(True)
        for a in range(amount):
            GPIO.output(self.stepPin, True)
            time.sleep(self.speed)
            GPIO.output(self.stepPin, False)
            time.sleep(self.speed)
        self.enable(False)

    def enable(self, doEna):
        GPIO.output(self.enaPin, not doEna)

    def setForward(self, b):
        if isinstance(b, bool):
            if self.reversed:
                GPIO.output(self.dirPin, not b)
            else:
                GPIO.output(self.dirPin, b)
