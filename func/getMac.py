# this function will get device mac id

import uuid

def send_mac():
    mac = uuid.getnode()
    return mac

print("mac id is >>>>> ", send_mac())