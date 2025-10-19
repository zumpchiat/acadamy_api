from fastapi import FastAPI

app = FastAPI()

#Endpoint basic
@app.get("/")
def read_root():
    return {"message" : "My First api in FastAPI"}


# Path Parameters
@app.get("/greet/{username}")
async def greet(username:str):
    return {"message": f"Hello {username}"}

