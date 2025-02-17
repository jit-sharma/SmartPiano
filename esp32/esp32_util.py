# -*- coding: utf-8 -*-
"""
==============================================================================
esp32_util.py:
Utility functions 
[MicroPython ESP32]
==============================================================================
Usages:
blink_esp_blue_led(LED, times=5, speed=2)
get_time()
print_time()

@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Feb-25] Jit Sharma: First version
    * v2 [12-Feb-25] : changed to _led_config.json for program maintained json
    
Last Updated: 12-Feb-25
==============================================================================

"""
import time
import json

LED_CONFIG = '_led_config.json'

def get_matrix_panel_width():
    # Use JSON config file
    config = json.loads(open(LED_CONFIG,'r', encoding='utf-8').read())
    p = config["matrix_panel_width"]
    return p

def set_matrix_panel_width(data):
    config = json.loads(open(LED_CONFIG,'r',encoding='utf-8').read())
    config["matrix_panel_width"] = data
    with open('_led_config.json', 'w', encoding='utf-8') as json_file:
        json.dump(config, json_file)
    p = get_matrix_panel_width()
    print(f"matrix_panel_width saved {data}, Read from file:{b}")
    return b

def get_brightness():
    # Use JSON config file
    config = json.loads(open(LED_CONFIG,'r', encoding='utf-8').read())
    bp = config["brightness_panel"]
    return bp


def update_brightness(data):
    config = json.loads(open(LED_CONFIG,'r',encoding='utf-8').read())
    config["brightness_panel"] = data
    with open('_led_config.json', 'w', encoding='utf-8') as json_file:
        json.dump(config, json_file)
    b = get_brightness()
    print(f"panel brightness saved {data}%, Read from file:{b}")
    return b


def blink_esp_blue_led(LED, times=5, speed=2):
    speed = speed/10
    for i in range(times):
        LED.value(1)
        time.sleep(speed)
        LED.value(0)
        time.sleep(speed/2)


def print_time():
    print("ESP32:", get_time())


def get_time():
    t = time.localtime()
    time_str = f"{t[3]:02}:{t[4]:02}:{t[5]:02}"
    return time_str


def get_datetime():
    t = time.localtime()
    time_str = f"{t[2]}/{t[1]}/{t[0]} {t[3]:02}:{t[4]:02}:{t[5]:02}"
    return time_str

def ts():
    return get_time()

def dt():
    return get_datetime()

start_ms = time.ticks_ms()

def ms(start_ms=0):
    return time.ticks_ms()-start_ms

def mstr(start_ms=0):
    t = ms(start_ms)
    return f"{t/1000:5.3f}"

def main(name):
    update_brightness(50)
    
    
if __name__ == '__main__':
    #print (f"{__filename__} is being run directly") 
    main("ESP Util ")
    
"""
print(ts(), time.ticks_ms())
time.sleep_ms(1000)
print(ts(), time.ticks_ms(), mstr(start_ms))
time.sleep_ms(1000)
print(ts(), time.ticks_ms(), mstr(start_ms))
"""