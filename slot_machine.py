import tm1637
import time
import random
import RPi.GPIO as GPIO

tm = tm1637.TM1637(clk=19, dio=13)
BUTTON, BLUE_LED, RED_LED = 21, 18, 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup([BLUE_LED, RED_LED], GPIO.OUT, initial=GPIO.LOW)

DOUBLE_PRESS_WINDOW = 0.4

def wait_for_button_release():
    """Wait until the button is released to avoid counting one hold twice."""
    while GPIO.input(BUTTON) == GPIO.LOW:
        time.sleep(0.01)

def blink_leds(pin, times=3, delay=0.2):
    """Flashes a specific LED a set number of times."""
    for _ in range(times):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)

def spin_reels(duration_steps=15):
    """Simulates the spinning motion on screen and alternates LEDs."""
    for step in range(duration_steps):
        fake_digits = [random.randint(0, 9) for _ in range(4)]
        tm.show("".join(str(digit) for digit in fake_digits))

        GPIO.output(BLUE_LED, step % 2 == 0)
        GPIO.output(RED_LED, step % 2 != 0)
        time.sleep(0.08)
        
    GPIO.output([BLUE_LED, RED_LED], GPIO.LOW)

print("Slot machine ready!")
try:
    while True:
        if GPIO.input(BUTTON) == GPIO.LOW:
            time.sleep(0.03)
            wait_for_button_release()

            double_press_deadline = time.monotonic() + DOUBLE_PRESS_WINDOW
            is_rigged = False
            while time.monotonic() < double_press_deadline:
                if GPIO.input(BUTTON) == GPIO.LOW:
                    is_rigged = True
                    wait_for_button_release()
                    break
                time.sleep(0.01)

            spin_reels()

             
            if is_rigged:
                final_numbers = [7, 7, 7, 7]

            else:
                final_numbers = [random.randint(0, 9) for _ in range(4)]

            for i in range(1, 5):
                display_state = final_numbers[:i] + [0] * (4 - i)
                tm.show("".join(str(digit) for digit in display_state))
                time.sleep(0.3)

            if len(set(final_numbers)) == 1:
                print("JACKPOT!")
                blink_leds(RED_LED)
            else:
                print("No jackpot. Try again!")
                blink_leds(BLUE_LED)

            time.sleep(0.6)
            
        time.sleep(0.05)

except KeyboardInterrupt:
    tm.write([0, 0, 0, 0])
    GPIO.cleanup()
    print("\nProgram stopped.")