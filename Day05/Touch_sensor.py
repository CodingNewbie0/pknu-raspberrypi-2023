# 푸시버튼 예제
import RPi.GPIO as GPIO
import time

stop_touch = 23 # 정차버튼
cancle_touch = 24 # 취소버튼
global count
count = 0 # 0으로 초기화
red = 17; green = 27; blue = 22;

def stop_clickHandler(argument): # 버스 정차(대기승객있음)
    global count
    for count in range(0, 50):
        count = count + 1
        if (count > 0):
            GPIO.output(red, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(blue, GPIO.HIGH)
        elif(count >= 50):
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        print(f'총 대기인원수는 {count}명 이상 초과할 수 없습니다.')
        else:
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        print(f'현 대기인원수는 {count}명 입니다.')

def cancle_clickHandler(argument): # 버스 정차안하고 바로출발(대기승객없음)
    global count
    for count in range(0, 50):
        count = count - 1
        if (count =< 0):
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        elif(count < 50):
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        print(f'정상적으로 취소되었습니다.\n현재 대기인원수는 {count}명 입니다.')

GPIO.setwarnings(False) # 경고표시로그 사라짐
GPIO.setmode(GPIO.BCM) # 숫자 핀번호로 꼽을때 쓰는 방식

GPIO.setup(stop_touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 터치센서 출력
GPIO.setup(cancle_touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(stop_touch, GPIO.RISING, callback=stop_clickHandler) # 미리 정의된 이벤트 핸들러 적용
GPIO.add_event_detect(cancle_touch, GPIO.RISING, callback=cancle_clickHandler)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True) 
GPIO.output(blue, True) 
GPIO.output(green, True)

while (True):
    time.sleep(0.01)
