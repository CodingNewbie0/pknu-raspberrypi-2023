import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN)
GPIO.setup(14, GPIO.OUT)

try:
    while True:
        inputIO = GPIO.input(6)

        if inputIO == False:
            GPIO.output(14, GPIO.LOW)
            time.sleep(0.01)

        else:
            GPIO.output(14, GPIO.HIGH)
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
