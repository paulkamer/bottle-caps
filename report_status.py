import os
from helpers import print_message

duplicates_dir = "./images/duplicates/"


# Determine result of scanning for duplicates
duplicates = [name for name in os.listdir(
    duplicates_dir) if os.path.isfile(os.path.join(duplicates_dir, name))]

num_duplicates_found = len(duplicates)
if (num_duplicates_found > 0):
    print_message(f"{num_duplicates_found} duplicates found:")

    for duplicate in duplicates:
        print_message(f"- {duplicate}")
else:
    print_message("No duplicates were found")
