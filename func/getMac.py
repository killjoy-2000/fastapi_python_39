# this function will get device mac id

import uuid
import sys
import hashlib
import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')

def get_mac():
    mac = str(uuid.getnode())
    hash = hashlib.sha256(mac.encode()).hexdigest()
    hash = hash[:6]
    # fold_id = open(".sec/fold_id.aspic", "r", encoding='utf-8')
    # print(fold_id.read())
    with open(".sec/fold_id.aspic", "w", encoding='utf-8') as id:
        id.write(hash)
    return hash

# get_mac()

def send_mac():
    with open(".sec/fold_id.aspic", "r", encoding='utf-8') as id:
        fold_id = id.read()
    return fold_id