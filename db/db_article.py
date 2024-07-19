from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DBArticle
from db.schemas import ArticleBase


# Create Article
def create_article(db: Session, request: ArticleBase):

    new_article = DBArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.user_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


# Create Article
def create_comment(db: Session, request: ArticleBase):
    pass


# Get all Articles
def get_all_articles(db: Session):
    return db.query(DBArticle).all()


# Get Article by ID
def get_article(db: Session, id: int):
    article =  db.query(DBArticle).filter(DBArticle.id == id).first()

    if not article:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"article with ID: {id} not found"
            )

    return article


# Get Article by User.id
# def get_article(db: Session, id: int):
#     return db.query(DBArticle).filter(DBArticle.user_id == id).first()