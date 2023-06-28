import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

swPin = 6
red = 14
blue = 15
green = 18

LED_list=[red, blue, green]

GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED_list, GPIO.OUT)
GPIO.output(LED_list, False)

while True:
	try:
		sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
		break
