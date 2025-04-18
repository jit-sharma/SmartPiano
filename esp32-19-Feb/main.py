# -*- coding: utf-8 -*-
"""
==============================================================================
main.py:
default file executed after boot
[MicroPython ESP32]


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [19-Jan-25] Jit Sharma: First version
    * v2 [9-Feb-25] Jit Sharma: Runs midi bluetooth services in async mode

Last Updated: 9-Feb-25
==============================================================================

"""
from time import sleep
import machine
from machine import Pin
from neopixel import NeoPixel

import midi_bluetooth
import asyncio
import esp32_util as u
import msg_display as msg
import led_display as anim

print(f'[{u.ts()}]: Type-C esp32 main.py inititated')
#np = NeoPixel(machine.Pin(4), 742)
#np.fill((0,0,0))
#np.write()

# Run Welcome Animation once here
anim.main(name="Welcome Animation", midi_file_id=20, play_msg=False)
msg.main(msg="FLOW NOTE", mode=1)
import gc
#gc.enable()
#gc.collect()
#gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

#import micropython
# micropython.mem_info(1)

@staticmethod
async def gc_coro():
    gc.enable()
    while True:
        gc.collect()
        gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
        print("GC ran")
        await asyncio.sleep(10)

try:    
    print(f'[{u.ts()}]: esp32 main.py Welcome done, starting bluetooth service')

    # Runs midi bluetooth services in async mode
    asyncio.run(midi_bluetooth.main())
except KeyboardInterrupt:
    print("Program terminated by using Keyboard ")
finally:
    #np.fill((0,0,0))
    #np.write()
    np = NeoPixel(machine.Pin(4), 742)
    np.fill((0,0,0))
    np.write()
    np = None


# asyncio.run(gc_coro())
print(f'[{u.ts()}]: Type-C esp32 main.py executed')