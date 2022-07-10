from fastapi import APIRouter, Depends, HTTPException

from . import auth
from utils.token_utils import decode_access_token
from utils.users_utils import get_user

router = APIRouter()

items = ["apple", "mango", "banana"]


@router.get("/")
def read_items(token: str = Depends(auth.oauth2_scheme)):
    token_data = decode_access_token(token)

    if not get_user(token_data.username, auth.users_db):
        raise HTTPException(status_code=401, detail="Not authorized")

    return {"results": items}
