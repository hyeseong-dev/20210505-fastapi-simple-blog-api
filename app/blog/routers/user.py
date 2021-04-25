from typing import List
from fastapi import APIRouter, Depends, status, Response

from sqlalchemy.orm import Session
from passlib.context import CryptContext

from utils import hasing, oauth2
from .. import schemas, database, models
from ..repository import user



get_db = database.get_db

router = APIRouter(
    prefix='/users',
    tags=['Users'],
    # dependencies=[Depends(get_token_header)],
    # response={404:{"description":"Not Found"}},
)

@router.get('/', response_model=List[schemas.ShowUser], status_code=200)
def retrieve_all(db:Session=Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def retrieve_one(id:int, response: Response, db:Session=Depends(get_db)):
    return user.get_one(id, db)

@router.post('/', response_model=schemas.ShowUser, status_code=201)
def create(request: schemas.User, db: Session=Depends(get_db)):             
    return user.create(request, db)

@router.put('/{id}', status_code=202)
def update(id:int, response:Response, request:schemas.User, db:Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   
    return user.update(id, request, db)

@router.delete('/{id}', status_code=204)
def destroy(id:int, response: Response, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.delete(id,db)

