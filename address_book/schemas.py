from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    body : str

class ShowBlog(Blog):
    
    class Config:
        orm_mode = True


class User(BaseModel):
    name : str
    password : str
    email : str
    

class ShowUser(BaseModel):
    name : str
    email : str
    class Config:
        orm_mode = True