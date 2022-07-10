import os
from datetime import datetime, time, timedelta
from typing import Union
from jose import jwt, JWTError


# Env vars
from dotenv import load_dotenv

load_dotenv()

# Token config
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return access_token
