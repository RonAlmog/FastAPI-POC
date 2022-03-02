from typing import List
from fastapi import APIRouter,  Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from blog import database
from .. import schemas, database, models
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=['blogs'])
def getall(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')

    blog.update(dict(request))
    db.commit()
    return 'updated'


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def getall(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")

    return blog
