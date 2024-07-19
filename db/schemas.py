from typing import List, Optional
from pydantic import BaseModel


# Artical inside UserDisplay
class Article(BaseModel):
    id: int
    title: str
    content: str
    published: bool

    class Config():
        from_attributes=True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: List[Article] = []
    
    class Config():
        from_attributes=True


# User data for ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config():
        from_attributes=True


class CommentForm(BaseModel):
    content: str
    user_id: int
    article_id: int

    class Config():
        from_attributes=True


class CommentBase(BaseModel):
    id: int
    content: str
    published: bool
    user_id: int
    article_id: int


class CommentDisplay(BaseModel):
    id: int
    content: str
    published: bool
    article: Article
    user: User

    class Config():
        from_attributes=True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: int


class ArticleDisplay(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    user: User

    class Config():
        from_attributes=True