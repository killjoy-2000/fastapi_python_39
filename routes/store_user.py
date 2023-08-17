from fastapi import APIRouter, Header, Request
from typing import Union
from typing_extensions import Annotated
import openpyxl
from openpyxl.utils import get_column_letter
from pydantic import BaseModel

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import auth,user

router = APIRouter()

class signature(BaseModel):
    fid: str 
class body(BaseModel):
    d_id: str
    user: str
    user_id: str
    image_no: Union[int, None] = None
    image_consumed: Union[int, None] = None
    tag: bool

@router.post("/add_data")
async def add_data(request: Request, signature: signature, body: body):
    try:
        # print(token)

        # variable
        res = {
            "respstatus":{
                "rcode" : "",
                "rmsg" : ""
            },
            "respdata" : {        
            }
        }
        # val = auth.validate_token(token)
        # if(val["status"] == True):
        #     print(val["body"])
        #     # print(val)
        #     return val
        # if(val["status"] == False):
        #     return {
        #         "sts": "fk"
        #     }
        if(signature.fid != "F-AU001"):
            res["respstatus"]["rcode"] = "FAU001"
            res["respstatus"]["rmsg"] = "Not a valid call"
            return res
        # print(body)
        # return res
        elif signature.fid == "F-AU001":
            token = request.headers.get("token")
            ip = request.client.host
            val = auth.validate_token(token, ip)

            if(val["status"] == False):
                res["respstatus"]["rcode"] = "FUP002"
                res["respstatus"]["rmsg"] = "failed to validate token"
                return res
            
            elif(val["status"] == True):     
                print(body)
                sts = user.add_user(body)
                print(sts)
                if sts == "user_exist":
                    res["respstatus"]["rcode"] = "FUP003"
                    res["respstatus"]["rmsg"] = "user already exists"
                    return res
                elif sts:
                    res["respstatus"]["rcode"] = "000"
                    res["respstatus"]["rmsg"] = "User added successfully"
                    return res
    except Exception as e:
        print(str(e))
        res["respstatus"]["rcode"] = "600"
        res["respstatus"]["rmsg"] = str(e) + " >>>>>>>>>>> contact support"
        return res

        

