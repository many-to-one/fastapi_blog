from enum import Enum
from typing import Optional
from fastapi import APIRouter, Query, status, Response
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogCreate(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@router.post(
        '/new/{id}',
        summary=['Post a blog'], # For Swagger
        description='This api method post a blog', # For Swagger
        response_description="The blog you've posted", # For json response 
        )
async def create_blog(blog: BlogCreate, id: int, version: int=1):

    return {
        "msg": "The blog was created succesfully",
        "blog": blog,
        "id": id,
        "version": version
    }

@router.post(
        '/post_comment/{id}',
        summary=['Post a comment'], # For Swagger
        description='This api method post a comment', # For Swagger
        response_description="The comment you've posted", # For json response 
        )
async def create_comment(blog: BlogCreate, id: int, 
                            comment_id: int= Query(
                                None,
                                title="some title",
                                description="some description",
                                alias="You comment ID",
                                deprecated=True,
                            )
                         ):

    return {
        "msg": "The blog was created succesfully",
        "blog": blog,
        "id": id,
        "comment_id": comment_id
    }