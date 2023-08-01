import json
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

# add the parent folder path
import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac
from func import auth

# class body(BaseModel):
class fid(BaseModel):
    fid: Union[str, None] = None   
class body(BaseModel):
    d_id: str
    user: str
    user_id: str

# class response(BaseModel):
#     status: str


router = APIRouter()

# res = json.dumps(res)
@router.get("/login")
async def login(fid: fid, body: body):
    # define all variable
    res = {
        "respstatus":{
            "rcode" : "",
            "rmsg" : ""
        },
        "respdata" : {        
        }
    }
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
                token = auth.get_token({"payload" :body.user+body.user_id})
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
