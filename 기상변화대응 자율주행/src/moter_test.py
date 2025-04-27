# Raspberry Pi의 GPIO 핀을 제어하기 위한 모듈
import RPi.GPIO as GPIO
# 시간 지연(sleep)을 주기 위한 모듈
import time

# --- 핀 번호 설정 (BCM 기준) ---
# 왼쪽 모터 제어 핀
AIN1 = 22  # 방향 1
AIN2 = 27  # 방향 2
PWMA = 18  # PWM 속도 제어

# 오른쪽 모터 제어 핀
BIN1 = 25  # 방향 1
BIN2 = 24  # 방향 2
PWMB = 23  # PWM 속도 제어

# --- GPIO 초기 설정 ---
# 핀 번호 체계를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

# 모터 제어 핀들을 모두 출력으로 설정
GPIO.setup([AIN1, AIN2, BIN1, BIN2, PWMA, PWMB], GPIO.OUT)

# --- PWM 설정 (주파수 1000Hz) ---
# 각 PWM 핀에 대해 PWM 객체 생성
pwm_a = GPIO.PWM(PWMA, 1000)  # 왼쪽 모터
pwm_b = GPIO.PWM(PWMB, 1000)  # 오른쪽 모터

# PWM 신호 출력 시작 (초기 듀티사이클 0 = 정지)
pwm_a.start(0)
pwm_b.start(0)

# --- 전진 함수 ---
def forward(speed=50):
    # 왼쪽, 오른쪽 모터 모두 정방향 회전
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

# --- 후진 함수 ---
def backward(speed=50):
    # 왼쪽, 오른쪽 모터 모두 역방향 회전
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

# --- 좌회전 함수 ---
def turn_left(speed=50):
    # 왼쪽 바퀴 뒤로, 오른쪽 바퀴 앞으로 회전 → 좌회전
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

# --- 우회전 함수 ---
def turn_right(speed=50):
    # 왼쪽 바퀴 앞으로, 오른쪽 바퀴 뒤로 회전 → 우회전
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

# --- 정지 함수 ---
def stop():
    # 모든 모터 정지
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

# --- 테스트 동작 루틴 ---
try:
    print("좌회전")
    turn_left(60)
    time.sleep(2)

    print("정지")
    stop()
    time.sleep(1)

    print("우회전")
    turn_right(60)
    time.sleep(2)

    print("정지")
    stop()
    time.sleep(1)

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

# --- 프로그램 종료 시 GPIO 정리 ---
finally:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
