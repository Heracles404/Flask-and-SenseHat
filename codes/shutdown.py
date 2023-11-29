from sense_hat import SenseHat
from time import sleep
import os

s = SenseHat()
s.rotation = 270

r = (255, 0, 0)
w = (255, 255, 255)

# Function to shutdown the Raspberry Pi
def shutdown():
    s.show_message("Halting...", text_colour=r, back_colour=w)  # Display 'Halting...' for visual feedback
    sleep(2)
    s.clear()
    os.system("sudo shutdown -h now")

while True:
    event = s.stick.wait_for_event(emptybuffer=True)

    # Check for middle button press
    if event.action == "released" or event.direction != "middle":
        continue

    # Call shutdown function on middle button press
    shutdown()
