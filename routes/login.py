from fastapi import APIRouter
# add the parent folder path
import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import getMac
router = APIRouter()


@router.get("/login")
async def login():
    # id = getMac.get_mac
    id = getMac.send_mac()
    # print("id >>>>>> ", id)
    return {"id" : id}
