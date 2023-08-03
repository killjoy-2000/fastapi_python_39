from fastapi import APIRouter, UploadFile, File
from typing import Union
from typing_extensions import Annotated

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    try:
        data = await file.read(2*1024*1024)
        await file.close()
        # print(data)
    except Exception as e:
        print(str(e))
    # print(file.filename)
    # print(file.size)
    return {"res" : "read file"}