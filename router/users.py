from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.schemas import UserBase, UserDisplay, UserUpdate
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)



# Create user
@router.post('/new', response_model=UserDisplay)
def create_user(request: UserBase, db: Session=Depends(get_db)):
    return db_user.create_user(db, request)

# Get all users
@router.get('/all', response_model=List[UserDisplay])
def all_users(db: Session=Depends(get_db)): 
    return db_user.all_users(db) 

# Get one user
@router.get(
        '/{id}', 
        summary=['Get User by it ID'],
        response_model=UserDisplay
        )
def all_users(id: int, db: Session=Depends(get_db)):

    user = db_user.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user
@router.put('/{id}', response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    updated_user = db_user.update_user(db, id, request)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user



# Partial update of user 
@router.patch('/{id}')
def patch_user(id: int, request: UserUpdate, db: Session = Depends(get_db)):
    updated_user = db_user.patch_user(db, id, request)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user



# Delete user
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    success = db_user.delete_user(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

