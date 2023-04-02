from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)




# @app.get("/")
# def index():
#     return {"data": {"name": "Gaurav"}}

# @app.post("/blog/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
    
#     new_blog = models.Blog(title = request.title, body = request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get("/all",status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}",status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
#                             f'Blog with the id {id} is not available')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f'Blog with the id {id} is not available'}
#     return blogs

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     print(blog)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
#                             f'Blog with the id {id} is not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f'Blog with the id {id} is not available'}
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return "deleted"

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
#                             f'Blog with the id {id} is not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f'Blog with the id {id} is not available'}
#     blog.update(request.dict())
#     db.commit()
#     return "updated"

# @app.post("/user/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
# def create(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name = request.name, password = hashing.Hash.bcrypt(request.password), email = request.email)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}",status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
#                             f'User with the id {id} is not available')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f'Blog with the id {id} is not available'}
#     return user