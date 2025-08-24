from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome Umesh!"}

@app.get("/posts")
async def get_posts():
    return {"posts": ["post1", "post2"]}


@app.post("/posts")
async def create_post(payload: dict = Body(...)):
    print(payload)
    return {"Response": f"Post created with title {payload['title']}"}