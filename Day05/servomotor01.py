# 서보모터 예제
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

servo_pin = 11
touch = 24

GPIO.setwarnings(False) # 경고표시로그 사라짐
GPIO.setup(servo_pin, GPIO.OUT) # 서보핀 출력
GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 터치센서 입력 설정

servo = GPIO.PWM(servo_pin, 50) # 50Hz
servo.start(0) # 서보모터의 초기값을 0으로 설정

servo_deg = 0
servo_min = 3
servo_max = 12

def set_servo_degree(degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0

    duty = servo_min+(degree*(servo_max-servo_min)/180.0)
    servo.ChangeDutyCycle(duty) # 각도만큼 바뀜

try:
    while True:
        if GPIO.input(servo_pin) == GPIO.HIGH:
            servo_deg += 10
            set_servo_degree(servo_deg)
            print(servo_deg)
            time.sleep(0.1)
            
        else:
            servo_deg -= 10
            set_servo_degree(servo_deg)
            print(servo_deg)
            time.sleep(0.1)
        
        if servo_deg > 170:
            servo_deg = 170
        elif servo_deg < 10:
            servo_deg = 10

finally:
    GPIO.cleanup() # 핀초기화