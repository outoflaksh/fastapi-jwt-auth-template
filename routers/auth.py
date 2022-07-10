from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from utils.users_utils import get_user, verify_user, hash_password

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


@router.post("/register", status_code=201)
def create_user(form_data: SignupForm = Depends()):
    user = get_user(form_data.username, users_db)

    if user:
        raise HTTPException(status_code=400, detail="Username already in use!")

    # user doesn't already exist
    hashed_password = hash_password(form_data.password)
    user = UserInDB(
        username=form_data.username,
        name=form_data.name,
        email=form_data.email,
        hashed_password=hashed_password,
    )

    users_db.append(dict(user))

    return {"detail": "User created successfully!"}


@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data, users_db)
    print(hash_password(form_data.password))

    if user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password!")

    return {"access_token": user.username, "token_type": "bearer"}
