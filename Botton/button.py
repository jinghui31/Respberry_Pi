from gpiozero import Button, LED
from signal import pause

button = Button(18)
led_red = LED(17)
led_grn = LED(27)

def userPressed():
    print('pressed')
    led_red.toggle()
    led_grn.off()

def userReleased():
    print('released')
    led_grn.blink()

button.when_pressed = userPressed
button.when_released = userReleased

pause()