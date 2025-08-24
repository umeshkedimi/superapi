from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},{"title": "title of post 2", "content": "content of post 2", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Welcome Umesh!"}

@app.get("/posts/{id}")
async def get_post_by_id(id: int):
    for post in my_posts:
        if post['id'] == id:
            return {"post_detail": post}
    return {"message": f"post with id: {id} was not found"}

@app.get("/posts")
async def get_posts():
    return {"posts": my_posts}


@app.post("/posts")
async def create_post(post: Post):
    new_post = post.dict()
    new_post['id'] = randrange(0, 1000000)
    my_posts.append(new_post)
    return {"Response": new_post}