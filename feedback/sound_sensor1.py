"""
This ESP32 MicroPython code was developed by newbiely.com
This ESP32 MicroPython code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-sound-sensor
"""

from machine import Pin
import time

SENSOR_PIN = 4  # The ESP32 pin GPIO18 connected to OUT pin of the sound sensor

prev_sound_state = 1  # the previous state from the input pin
sound_state = 1  # the current reading from the input pin

# Initialize the sensor pin as an input
sensor_pin = Pin(SENSOR_PIN, Pin.IN)
sound_state = sensor_pin.value()
print('Starting Sound Sensor', sound_state, prev_sound_state)
i = 0
# Main loop
while True:
    # Read the state of the input pin
    sound_state = sensor_pin.value()

    if prev_sound_state == 1 and sound_state == 0:
        print(" The sound has been detected")
    elif prev_sound_state == 0 and sound_state == 1:
        print("The sound has disappeared")
    else:
        print(f"{i} The sound state: {sound_state}, {prev_sound_state}")
    # Save the last state
    prev_sound_state = sound_state
    i += 1
    time.sleep(0.5)  # Delay for 100 milliseconds to mimic Arduino's loop delay
    #print('Sound Sensor', sound_state)
    
print('Starting Sound Sensor ended')