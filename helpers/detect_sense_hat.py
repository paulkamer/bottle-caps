import os
import re

def detect_sense_hat():
    hat_product_path = "/proc/device-tree/hat/product"

    sense_hat_present = False

    if os.path.exists(hat_product_path):
        with open(hat_product_path) as hat_product:
            product = hat_product.readline()
            print(product)
    
            if re.match(r'sense', product.lower()):
                sense_hat_present = True

    return sense_hat_present