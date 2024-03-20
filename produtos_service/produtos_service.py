from fastapi import FastAPI
import uuid
app = FastAPI()

produto = {}


def carregar_produtos():
    file = open("produtos_services.txt", "r")
    produtos = file.read().splitlines()
    return produtos

@app.post("/produtos/{nome}&{preco}/add")
async def criar_produto(nome: str, preco: float):
    produto["id"] = str(uuid.uuid4()) 
    produto["nome"] = nome
    produto["preco"] = preco
    file = open("produtos_services.txt", "a")
    file.write(f"{produto}\n")
    file.close()
    return {"Produto criado com sucesso"}

@app.get("/produtos")
async def listar_produtos():
    return carregar_produtos()