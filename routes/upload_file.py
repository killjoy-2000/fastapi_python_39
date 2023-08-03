from fastapi import APIRouter, UploadFile, File
from typing import Union
from typing_extensions import Annotated
import shutil

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    # try:
    #     data = await file.read(2*1024*1024)
    #     await file.close()
    #     # print(data)
    # except Exception as e:
    #     print(str(e))
    print(file.filename)
    print(file.size)
    with open(file.filename, 'wb') as f:
        shutil.copyfileobj(file.file, f)
        shutil.move(file.filename, 'recv_files')
    return {"res" : "read file"}