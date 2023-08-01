import jwt
import json

def get_token(payload):
    # print(type(payload))

    # pay = json.dumps(payload.__dict__)
    token = jwt.encode(payload, "secret", algorithm="HS256")
    return token
# print(get_token())