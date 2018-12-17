
from tkinter import *
from functools import partial
"""RGBLED just use for static (red, green, blue)"""
#from gpiozero import RGBLED
#from random import randint
#import RPi.GPIO as gpio

#led = RGBLED(red = 17, green = 22, blue = 27)

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
    9: (1, 1, 1, 1, 0, 1, 0, 0)
}

#gpio.setwarnings(False)
#gpio.setmode(gpio.BCM)

def ledOpen():
    print('ledOpen')
    #r = randint(0, 100) / 100
    #g = randint(0, 100) / 100
    #b = randint(0, 100) / 100
    #led.color = (r, g, b)

def ledClose():
    print('ledClose')
    #led.color = (0, 0, 0)

def Led(color):
    #ran = randint(0, 100) / 100
    print(color)
    if color == 'RED':
        #led.color = (ran, 0, 0)
        pass
    elif color == 'GREEN':
        #led.color = (0, ran, 0)
        pass
    elif color == 'BLUE':
        #led.color = (0, 0, ran)
        pass

def Number(data):
    print(data)
    for index, pin in enumerate(pins):
        #gpio.output(pin, digits[data][index])
        print(pin, digits[data][index])

    #gpio.cleanup()

def appInterface(window):
    frame = Frame(window, borderwidth = 1, relief = GROOVE)
    Label(frame, text = 'LED Controler', font = ('Helvetica', 20), anchor = W).pack(fill = X)

    Button(
        frame, text = 'open', font = ('Helvetica', 20), pady = 10, command = ledOpen
    ).pack(side = LEFT, fill = X, expand = True, padx = 10, pady = 10)
    
    Button(
        frame, text = 'close', font = ('Helvetica', 20), pady = 10, command = ledClose
    ).pack(side = LEFT, fill = X, expand = True, padx = 10, pady = 10)
 
    frame.pack(fill = X, padx = 10, pady = 10)

    rgbData = ['RED', 'GREEN', 'BLUE']
    rgbFrame = Frame(window, borderwidth = 1, relief = GROOVE)
    for i in rgbData:
        Button(
            rgbFrame, text = i, font = ('Helvetica', 20), pady = 10, command = partial(Led, i)
        ).pack(side = LEFT, fill = X, expand = True, padx = 10, pady = 10)

    rgbFrame.pack(fill = X, padx = 10, pady = 10)
    
    numFrame1 = Frame(window, borderwidth = 1, relief = GROOVE)
    for i in range(5):
        Button(
            numFrame1, text = i, font = ('Helvetica', 20), pady = 10, command = partial(Number, i)
        ).pack(side = LEFT, fill = X, expand = True, padx = 10, pady = 10)
    numFrame1.pack(fill = X, padx = 10, pady = 10)

    numFrame2 = Frame(window, borderwidth = 1, relief = GROOVE)
    for i in range(5, 10):
        Button(
            numFrame2, text = i, font = ('Helvetica', 20), pady = 10, command = partial(Number, i)
        ).pack(side = LEFT, fill = X, expand = True, padx = 10, pady = 10)

    numFrame2.pack(fill = X, padx = 10, pady = 10)

if __name__ == '__main__':
    app = Tk()
    app.title('LEDControl')
    app.geometry('500x500')
    app.option_add('*Button.Background', '#0000FF')
    app.option_add('*Button.Foreground', 'white')
    appInterface(window = app)
    app.mainloop()