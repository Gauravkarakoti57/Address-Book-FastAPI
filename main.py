from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# class Blog(BaseModel):
#     title : str
#     body : str

@app.get("/")
def index():
    return {"data": {"name": "Gaurav"}}

@app.get("/about")
def about():
    return {"data": "My name is Gaurav"}

# @app.post("/blog")
# def create(blog: Blog):
#     return {"data": f"Data is created {blog.title}"}