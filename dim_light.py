from gpiozero import RotaryEncoder, PWMLED

BRIGHTNESS_CURVE = 2
MAX_STEPS = 10

rotor = RotaryEncoder(16, 20, wrap=False, max_steps=MAX_STEPS)
rotor.steps = -MAX_STEPS
led = PWMLED(18)

def change_bright():
    position = (rotor.steps + MAX_STEPS) / (2* MAX_STEPS)
    brightness = position ** BRIGHTNESS_CURVE
    led.value = brightness
    print(f'Brightness:  {brightness:.0%}')

change_bright()
rotor.when_rotated = change_bright

try:
    while True:
        pass
except KeyboardInterrupt:
    led.off() 