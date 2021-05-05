from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.routing import Host
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Alex'}}


@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}


#if __name__ == "__main__":
#    uvicorn.run(app, host = "127.0.0.1", port = '8000')