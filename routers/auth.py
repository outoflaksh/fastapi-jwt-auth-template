from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import User, UserInDB, SignupForm

# Auth flow: username and password are sent once and then a token is returned,
# which then has to be included in the headers of any protected route

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = []


@router.post("/register")
def create_user(form_data: SignupForm = Depends()):
    users.append(dict(form_data))
    print(users)
    return {"msg": "OK"}


@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username, "token_type": "bearer"}


@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"token": token}
