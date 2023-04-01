from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {"data": {"name": "Gaurav"}}

@app.get("/about")
def about():
    return {"data": "My name is Gaurav"}