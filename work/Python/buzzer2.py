import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1) # 초기 1 헤르츠
pwm.start(90.0) # 듀티비 90% (음 구분 명확)

# 음계 도, 레, 미, 파, 솔, 라, 시를 나타냄.
scale = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 987, 1046]

# 음계를 숫자로 표현하여 노래로 만드는 변수
twinkle = [3,3,3,10,10,10]

try:
	for i in range(0,100):
		pwm.ChangeFrequency(scale[twinkle[i]])
		if i==1 or i==2 or i==3:
			time.sleep(1) # 특정부분 1초 출력
		else:
			time.sleep(0.5) # 0.5초 출력
	pwm.stop()

finally:
	GPIO.cleanup()
