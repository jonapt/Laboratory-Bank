from machine  import Pin, DAC, ADC
from time import sleep
import math
from multimeter import tester
from generador import senxd
from continuidad import conti

pin_button=Pin(22,Pin.IN)
pin_button2=Pin(23,Pin.IN)
sel=0

while True:
    if pin_button2.value()==1:
        sel=sel+1
        print(sel)
        sleep(1)
        if sel>=5:
            sel=0
        
    if sel == 1:
        tester(sel)
    elif sel == 2:
        continue
    elif sel == 3:
        conti(sel)
    elif sel == 4:
        senxd(sel)
    elif sel == 5:
        continue