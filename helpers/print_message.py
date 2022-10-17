import sys
from sense_hat import SenseHat
from helpers import detect_sense_hat


def print_message(message: str):
    print(message)

    sense_hat_present = detect_sense_hat()
    if (sense_hat_present):
        sense = SenseHat()
        sense.show_message(message)


if __name__ == "__main__":
    message = sys.argv[1]

    print_message(message)
