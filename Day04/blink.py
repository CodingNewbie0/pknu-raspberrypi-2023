# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18

# GPIO.setmode(GPIO.BOARD) # 1 ~ 40
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT) # GPIO 18번 핀에다가 출력을 설정

while (True):
    GPIO.output(signal_pin, True) # GPIO 18번 핀에 전압 시그널 켜짐
    time.sleep(0.5) # 불이 0.5초동안 켜짐
    GPIO.output(signal_pin, False) # 오프 
    time.sleep(0.5) # 0.5초동안 불끈상태로 대기

    