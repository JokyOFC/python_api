from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
    
app = FastAPI()

class ItemTeste(BaseModel):
    nome: str
    idade: int

@app.get("/")   
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def teste():
    return {"teste": "teste"}

@app.post("/testparams")
async def testparams(item: ItemTeste):
    return {"parametros": item}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info") 
