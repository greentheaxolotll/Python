from gpiozero import LED
from time import sleep

def to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * to_binary(n // 2))

d = int(input("Enter a decimal number: "))
x = str(to_binary(d))
print(x)
lights = [LED(26), LED(19), LED(20), LED(13), LED(21), LED(12), LED(16), LED(6)]
j = 0
for i in lights:
    if x[j:j+1] == "1":
        i.on()
        sleep(1)
    else:
        i.off()
    j += 1