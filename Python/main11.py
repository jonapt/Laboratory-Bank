from machine  import Pin, DAC, ADC
from time import sleep
import math
from multimeter import tester
from generador import senxd
from continuidad import conti

pin_button=Pin(22,Pin.IN)
pin_button2=Pin(23,Pin.IN)
sel=from machine import Pin, ADC
from time import sleep


pin_button2=Pin(23,Pin.IN)
def tester(sel):
    
    
        
    pin34in_a = Pin(34)
    in_voltage = ADC(pin34in_a)
    
    out_voltage = Pin(33, Pin.OUT)
    
    in_voltage.atten(ADC.ATTN_11DB) #Acá porque trabajaremos un rango de 11DB y tener de 0 a +3.3 Voltios
    in_voltage.width(ADC.WIDTH_12BIT)
    

    
    while (sel==1):
        if pin_button2.value()==1:
            sel=sel+1
        out_voltage.on()
        volt_reader_max = (in_voltage.read_u16()/65535/2)
        
        volt_measured = 3.3 - volt_reader_max*(79/5)
        
        ohm_reader = in_voltage.read()
        print("Voltaje: ",volt_measured)
        sleep(0.5)


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