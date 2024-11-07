from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    # orm_mode allows the system to return database data automatically into
    # the format provided above (UserDisplay username and email)
    # without that we get an error saying we can't convert from one type 
    # to another. So we can convert automatically from DbUser into UserDisplay
    class Config():
        orm_mode = True