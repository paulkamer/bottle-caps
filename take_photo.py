from datetime import datetime
from picamera import PiCamera
from time import sleep

with PiCamera() as cam:
    print("Starting up camera. Starting in 2 seconds...")
    cam.start_preview()

    sleep(2)  # Let camera "warm up"

    # TODO support input from Sense HAT
    input("Hit ENTER to take a photo")

    print("Taking photo")
    cam.capture("images/image_%s.jpg" %
                datetime.now().strftime("%Y-%m-%d_%H%M%S"), quality=100)

    # TODO Show photo taken & ask for confirmation to keep it?
    # TODO allow to take another photo to overwrite previous one?

    cam.stop_preview()
