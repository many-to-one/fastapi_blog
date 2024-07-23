from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from auth import oauth2
from db.database import get_db
from db.models import DbUser
from db.hash import Hash

router = APIRouter(
    # prefix='/authentication',
    tags=['authentication']
)

@router.post('/token')
def get_token(
        request: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
    ):

    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid credentials'
        )
    if not Hash.verify(user.password, request.password):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Incorrect password'
        )
    
    access_token = oauth2.create_access_token(data={'sub': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username,
    }
    