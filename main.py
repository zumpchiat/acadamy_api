from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional,List


app = FastAPI()

academias = [{
    "id": 1,
    "nome": "Team Neves",
    "responsavel_tecnico": "Nelson Gonçalves",
    "fundacao": "1990",
    "criado_at" : "2014-06-15" 
},
{
    "id": 2,
    "nome": "Team Caveira",
    "responsavel_tecnico": "Anderson Almeida",
    "fundacao": "2013",
    "criado_at" : "2016-04-05" 
},
{
    "id": 3,
    "nome": "Team Carneiro",
    "responsavel_tecnico": "Marcos Carneiro",
    "fundacao": "2018",
    "criado_at" : "2018-08-12"
}
]
class Academia(BaseModel):
     id: int
     nome : str
     responsavel_tecnico : str
     fundacao : str
     criado_at : str

# Get /api/academias
@app.get("/api/academias", response_model=List[Academia])
async def get_all_academias():
    return academias
    

# Get /api/academias/id
@app.get("/api/academias/{id}")
async def get_academia(id:int) -> dict:
    for academia in academias:     
        if academia["id"] == id:
            return academia
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Academia não encontrada!")

# Post /api/academias
@app.post("/api/academias/", status_code=status.HTTP_201_CREATED)
async def create_academia(academia_data: Academia) -> dict:
    new_academia = academia_data.model_dump()

    academias.append(new_academia)

    return new_academia





