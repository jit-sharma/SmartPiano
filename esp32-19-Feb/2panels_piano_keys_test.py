import machine
import neopixel
import time

def clear(np):
    np.fill((0, 0, 0))
    np.write()

try:
    LED = machine.Pin(2, machine.Pin.OUT)
    np = neopixel.NeoPixel(machine.Pin(4), 870)
    clear(np)
    np[0] = (150, 0, 0) # set to red, full brightness
    np[1] = (0, 150, 0) # set to green, half brightness
    np[2] = (0,0,155)
    np.write()

    strip = 256*2
    counter = strip

    for i in range (0,30):
        for j in range (counter,counter+3):
            np[j] = (155,0,0)
        counter += 3
        for j in range (counter,counter+3):
            np[j] = (0,155,0)
        counter += 3        
        for j in range (counter,counter+3):
            np[j] = (0,0,155)
        counter += 3
        

    """
    for i in range (counter+1,counter+10):
        np[i] = (0,155,0)
    """

    np.write()
    t = 60*3
    for i in range(t):
        time.sleep(1)
        print(f'\r Running timer {i:3}/{t:3} sec, Press Ctrl+C to terminate.', end="")


    LED.value(1)
    time.sleep(.25)
    LED.value(0)
except KeyboardInterrupt:
    print("\nProgram terminated by using Keyboard ")
finally:
    clear(np)    
