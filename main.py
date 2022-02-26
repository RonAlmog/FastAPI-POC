import string
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'hoo'}


@app.get('/about')
def about():
    return {'data': 'about'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

# query params /clients?limit=10&page=2'


@app.get('/clients')
def queryparams(limit: int = 10, page: int = 1, sort: Optional[str] = None):
    return {'limit': limit, 'page': page}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': 'blog comments for ' + id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def createblog(request: Blog):
    return request
    return {'data': 'xx'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
