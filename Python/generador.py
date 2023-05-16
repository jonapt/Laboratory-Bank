from machine  import Pin, DAC, ADC
from time import sleep
import math

pin_button=Pin(22,Pin.IN)
pin_button2=Pin(23,Pin.IN)

def senxd(sel):
    print('GENERADOR DE FUNCIONES')
    f=10
    buf=[1 for i in range(16250) ]
    
    for i in range(len(buf)):
        buf[i]=128 + int(127*math.sin(f*i/len(buf)))

    dac1=(Pin(25))
    salida=DAC(dac1)

    while sel==4:
        
        if pin_button2.value()==1:
            sel=sel+1
        
        if pin_button.value()==1:
            f=f+100
            print(f)
        if f>10000:
            f=100
        for i in range(len(buf)):
            buf[i]=128 + int(127*math.sin(f*i/len(buf)))
            
        for i in buf:
            salida.write(i)
        
        for i in range(1,255):
            salida.write(i)
    
