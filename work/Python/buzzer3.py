import RPi.GPIO as GPIO
import time
import keyboard

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 440) # 초기 440 헤르츠
pwm.start(90.0) # 듀티비 90% (음 구분 명확)

# 음계 도, 레, 미, 파, 솔, 라, 시, 높은도를 나타냄.
a = [262]
s = [294]
d = [330]
f = [349]
z = [392]
x = [440]
c = [494]
v = [523]

while True:
	if keyboard.read_key() == "q":
		print("Quit")
		pwm.stop()
		break
	elif keyboard.read_key() == "a":
		pwm.ChangeFrequency(a)
		time.sleep(0.1) # 특정부분 0.1초 출력
		
GPIO.cleanup()
