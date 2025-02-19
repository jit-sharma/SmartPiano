# -*- coding: utf-8 -*-
# Complete project details at https://RandomNerdTutorials.com/micropython-esp32-bluetooth-low-energy-ble/
"""
==============================================================================
midi_bluetooth.py:
ESP32 bluetooth services
MicroPython ESP32

Excute main function to initiate bluetooth services
1. peripheral_task - advertises bluetooth service name ["Rachit-Smart MIDI LED Piano"]
2. sensor_task - a timer service, timer counter can be read from Bluetooth client
3. midi_task - receives data from blutooth client

Usages
Python files: esp32_util.py, ble_helper.py
==============================================================================
Usages:


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Feb-25] Jit Sharma: First version
    * v2 [xx-Feb-25] Jit Sharma:

Last Updated: 9-Feb-25
==============================================================================
"""

import sys
from micropython import const
import asyncio
import aioble
import bluetooth
import struct
from machine import Pin
from random import randint
import ble_helper 
import esp32_util as u

bluetooth_service_name = "Rachit-SmartLED Piano"

def ts():
    return u.ts()

# Init LED
led = Pin(2, Pin.OUT)
led.value(0)

# Init timer value
value = 0

# See the following for generating UUIDs:
# https://www.uuidgenerator.net/
_BLE_SERVICE_UUID = bluetooth.UUID('19b10000-e8f2-537e-4f6c-d104768a1214')
_BLE_SENSOR_CHAR_UUID = bluetooth.UUID('19b10001-e8f2-537e-4f6c-d104768a1214')
_BLE_LED_UUID = bluetooth.UUID('19b10002-e8f2-537e-4f6c-d104768a1214')
# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000

# Register GATT server, the service and characteristics
ble_service = aioble.Service(_BLE_SERVICE_UUID)
sensor_characteristic = aioble.Characteristic(ble_service, _BLE_SENSOR_CHAR_UUID, read=True, notify=True)
led_characteristic = aioble.Characteristic(ble_service, _BLE_LED_UUID, read=True, write=True, notify=True, capture=True)

# Register service(s)
aioble.register_services(ble_service)

# Helper to encode the data characteristic UTF-8
def _encode_data(data):
    return str(data).encode('utf-8')

# Helper to decode the LED characteristic encoding (bytes).
def _decode_data(data):
    try:
        if data is not None:
            # Decode the UTF-8 data
            print("Data received:", data)
            number = int.from_bytes(data, 'big')
            return number
    except Exception as e:
        print("Error decoding input fron Bluetooth client:", e)
        return None

# Get sensor readings
def get_random_value():
    return randint(0,100)

# Get new value and update characteristic
async def sensor_task():
    value = 0
    end_time = 60.0*60*5 # 5 Hours exit
    while True:
        if value >= end_time:
            sys.exit(-1)
            break
        #value =  #get_random_value()
        sensor_characteristic.write(_encode_data(value), send_update=True)
        print(f'\r [{ts()}] Bluetooth service on for: {value:4} Sec', end="")
        value += 1

        await asyncio.sleep_ms(1000)


# Serially wait for connections. Don't advertise while a central is connected.
async def peripheral_task():
    while True:
        try:
            async with await aioble.advertise(
                _ADV_INTERVAL_MS,
                name=bluetooth_service_name,
                services=[_BLE_SERVICE_UUID],
                ) as connection:
                    print(f"\n [{ts()}] Connection from", connection.device)
                    await connection.disconnected()             
        except asyncio.CancelledError:
            # Catch the CancelledError
            print(f"[{ts()}] Peripheral task cancelled")
        except Exception as e:
            print(f"[{ts()}] Error in peripheral_task:", e)
        finally:
            # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)


import gc

async def midi_task():
    i=j=0
    print("\nBluetooth connection, listening...")
    while True:
        try:
            connection, data = await led_characteristic.written()
            # print('Connection: ')
            #print('Data: ', data, type(data))
            data = _decode_data(data)
            print('Decoded Input Data: ', data)
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            print("GC ran")            
            print(f"\n Timer:{i:2} calls:{j:2}", end=" ")
            i+=1
            # 1-10 is for File Numbers, 0 to reset, A to play welcome Msg
            if data in range(1,21):
                j += 1
                print(f'[{ts()}]: Turning LED ON')
                led.value(1)
                ble_helper.play_midi_raindrop(data)
                print(f'[{ts()}]: Turning LED OFF')
                led.value(0)
            elif data in range(21,121):
                j += 1
                print(f'[{ts()}]: Turning LED ON')
                led.value(1)
                if data>100:
                    data = data - 100
                ble_helper.set_brightness(data)
                print(f'[{ts()}]: Turning LED OFF')
                led.value(0)
            elif data == 0:
                j += 1
                print(f'[{ts()}]: Turning LED OFF')
                ble_helper.reset_LEDs()
                led.value(0)
            elif data == 65: # "A"
                j += 1
                ble_helper.display_anim()
                led.value(0)                
            else:
                print('Unknown command')
        except asyncio.CancelledError:
            # Catch the CancelledError
            print("Peripheral task cancelled")
        except Exception as e:
            print("Error in peripheral_task:", e)
        finally:         # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)
    print(f"[{ts()}]: Bluetooth session ended")        



# Run tasks
async def main():
    print(f"[{ts()}] {__name__} Creating async Tasks")
    t1 = asyncio.create_task(sensor_task())
    t2 = asyncio.create_task(peripheral_task())
    t3 = asyncio.create_task(midi_task())
    print(f"[{ts()}] {__name__} Created async Tasks")
    if not t1:
        t2.cancel()
        t3.cancel()
    print(f"[{__name__}] value: {value}")
    await asyncio.gather(t1,t2)
    
#asyncio.run(main())
if __name__ == '__main__':
    print(f"[{ts()}]: Bluetooth Service - run from main.py")