from sqlalchemy.orm import Session
from db.hash import Hash
from db.models import DbUser
from db.schemas import UserBase, UserUpdate


# CREATE USER
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# GET ALL USERS
def all_users(db: Session):
    return db.query(DbUser).all()

 # GET USER BY ID
def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

# UPDATE USER
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        return None  # Or raise an exception

    user.username = request.username
    user.email = request.email
    user.password = request.password  # if password needs to be updated

    db.commit()
    db.refresh(user)

    return user


# UPDATE USER BY A REQUESTED VALUE
def update_user_partial(db: Session, id: int, request: dict) -> DbUser:
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        return None  # Or raise an exception

    # Update only the fields that are provided in the request
    if "username" in request:
        user.username = request["username"]
    if "email" in request:
        user.email = request["email"]
    if "password" in request:
        user.password = Hash.bcrypt(request["password"])  # Hash the new password

    db.commit()
    db.refresh(user)

    return user


# DELETE USER
def delete_user(db: Session, id: int) -> bool:
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        return False  # Or raise an exception
    
    db.delete(user)
    db.commit()
    
    return True