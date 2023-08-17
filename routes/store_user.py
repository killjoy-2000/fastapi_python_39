from fastapi import APIRouter, Header, Request
from typing import Union
from typing_extensions import Annotated
import openpyxl
from openpyxl.utils import get_column_letter
from pydantic import BaseModel

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import auth

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
        res["respstatus"]["rcode"] = "000"
        res["respstatus"]["rmsg"] = "valid call"
        return res

