from machine import Pin, ADC
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
