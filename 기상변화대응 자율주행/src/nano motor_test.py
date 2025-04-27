import RPi.GPIO as GPIO
import time

# 핀 번호 설정
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
PWMA = 18
PWMB = 23

# 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup([AIN1, AIN2, BIN1, BIN2, PWMA, PWMB], GPIO.OUT)

# PWM 설정 (주파수 1000Hz)
pwm_a = GPIO.PWM(PWMA, 1000)
pwm_b = GPIO.PWM(PWMB, 1000)
pwm_a.start(0)
pwm_b.start(0)

def forward(speed=50):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

def backward(speed=50):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

def stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

try:
    print("전진")
    forward(60)
    time.sleep(2)

    print("정지")
    stop()
    time.sleep(1)

    print("후진")
    backward(60)
    time.sleep(2)

    print("정지")
    stop()

finally:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
