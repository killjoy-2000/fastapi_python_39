import json
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac
from func import auth

router = APIRouter()

class fid(BaseModel):
    fid: Union[str, None] = None   
class body(BaseModel):
    d_id: str
    user: str
    user_id: str
@router.post("/val")
async def val(fid: fid, body: body):
    