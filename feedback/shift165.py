from machine import Pin

import time
import esp32_util as u

data_pin = Pin(13, Pin.IN)  # Green Data output from 74HC165
clock_pin = Pin(14, Pin.OUT)  # Purple cable
latch_pin = Pin(12, Pin.OUT)  # white cable
register = 1

def read_shift_register():
    clock_pin.value(0) # reseting clock
    latch_pin.value(0)  # reseting latch
    data_pin.value(0)
    time.sleep_us(1)  # Short delay for stability
    #print('latch pin 0')
    #time.sleep(1) 
    latch_pin.value(1)  # Activate latch
    print('latch pin 1, wait for a sec')
    time.sleep_us(1)
    data_value = 0
    """ """
    for i in range(8*register):  # Read 8 bits
        # clock_pin.value(1)  # Clock pulse
        #time.sleep_ms(1)
        data = data_pin.value()
       
        print(f'{data}', end="")
        if i%8==3:
            print(".", end="")
        if i==7:
            print("  ", end=" ")
        data_value |= data_pin.value() << i
        clock_pin.value(1)
        #time.sleep(.1)
        clock_pin.value(0)
    latch_pin.value(0)  # reseting latch
    print(f'\n{u.mstr()}-----------')
    """ """
    return data_value

timer  = 0
while True:
    data = read_shift_register()
    if register == 1:
        print(f"{timer}: Read data:", data, "[a-h]: {0:08b}".format(data))
    elif register == 2:
        print(f"{timer}: Read data:", data, "2[a-h] 1[a-h]: {0:016b}".format(data))
    else:
        print(f"{timer}: Read data:", data, "4 3 2[a-h] 1[a-h]: {0:032b}".format(data))
        
    # Process the read data as needed
    timer +=1
    time.sleep_ms(250)# comment this
    time.sleep_ms(43) # 7 ms processing time, capture input at 50 ms interval, 5 times for a note event
