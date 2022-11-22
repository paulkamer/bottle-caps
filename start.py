from helpers import sense
from steps import countdown
from steps import take_photo
from steps import report_status
from duplicateimagedetector.src import app as duplicates_detector
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),
            'config_duplicate_image_detector.ini'))

options = {
    'config': config,
}

countdown()
take_photo()

duplicates_detector(**options)

report_status()

sense.clear()
exit()
