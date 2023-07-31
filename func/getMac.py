# this function will get device mac id

import uuid
import sys
import hashlib

def get_mac():
    mac = str(uuid.getnode())
    hash = hashlib.sha256(mac.encode()).hexdigest()
    hash = hash[:6]
    return hash
