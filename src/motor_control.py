import RPi.GPIO as GPIO

# GPIO Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm_pin = 18
motor_pins = {
    'm_f_l': (2, 3),
    'm_f_r': (22, 23),
    'm_r_l': (14, 15),
    'm_r_r': (24, 25)
}

for pin_pair in motor_pins.values():
    GPIO.setup(pin_pair[0], GPIO.OUT)
    GPIO.setup(pin_pair[1], GPIO.OUT)

GPIO.setup(pwm_pin, GPIO.OUT)
pwm_out = GPIO.PWM(pwm_pin, 1000)
pwm_out.start(50)

# Movement directions
direction = {
    '8': (1, 1, 1, 1),  # Forward
    '2': (-1, -1, -1, -1),  # Backward
    '4': (-1, 1, 1, -1),  # Left
    '6': (1, -1, -1, 1),  # Right
    '5': (0, 0, 0, 0)   # Stop
}

speed = 50

def set_motor_speed(ch):
    global speed
    speed = min(100, max(0, speed + (10 if ch == '+' else -10)))
    pwm_out.ChangeDutyCycle(speed)

def move_robot(ch):
    if ch in direction:
        for i, (pin1, pin2) in enumerate(motor_pins.values()):
            GPIO.output(pin1, GPIO.HIGH if direction[ch][i] == 1 else GPIO.LOW)
            GPIO.output(pin2, GPIO.LOW if direction[ch][i] == 1 else GPIO.HIGH)
