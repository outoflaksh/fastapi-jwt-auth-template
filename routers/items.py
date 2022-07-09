from fastapi import APIRouter, Depends

from . import auth

router = APIRouter()

items = ["apple", "mango", "banana"]


@router.get("/")
def read_items(token: str = Depends(auth.oauth2_scheme)):
    return {"results": items}
