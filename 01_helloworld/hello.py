from fastapi import FastAPI, Request

app: FastAPI = FastAPI()

@app.get("/")
def index_root():
    return {"message": "Hello World"}

@app.get("/{name}")
def hi_name(name: str):
    return {"greet": f"Hi {name}! How are you."}