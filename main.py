from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response
from sqlalchemy import Engine

from router import blog_get, blog_post
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {
        "message": "Hello world!"
    }

models.Base.metadata.create_all(engine)