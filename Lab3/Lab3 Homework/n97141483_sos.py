import RPi.GPIO as GPIO
import time

LED = 12
BUZZER = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

voice = GPIO.PWM(BUZZER, 523)
voice.start(0)


def signal(duration):
    # LED 亮 + 蜂鳴器響
    GPIO.output(LED, True)
    # voice.ChangeDutyCycle(90)
    voice.start(50)

    time.sleep(duration)

    # LED 滅 + 蜂鳴器停
    GPIO.output(LED, False)
    # voice.ChangeDutyCycle(0)
    voice.stop()

    time.sleep(0.2)


try:
    # S：3 短
    for i in range(3):
        signal(0.2)

    time.sleep(0.4)

    # O：3 長
    for i in range(3):
        signal(0.6)

    time.sleep(0.4)

    # S：3 短
    for i in range(3):
        signal(0.2)

finally:
    voice.stop()
    GPIO.cleanup()