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

# Query Parameters
# http://localhost:8000/search?username=Pedro

user_list = [
    "João",
    "Maria",
    "josé",
    "Pedro",
]

@app.get("/search")
async def search(username:str):
    for user in user_list:
        if username in user_list:
            return {"message": f" Seu usuário é {username}"}
        
        else:
            return {"message": f"Usuário não encontrado!!!"} 


#Optional Parameters

from typing import Optional

@app.get("/greetoptional")
async def greetoptional(username:Optional[str]="Convidado"):
    return {"message": f"Olá, {username}  como você está"}