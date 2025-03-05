from machine import Pin
from machine import TouchPad as tp
from time import sleep

touch = tp(Pin(13))

while True:
    print(touch.read())
    sleep(0.5)
    
    