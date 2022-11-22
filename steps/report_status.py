import os
from time import sleep
from helpers import sense


def report_status():
    duplicates_dir = "images/duplicates/"

    # Determine result of scanning for duplicates
    duplicates = [name for name in os.listdir(
        duplicates_dir) if os.path.isfile(os.path.join(duplicates_dir, name))]

    num_duplicates_found = len(duplicates)
    if (num_duplicates_found > 0):
        print(f"{num_duplicates_found} duplicates found:")
        for duplicate in duplicates:
            print(f"- {duplicate}")

        sense.duplicates_found()
        sense.wait_for_stick_input()  # Wait for user to confirm
    else:
        print("No duplicates found")
        sense.no_duplicates_found()
        sleep(2)
