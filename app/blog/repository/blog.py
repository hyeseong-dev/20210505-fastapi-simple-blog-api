from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas, models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_one(id:int, db:Session):
    blog =  db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail={'detail' : f'Blog with the id, {id} is not available'}
        )
    return blog

def create(request: schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session ):
    blog = db.query(models.Blog).filter(models.Blog.id==id)  
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={'detail' : f'Blog with the id, {id} is not available'}
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return '삭제 완료'

def update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={'detail' : f'Blog with the id, {id} is not available'}
        )
    blog.update(dict(request),synchronize_session = False)
    db.commit()
    return '변경 완료'