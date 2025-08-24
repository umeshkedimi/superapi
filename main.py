from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome Umesh!"}

@app.get("/posts")
async def get_posts():
    return {"posts": ["post1", "post2"]}