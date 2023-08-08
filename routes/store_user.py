from fastapi import APIRouter, Header
from typing import Union
from typing_extensions import Annotated
import openpyxl
from openpyxl.utils import get_column_letter

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import auth

router = APIRouter()

@router.post("/add_data")
async def add_data(token: Annotated[Union[str, None], Header()] = None):
    # print(token)
    val = auth.validate_token(token)
    if(val["status"] == True):
        print(val["body"])
        # print(val)
        return val
    if(val["status"] == False):
        return {
            "sts": "fk"
        }

