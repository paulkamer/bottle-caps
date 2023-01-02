from time import sleep
from datetime import datetime
from helpers.detect_sense_hat import detect_sense_hat
from helpers.sense import wait_for_stick_input


has_camera = True
try:
    from picamera import PiCamera
except Exception:
    has_camera = False
    pass


def wait_for_input():
    sense_hat_present = detect_sense_hat()
    if (sense_hat_present):
        print("Push Sense HAT joystick down to take a photo")
        wait_for_stick_input()
    else:
        input("Hit ENTER to take a photo")


def take_photo():
    if (has_camera == False):
        print('No camera')
        return

    with PiCamera() as cam:
        print("Starting up camera. Starting in 2 seconds...")
        cam.start_preview()

        sleep(2)  # Let camera "warm up"

        wait_for_input()

        print("Taking photo")
        cam.capture("images/image_%s.jpg" %
                    datetime.now().strftime("%Y-%m-%d_%H%M%S"), quality=100)

        # TODO Show photo taken & ask for confirmation to keep it?
        # TODO allow to take another photo to overwrite previous one?

        cam.stop_preview()
