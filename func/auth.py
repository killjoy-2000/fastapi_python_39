import jwt
import json

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac


def get_token(payload):
    print(type(payload))

    # pay = json.dumps(payload.__dict__)
    token = jwt.encode(payload, str(getMac.get_mac()), algorithm="HS256")
    return token
# print(get_token())

def check_token(token):
    # try:

    return

# here get multiple return and print only the required one
# print(getMac.get_mac()[1])

def generate_token():
    token = jwt.encode({"":getMac.get_mac()[1]}, getMac.get_mac()[0], algorithm="HS256")
    return token
print(generate_token())