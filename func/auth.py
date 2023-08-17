import jwt
import json
from datetime import datetime, timedelta
from typing import Union
import openpyxl

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac
from session import activity


def get_token(payload):
    # print(type(payload))

    # pay = json.dumps(payload.__dict__)
    # payload['exp'] = int
    body = {
        "exp" : datetime.utcnow() + timedelta(seconds=3600),
        "body" : payload,
        "time" : str(datetime.now())
    }

    token = jwt.encode(body, str(getMac.get_mac()[1])+datetime.today().strftime("%Y-%m-%d"), algorithm="HS256")
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

def validate_token(token,ip):
    res = {
        "status" : bool,
        "body": str
    }
    try:
        val = jwt.decode(token, str(getMac.get_mac()[1])+datetime.today().strftime("%Y-%m-%d"), algorithms="HS256")
        res["status"] = True
        res["body"] = val
        return res
    except Exception as e:
        print(str(e))
        activity.change_activity(ip)
        res["status"] = False
        res["body"] = str(e)
        return res

    # return val