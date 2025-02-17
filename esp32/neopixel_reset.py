#
""" MicroPython ESP 32 lib """
import machine
from machine import Pin
from neopixel import NeoPixel
import time

def clear(np):
    np.fill((0, 0, 0))
    np.write()


def main(name="Neo Reset"):
    print(f'{name}:, clearing/reseting LEDs')  # Press Ctrl+F8 to toggle the breakpoint.
    led = machine.Pin(2, machine.Pin.OUT)
    led.value(1)
    time.sleep(1)
    led.value(0)
    
    led_count = 999
    np = NeoPixel(machine.Pin(16), led_count)
    clear(np)
    print("Cleared/reset")

if __name__ == '__main__':
    main("NeoPixel LEDs")


