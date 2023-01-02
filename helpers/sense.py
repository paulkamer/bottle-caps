import time

sense = None
try:
    from sense_hat import SenseHat
    sense = SenseHat()
except Exception:
    pass


def sense_present():
    return sense is not None


def wait_for_stick_input():
    if sense_present() is True:
        sense.clear()
        sense.set_pixel(7, 7, 0, 255, 0)
        sense.stick.wait_for_event()
        sense.clear()


def clear(color=None):
    if sense_present():
        if (color is not None):
            sense.clear(color)
        else:
            sense.clear()


def no_duplicates_found():
    clear((0, 255, 0))


def duplicates_found():
    clear((255, 0, 0))
