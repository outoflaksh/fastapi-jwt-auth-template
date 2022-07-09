from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str = None
    name: str = None


class SignupForm(User):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str
