from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "id": 1},
            {"title": "Post 2", "content": "Content of post 2", "published": False, "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

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
