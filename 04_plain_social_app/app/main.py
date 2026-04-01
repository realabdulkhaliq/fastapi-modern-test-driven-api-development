from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Post(BaseModel):
    title: str
    content: str
    Published: bool = True

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/createpost")
def create_post(post: Post):
    print(post)

@app.get("/posts")
def get_posts():
    return {"All Posts": "These are all the posts"}

@app.get("/posts/latest")
def get_latest_posts():
    return {"Latest Posts": "These are the latest posts"}
