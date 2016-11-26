# This program will Blink the LED connected to GPIO 7.
import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(7, GPIO.OUT)            # set GPIO7 as an output

try:
    while True:
        GPIO.output(7, 1)          # set GPIO7 to 1/GPIO.HIGH/True
        sleep(1)                   # wait a second
        GPIO.output(7, 0)          # set GPIO7 to 0/GPIO.LOW/False
        sleep(1)                   # wait a second

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program

