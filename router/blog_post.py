from enum import Enum
from typing import Annotated, Dict, List, Optional
from fastapi import APIRouter, Body, Path, Query, status, Response
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogCreate(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[Image] = None


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
        '/post_comment/{id}/comment_id/{comment_id}',
        summary=['Post a comment'], # For Swagger
        description='This api method post a comment', # For Swagger
        response_description="The comment you've posted", # For json response 
        )
async def create_comment(blog: BlogCreate, id: int, 
                            # for Swagger:
                            comment_title: str= Query(
                                None,
                                title="some title",
                                description="some description",
                                alias="You comment Title",
                                deprecated=True,
                            ),
                            # comment: str = Body('Hi there!') # Default comment
                            comment: str = Body(...,
                                                min_length=10,
                                                max_length=255,
                                                regex='^[a-z\\s*$]' # only little letters; '[a-z\\s*$]' - with big letter
                                                ),
                            # v: not necessary
                            v: Optional[List[str]] = Query(None), 
                            # v: Optional[List[str]] = Query(['0.1', '0.2', '0.3']), # default parameters
                            comment_id: int = Path(title="The ID of the item to get", ge=0, le=1000) # this title will be in the link-path with comment_id
                         ):

    return {
        "msg": "The blog was created succesfully",
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "comment": comment,
        "comment_id": comment_id,
        "values_in_link_as_query": v,
    }

def required_functionality():
    return {'Some important data'}