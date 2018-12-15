from gpiozero import Button, LEDBoard
from signal import pause
import time

button = Button(18)
led = LEDBoard(red = 17, green = 27, blue = 22)

def userPressed():
    led.red.toggle()
    time.sleep(1)
    led.green.toggle()
    time.sleep(1)
    led.blue.toggle()

button.when_pressed = userPressed
pause()