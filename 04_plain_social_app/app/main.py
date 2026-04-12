from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "id": 1},
            {"title": "Post 2", "content": "Content of post 2", "published": False, "id": 2},
            {"title": "Post 3", "content": "Content of post 3", "published": True, "id": 3}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    my_posts.append(post.dict())
    return {"message": "Post created successfully", "post": post.dict()}

@app.get("/posts")
def get_posts():
    return {"All Posts": my_posts}

@app.get("/posts/latest")
def get_latest_posts():
    latest_posts = my_posts[-1] if my_posts else None
    return {"Latest Posts": latest_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if post:
        return {"Post": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = find_post(id)
    if post:
        my_posts.remove(post)
        return {"message": f"Post with id {id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")