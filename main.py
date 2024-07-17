from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response

from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {
        "message": "Hello world!"
    }


