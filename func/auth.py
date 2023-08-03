import jwt
import json
from datetime import datetime

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac


def get_token(payload):
    # print(type(payload))

    # pay = json.dumps(payload.__dict__)
    token = jwt.encode(payload, str(getMac.get_mac()[1]), algorithm="HS256")
    return token
# print(get_token())

# def check_token():
#     # try:
#     token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyIiOiJmMTRiMTRiYjYxMjRiZGIyZGJjMTA3NmQ5OTY1YTcwNzIzOTM3MDJlMWU3NzkzNjVlMjFlNTQ1NmE2MDVjYmNhIn0.zfBDymWsMDTUGzbfF_dQ9jh56LwQb3V_MPJIaKWIF4U"
#     val = jwt.decode(token, getMac.get_mac()[0], algorithms="HS256")
#     return val
# print(check_token())

# here get multiple return and print only the required one
# print(getMac.get_mac()[1])

def generate_token():
    token = jwt.encode({"":getMac.get_mac()[1]}, getMac.get_mac()[0], algorithm="HS256")
    return token
# print(generate_token())