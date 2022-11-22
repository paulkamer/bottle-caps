from helpers.print_message import print_message
import time


def countdown():
    for i in reversed(range(1, 4)):
        print_message(str(i))
        time.sleep(1)
