from fastapi import FastAPI

app = FastAPI()

@app.get("/notifications")
def notification(filter:str):
    return {"message": f"Notification: {filter}"}

# http://127.0.0.1:8000/notifications?filter=14 August Holiday
# Put ? to give parameters