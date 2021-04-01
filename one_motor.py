import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)

gpio.output(16, True)
time.sleep(4)
gpio.output(16, False)
time.sleep(0.5)
gpio.output(18, True)
time.sleep(4)
gpio.output(18, False)

gpio.cleanup()
