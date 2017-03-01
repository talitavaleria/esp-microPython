##
#   @file   main.py
#   @author Talita Valeria A da Matta
#   @date   March 2017
#   @description Mod 10-counter with 7 seg display
##

from machine import Pin
import array
import utime
import pmap  #pin mapping

# Binary to 7seg digit
digit = array.array('B', [ 0x3F,  # 0 
                           0x06,  # 1
                           0x5B,  # 2
                           0x4F,  # 3
                           0x66,  # 4
                           0x6D,  # 5
                           0x7D,  # 6
                           0x07,  # 7
                           0x7F,  # 8
                           0x6F]) # 9

# Configure pins as OUTPUT    
pins = [ Pin(pmap.D1, Pin.OUT), 
         Pin(pmap.D2, Pin.OUT), 
         Pin(pmap.D3, Pin.OUT), 
         Pin(pmap.D4, Pin.OUT), 
         Pin(pmap.D5, Pin.OUT), 
         Pin(pmap.D6, Pin.OUT), 
         Pin(pmap.D7, Pin.OUT)]

cont = 0

while(True):

    if(cont + 1 > 9):
        cont = 0
    else:
        cont+=1

    for x in range(0, 7):
        pins[x].value( digit[cont] & (1 << x) )

    utime.sleep_ms(200)