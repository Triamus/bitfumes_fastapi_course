from app.blog.routers import authentication
from fastapi import FastAPI
from app.blog.database import engine
from app.blog.routers import blog, user, authentication
from app.blog import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

