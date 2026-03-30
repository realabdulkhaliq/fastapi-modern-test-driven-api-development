from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"All Posts": "These are all the posts"}

@app.get("/posts/latest")
def get_latest_posts():
    return {"Latest Posts": "These are the latest posts"}
