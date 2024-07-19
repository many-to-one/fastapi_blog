from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DBComment
from db.schemas import CommentForm


# Create Article
def create_comment(db: Session, form_data: CommentForm):
    new_comment = DBComment(
        content=form_data.content,
        published=True,
        user_id=form_data.user_id,
        article_id=form_data.article_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


# # Create Article
# def create_comment(db: Session, request: ArticleBase):
#     pass


# # Get all Articles
# def get_all_articles(db: Session):
#     return db.query(DBArticle).all()


# # Get Article by ID
# def get_article(db: Session, id: int):
#     article =  db.query(DBArticle).filter(DBArticle.id == id).first()

#     if not article:
#         raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"article with ID: {id} not found"
#             )

#     return article


# Get Article by User.id
# def get_article(db: Session, id: int):
#     return db.query(DBArticle).filter(DBArticle.user_id == id).first()