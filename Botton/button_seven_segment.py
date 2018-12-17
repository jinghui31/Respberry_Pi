import RPi.GPIO as gpio
import time

pins = (5, 6, 13, 19, 12, 16, 20, 21)
digits = {
    0: (1, 1, 1, 0, 0, 1, 1, 1),
    1: (1, 0, 0, 0, 0, 1, 0, 0),
    2: (1, 1, 0, 1, 0, 0, 1, 1),
    3: (1, 1, 0, 1, 0, 1, 1, 0),
    4: (1, 0, 1, 1, 0, 1, 0, 0),
    5: (0, 1, 1, 1, 0, 1, 1, 0),
    6: (0, 1, 1, 1, 0, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 1, 0, 0),
    8: (1, 1, 1, 1, 0, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 0, 0),
    '.': (0, 0, 0, 0, 1, 0, 0, 0)
}

phones = list(map(int,'0933822291'))
for i in range(len(phones)):
    phones.insert((i + 1) * 2 - 1, '.')

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

for pin in pins:
    gpio.setup(pin, gpio.OUT)

for num in phones:
    for index, pin in enumerate(pins):
        gpio.output(pin, digits[num][index])
    time.sleep(0.7)

gpio.cleanup()