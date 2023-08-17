from fastapi import APIRouter, UploadFile, File, Request
from typing import Union
from typing_extensions import Annotated
import shutil

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import auth

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile, request: Request):
    # try:
    #     data = await file.read(2*1024*1024)
    #     await file.close()
    #     # print(data)
    # except Exception as e:
    #     print(str(e))

    # variable
    res = {
        "respstatus":{
            "rcode" : "",
            "rmsg" : ""
        },
        "respdata" : {        
        }
    }

    # get token
    token = request.headers.get("token")
    ip = request.client.host
    # validate token
    val = auth.validate_token(token, ip)
    print(val)
    if val["status"] == True:
        print(file.filename)
        print(file.size)
        try:
            with open(file.filename, 'wb') as f:
                shutil.copyfileobj(file.file, f)
                shutil.move(file.filename, 'recv_files')
                res["respstatus"]["rcode"] = "000"
                res["respstatus"]["rmsg"] = "success"
            return res
            # break
        except Exception as e:
            print(str(e))
            res["respstatus"]["rcode"] = "FUP002"
            res["respstatus"]["rmsg"] = "File already exists"
            return res
            # break
    
    elif val["status"] == False:
        res["respstatus"]["rcode"] = "FUP001"
        res["respstatus"]["rmsg"] = "failed to validate token"
        print(val["body"])
        return res