from gpiozero import Button, RGBLED
# RGBLED just use for static (red, green, blue)
from signal import pause
from random import randint

button = Button(18)
led = RGBLED(red = 22, green = 27, blue = 17)

def Action():
    r = randint(0, 100) / 100
    g = randint(0, 100) / 100
    b = randint(0, 100) / 100
    led.color = (r, g, b)

def Close():
    led.color = (0, 0, 0)

button.when_pressed = Action
button.when_held = Close
pause()