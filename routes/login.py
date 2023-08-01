import json
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

# add the parent folder path
import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac

# class body(BaseModel):
class fid(BaseModel):
    fid: Union[str, None] = None
class body(BaseModel):
    d_id: str

# class response(BaseModel):
#     status: str

res =  {
    "status": "false"
}

router = APIRouter()

# res = json.dumps(res)
@router.get("/login")
async def login(fid: fid, body: body):
    # id = getMac.get_mac
    id = getMac.send_mac()
    print("fid >>>>>> ", fid)
    print("body >>>>>> ", body)
    print(body.d_id)
    if(body.d_id == id):
        res["status"] = "success"
        
        print("success")
    # print("id >>>>>> ", id)
    # f = json.dumps(response)
    # print(f)
    return res
