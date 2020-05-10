from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
    pot_value = pot.read()
    if pot_value == 0:
        pot_value = 0
        
    elif pot_value > 0:
        pot_value = pot_value

    print(pot_value)
    sleep(0.1)