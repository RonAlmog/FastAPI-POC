from typing import List
from urllib import request
from fastapi import APIRouter,  Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from blog import database
from .. import schemas, database, models, oauth2
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=['blogs'])
def getall(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, requst: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def getall(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
