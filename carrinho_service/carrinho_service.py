from fastapi import FastAPI


app = FastAPI()

cart = {}

def carregar_carrinhos():
    file = open("carrinho_service.txt", "r")
    carrinhos = file.read().splitlines()
    return carrinhos

@app.post("/carrinho/{user_id}&{produto_id}&{quantidade}/add")
async def add_carrinho(user_id: int, produto_id: int, quantidade: int):
    cart[user_id] = {"produto_id": produto_id, "quantidade": quantidade}
    file = open("carrinho_service.txt", "a")
    file.write(f"{cart}\n")
    file.close()
    return {"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"}

@app.get("/carrinho")
async def mostrar_carrinhos():
    return carregar_carrinhos()