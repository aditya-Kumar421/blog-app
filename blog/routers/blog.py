from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from blog import schemas, models
from blog.database import get_db
from sqlalchemy.orm import Session
from ..repository.blog import get_all, create_blog, show_blog, update_blog, destroy_blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/', response_model = List[schemas.ShowBlog] )
def all(db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_all(db)


@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return create_blog(request, db)


@router.get('/{id}', status_code= 200, response_model= schemas.ShowBlog)
def show(id:int, db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return show_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return update_blog(id, request, db)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return destroy_blog(id, db)
