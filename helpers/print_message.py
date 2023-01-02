from helpers.detect_sense_hat import detect_sense_hat


import warnings
warnings.simplefilter("always", Warning)

try:
    from sense_hat import SenseHat
    sense = SenseHat()
except Exception:
    pass


def print_message(message: str):
    print(message)

    sense_hat_present = detect_sense_hat()
    if (sense_hat_present):
        sense.clear()
        sense.show_message(message)
