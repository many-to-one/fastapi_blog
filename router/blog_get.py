from enum import Enum
from typing import Optional
from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# @app.get('/all')
# def all_blogs():
#     return {
#         "blog all": "all"
#     }

# @app.get('/all')
# def all_blogs(page=1, page_size=5):
#     return {
#         "blog all page": f"{page}",
#         "blog all page_size": f"{page_size}",
#     }

@router.get(
        '/all',
        summary=['Receive all blogs'], # For Swagger
        description='This api method returns all blogs', # For Swagger
        response_description='The list of all blogs', # For json response 
        )
def all_blogs(page=1, page_size: Optional[int] = True):
    return {
        "blog all page": f"{page}",
        "blog all page_size": f"{page_size}",
    }

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def blog_type(type: BlogType):
    """
        Another type of description method
        - **type** here we need to put a type to this function
        - **smth** something else
        - **more** something more
    """
    return {
        "blog type": f"{type}"
    }

# @app.get('/blog/{id}')
# def index(id: int):
#     return {
#         "blog id": f"{id}"
#     }

@router.get('/{id}', status_code=status.HTTP_200_OK)
def index(id: int, response: Response):

    if id > 5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'message': f"Error {id}"}
    else:
        response.status_code=status.HTTP_200_OK
        return {
            "blog id": f"{id}"
        }

