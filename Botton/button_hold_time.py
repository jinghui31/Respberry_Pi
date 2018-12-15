from gpiozero import Button, LEDBoard
from signal import pause
import time

button = Button(18)
led = LEDBoard(red = 17, green = 27, blue = 22)

def Action():
    led.red.on()
    time.sleep(1)
    led.red.off()
    led.green.on()
    time.sleep(1)
    led.green.off()
    led.blue.on()
    time.sleep(1)
    led.blue.off()

button.when_held = Action
pause()