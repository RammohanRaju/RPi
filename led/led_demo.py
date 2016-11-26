# This program will Light the LED connected to GPIO 7.
# Note: This will make the LED to keep on lighting. Make sure to clenup after the execution.
import RPi.GPIO as GPIO      # Import RPi.GPIO module
GPIO.setmode(GPIO.BCM)       # Choose BCM or BOARD
GPIO.setup(7, GPIO.OUT)      # Set GPIO7 as an output
GPIO.output(7, 1)            # Set GPIO7 to 1/GPIO.HIGH/True

#GPIO.output(7, 0)           # Uncomment to switch off the LED
#GPIO.cleanup()              # Uncomment to clean up GPIO
