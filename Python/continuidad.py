from machine import Pin, ADC
from time import sleep

pin_button=Pin(22,Pin.IN)
pin_button2=Pin(23,Pin.IN)

def  conti(sel):
    pin_buzz=Pin(19,Pin.OUT)
    pin_t=Pin(18,Pin.OUT)
    pin_h=Pin(5,Pin.IN)
    
    while sel==3:
        if pin_button2.value()==1:
            sel=sel+1
        if pin_h.value() == 1:
            pin_buzz.off()
        else:
            pin_buzz.on()
        
        