import json
from fastapi import APIRouter, Request
from typing import Union
from pydantic import BaseModel
import asyncio
# import openpyxl

# add the parent folder path
import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac
from func import auth
from session import activity

# class body(BaseModel):
class fid(BaseModel):
    fid: Union[str, None] = None   
class body(BaseModel):
    d_id: str
    user: str
    user_id: str
    image_no: Union[int, None] = None

# class response(BaseModel):
#     status: str


router = APIRouter()


# res = json.dumps(res)
@router.post("/login")
async def login(fid: fid, body: body, request: Request):
    s = activity.check_sts(request.client.host)
    print(s)
    # define all variable
    res = {
        "respstatus":{
            "rcode" : "",
            "rmsg" : ""
        },
        "respdata" : {        
        }
    }
    payload = {
        "user" : body.user,
        "used id" : body.user_id,
        "image" : body.image_no,
        "ip": request.client.host
    }
    if s == "available":
        res["respstatus"]["rcode"] = "100"
        res["respstatus"]["rmsg"] = "can not login again"
        return res
    token = ""
    # rcode = "000"
    # rmsg = ""
    try:
        # id = getMac.get_mac
        id = getMac.send_mac()
        print("fid >>>>>> ", fid)
        print("body >>>>>> ", body)
        # print(body.d_id)
    except Exception as e:
        print(str(e))
        res["respstatus"]["rcode"] = "FLG001"
        res["respstatus"]["rmsg"] = "failed to get mac"
    try:    
        if(body.d_id == id):
            res["respstatus"]["rcode"] = "000"
            res["respstatus"]["rmsg"] = "successfully validate device"            
            print("success")
            # here send the payload as json
            try:
                token = auth.get_token(payload)
                res["respdata"]["token"] = token
            except Exception as e:
                print(str(e))
                res["respstatus"]["rcode"] = "FLG004"
                res["respstatus"]["rmsg"] = "failed to get token"
        else:
            res["respstatus"]["rcode"] = "FLG002"
            res["respstatus"]["rmsg"] = "failed to validate device"
        # print("id >>>>>> ", id)
        # f = json.dumps(response)
        # print(f)
    except Exception as e:
        print(e)
        res["respstatus"]["rcode"] = "FLG003"
        res["respstatus"]["rmsg"] = str(e)
    
    finally:
        return res
