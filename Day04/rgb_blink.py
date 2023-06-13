# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17
green = 22
blue = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True) 
GPIO.output(blue, True) 
GPIO.output(green, True) # 여기까지 초기화

try:
    while (True):
        GPIO.output(red, False) # 온 (빨강)
        GPIO.output(blue, True) # 오프 
        GPIO.output(green, True) # 오프 
        time.sleep(0.5)

        GPIO.output(red, True) # 오프
        GPIO.output(blue, False) # 온 (파랑)
        GPIO.output(green, True) # 오프 
        time.sleep(0.5)

        GPIO.output(red, True) # 오프
        GPIO.output(blue, True) # 오프 
        GPIO.output(green, False) # 온 (초록) 
        time.sleep(0.5)

        GPIO.output(red, False) # 분홍
        GPIO.output(blue, False) 
        GPIO.output(green, True) 
        time.sleep(0.5)

        GPIO.output(red, False) # 노랑
        GPIO.output(blue, True) 
        GPIO.output(green, False) 
        time.sleep(0.5)

        GPIO.output(red, True) # 하늘
        GPIO.output(blue, False)  
        GPIO.output(green, False)  
        time.sleep(0.5)

        GPIO.output(red, False) # 하양
        GPIO.output(blue, False) 
        GPIO.output(green, False) 
        time.sleep(0.5)
        
        GPIO.output(red, True) # 꺼짐
        GPIO.output(blue, True) 
        GPIO.output(green, True) 
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()