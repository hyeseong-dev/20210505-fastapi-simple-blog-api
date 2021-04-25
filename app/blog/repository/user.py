from fastapi import HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from blog import schemas,models
from utils import hasing
from blog import database


def get_all(db:Session):
    users = db.query(models.User).all()
    return users

def get_one(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={'detail' : f'User with the id, {id} is not available'}
    )
    return user

def create(request: schemas.User, db: Session):
    hashed_pw = hasing.Hash.bcrypt(request.password)
    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashed_pw,
     )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update(id:int, request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
   
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={'detail' : f'User with the id, {id} is not available'}
        )
    user.update(dict(request),synchronize_session = False)
    db.commit()
    return '변경 완료'

def delete(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    print(user)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={'detail' : f'Blog with the id, {id} is not available'}
        )
    user.delete(synchronize_session=False)
    db.commit()
    return '삭제완료'

