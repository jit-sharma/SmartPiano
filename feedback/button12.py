"""
This ESP32 MicroPython code was developed by newbiely.com
This ESP32 MicroPython code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-button-debounce
"""

from machine import Pin
import time

BUTTON_PIN = 12 # The ESP32 pin GPIO21 connected to the button

# Setup the button pin. The Pin.PULL_UP enables the internal pull-up resistor.
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Initialize the previous state of the button
prev_button_state = 1  # Assuming the button is unpressed initially
i=0
button_state = button.value()
print("button_state:", button_state)
while True:
    # Read the current state of the button
    button_state = button.value()

    # Check if button was released
    if prev_button_state == 0 and button_state == 1:
        print("The button is released")

    # Check if button was pressed
    if prev_button_state == 1 and button_state == 0:
        print("The button is pressed")

    # Save the current state as the previous state for the next loop iteration
    prev_button_state = button_state
    time.sleep(.3)
    i=i+1
    print(f'\r{i}', end=' ')
    
print('\n EOF')