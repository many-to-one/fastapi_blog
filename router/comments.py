from typing import List
from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.schemas import CommentDisplay, CommentForm
from db import db_comments


router = APIRouter(
    prefix='/comments',
    tags=['comments']
)


# Create a Comment
@router.post('/new_comment', response_model=CommentDisplay)
def create_comment(form_data: CommentForm = Depends(CommentForm), db: Session=Depends(get_db)):
    return db_comments.create_comment(db, form_data)