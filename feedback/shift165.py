from machine import Pin

import time
import esp32_util as u

data_pin = Pin(13, Pin.IN)  # Data output from 74HC165, 27
clock_pin = Pin(14, Pin.OUT)  # Clock pin 26
latch_pin = Pin(12, Pin.OUT)  # Latch pin 25

def read_shift_register():
    clock_pin.value(0) # reseting clock
    latch_pin.value(0)  # reseting latch
    data_pin.value(0)
    #clock_pin.value(1)
    time.sleep_us(1)  # Short delay for stability
    print('latch pin 0')
    #time.sleep(1) 
    latch_pin.value(1)  # Activate latch
    print('latch pin 1, wait for a sec')
    #clock_pin.value(0)
    #time.sleep(1)
    data_value = 0
    """ """
    for i in range(16):  # Read 8 bits
        # clock_pin.value(1)  # Clock pulse
        time.sleep_ms(1)
        data = data_pin.value()
       
        print(f'{data}', end="")
        if i%8==3:
            print(".", end="")
        if i==7:
            print("  ", end=" ")
        data_value |= data_pin.value() << i
        clock_pin.value(1) 
        clock_pin.value(0)
    print(f'\n{u.mstr()}-----------')
    """ """
    return data_value

timer  = 0
while True:
    data = read_shift_register()
    print(f"{timer}: Read data:", data, "2[a-h] 1[a-h]: {0:016b}".format(data))
    # Process the read data as needed
    timer +=1
    time.sleep(2)
    time.sleep_ms(43) # 7 ms processing time, capture input at 50 ms interval, 5 times for a note event
