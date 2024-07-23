from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Engine

from auth import authentication
from router import blog_get, blog_post, users, articles, comments
from db import models
from db.database import engine

app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(articles.router)
app.include_router(comments.router)

@app.get('/')
def index():
    return {
        "message": "Hello world!"
    }

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)