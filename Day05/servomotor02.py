# 서보모터2 예제
from time import sleep
from gpiozero import Servo, Button
from gpiozero.tools import sin_values

servo = Servo(11)
touch = Button(24)

servo.source = sin_values()
servo.source_delay = 0.1

# while True:
#     servo.min()
#     sleep(1)
#     touch.wait_for_press()

#     servo.mid()
#     sleep(1)
#     touch.wait_for_press()

#     servo.max()
#     sleep(1)
#     touch.wait_for_press()

    # if touch.wait_for_press:
    #     servo.source = sin_values()
    #     servo.source_delay = 0.1
    # else:
    #     servo.source = sin_values()
    #     servo.source_delay = -0.1