from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    items = relationship('DBArticle', back_populates='user')
    usr_comments = relationship('DBComment', back_populates='user')


class DBArticle(Base):
    __tablename__='articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String, index=True)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DbUser', back_populates='items')
    comments = relationship('DBComment', back_populates='article')


class DBComment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))
    user = relationship('DbUser', back_populates='usr_comments')
    article = relationship('DBArticle', back_populates='comments')