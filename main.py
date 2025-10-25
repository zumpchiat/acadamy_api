from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional,List


app = FastAPI()

academias = [{
    "id": 1,
    "nome": "Equipe BRAE",
    "responsavel_tecnico": "Mauro Gonçalves",
    "fundacao": "1990",
    "criado_at" : "2014-06-15" 
},
{
    "id": 2,
    "nome": "Equipe CRUA",
    "responsavel_tecnico": "Almeida",
    "fundacao": "2013",
    "criado_at" : "2016-04-05" 
},
{
    "id": 3,
    "nome": "Equipe Saboia",
    "responsavel_tecnico": "Magno ",
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

class AcademiaUpdate(BaseModel):
     nome : str
     responsavel_tecnico : str
     fundacao : str
     


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


#patch /api/academias/id
@app.patch("/api/academias/{id}")
async def update_academia(id: int, academia_update_data:AcademiaUpdate) -> dict:

    for academia in academias:
        if academia["id"] == id:
            academia["nome"] = academia_update_data.nome
            academia["responsavel_tecnico"] = academia_update_data.responsavel_tecnico
            academia["fundacao"] = academia_update_data.fundacao
          
            return academia
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Academia não encontrada!")


#Delete /api/academias/id
@app.delete("/api/academias/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_academia(id: int):
    
    for academia in academias:
        if academia["id"] == id:
            academias.remove(academia)
            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Academia não encontrada!")


