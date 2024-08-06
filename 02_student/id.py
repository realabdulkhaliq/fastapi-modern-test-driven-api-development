from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(who:str, id:str = Body(embed=True)):
    return f"Hello? {who} with ID {id}?"