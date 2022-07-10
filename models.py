from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    email: str = None
    name: str = None


class SignupForm(User):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str
