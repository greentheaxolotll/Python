import time
import board
import adafruit_dht
from gpiozero import LED
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 
red_led = LED(17)  # Change the pin number to the pin connected to your red LED
blue_led = LED(4)  # Change the pin number to the pin connected to your blue LED

print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    # TODO: Assign f where f represents the Farienheit equivalent to the input Celcius c
    f = (c * 9/5) + 32
    return f 
try:
    while True:
        try:
            celsius = sensor.temperature # Get the temperature in Celcius from the sensor
            fahrenheit = to_fahrenheit(celsius)
            current_time = datetime.now()
            print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
            with open("temperature.csv", "a") as file:
                file.write("{0},{1:0.1f},{2:0.1f}\n".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
            # TODO: Light up the red light when the temperature is above 72, and blue when it is below 72.
            if fahrenheit > 72.0:
                red_led.on()
                blue_led.off()
            else:
                blue_led.on()
                red_led.off()
            time.sleep(3.0)
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error    
except KeyboardInterrupt:
    print("program stopped by user")
finally:
    sensor.exit()
    red_led.off()
    blue_led.off()
    print("program stopped")
