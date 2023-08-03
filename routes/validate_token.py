# this file is for testing purposes only

from fastapi import APIRouter,Header
from typing import Union
from typing_extensions import Annotated

import sys
sys.path.append('/home/aritra/KaBooM/deja VU/python-test/fastapi-test-p39-v2/')
from func import auth


router = APIRouter()

@router.post("/validate")
async def validate(token: Annotated[Union[str, None], Header()] = None):
    print(token)
    val = auth.validate_token(token)
    print(val)
    return val