from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext

from models import User, UserInDB, SignupForm

# Auth flow: username and password are sent once and then a token is returned,
# which then has to be included in the headers of any protected route

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users_db = [
    {
        "username": "user1",
        "email": "user@email.com",
        "name": "user1",
        "hashed_password": "$2b$12$bTuZG0mNK2ciF1U2viC1YOuiV6cG2FCIzd..wXMBfpqnQCYbzlm6q",
    }
]


@router.post("/register")
def create_user(form_data: SignupForm = Depends()):

    return {"msg": "OK"}


# Utils


def hash_password(password: str):
    passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return passwd_context.hash(password)


def verify_hash(password_input, hashed_password):
    passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return passwd_context.verify(password_input, hashed_password)


def get_user(username: str, db):
    for user in db:
        if user["username"] == username:
            return UserInDB(**user)
    return None


def verify_user(form_data):
    user = get_user(form_data.username, users_db)

    if user:
        password_input = form_data.password
        hashed_password = user.hashed_password

        if verify_hash(password_input, hashed_password):
            return user


@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data)
    print(hash_password(form_data.password))

    if user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password!")

    return {"access_token": user.username, "token_type": "bearer"}
