from typing import List, Optional
from fastapi import APIRouter, Cookie, Depends, Form, HTTPException, status, Header, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db.schemas import ArticleBase, ArticleDisplay
from db import db_article
from fastapi.encoders import jsonable_encoder
from auth.oauth2 import oauth2_scheme


router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create Article
@router.post('/new', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session=Depends(get_db)):
    return db_article.create_article(db, request)


# Get Article by ID
@router.get('/all', response_model=List[ArticleDisplay])
def get_all_articles(
        db: Session=Depends(get_db),
        token: str=Depends(oauth2_scheme)
    ):
    return db_article.get_all_articles(db)


# Get Article by ID (With custom headers, is not necessary)
@router.get('/{id}')
def get_article(
        id: 
        int, db: Session = Depends(get_db), 
        custom_header: Optional[str] = Header(None),
        test_cookie: Optional[str] = Cookie(None)
    ):

    article = db_article.get_article(db, id)

    headers = {"Custom-Resp-Headers": custom_header} if custom_header else {}
    # cookie = {"Custom-Cookie": test_cookie} if test_cookie else {}

    return {
        'content': article,
        'headers': headers,
        'cookie': test_cookie,
        'status_code': status.HTTP_200_OK
    }

    # Optional type of response if there is more than one
    # value in the response (headers for example)
    # response = JSONResponse(
    #     content=jsonable_encoder(article),
    #     headers=headers,
    #     cookie=test_cookie,
    #     status_code=status.HTTP_200_OK
    # )
    
    # Set cookies
    # response.set_cookie(key='key1', value='val1')

    # return response

    # return {
    #     'content': jsonable_encoder(article),
    #     'headers': headers,
    #     'cookie': test_cookie,
    #     'status_code': status.HTTP_200_OK
    # }
