from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "My First api in FastAPI"}