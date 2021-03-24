import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(self, pin_pulse, pin_dir):
        if not isinstance(pin_pulse, int) or not isinstance(pin_dir, int):
            raise TypeError("Pins must be of type int.")
        self.pin_pulse = pin_pulse
        self.pin_dir = pin_dir
        GPIO.setup(self.pin_pulse, GPIO.OUT)
        GPIO.setup(self.pin_dir, GPIO.OUT)

    def spin(self, direction, speed, round):
        self.setDirection(direction)

        if round < 0:
            raise TypeError("round should be non-negative (rounds)")
        if speed < 0:
            raise TypeError("speed should be non-negative (rounds per second)")

        # (360 deg per round)/(1.8 deg per step) 1/16 stepping mode.
        steps = 200 * 16 * round

        #ignoring on and off, 2sleeptime per step per step. 200 * 16 step per round, speed is in round per sec.
        sleeptime = 1.0 / (200 * 2 * 16 * speed)

        print(steps, sleeptime)

        # motor's hard limit is 4 micro seconds
        if sleeptime < 0.000004:
            raise Exception("Too fast, motor can't run")

        for i in range(steps):
            GPIO.output(self.pin_pulse, GPIO.HIGH)
            time.sleep(sleeptime)
            GPIO.output(self.pin_pulse, GPIO.LOW)
            time.sleep(sleeptime)

    def setDirection(self, direction):
        if direction == 0:
            GPIO.output(self.pin_dir, GPIO.LOW)
        elif direction == 1:
            GPIO.output(self.pin_dir, GPIO.HIGH)
        else:
            raise TypeError("Direction must be binary.")
