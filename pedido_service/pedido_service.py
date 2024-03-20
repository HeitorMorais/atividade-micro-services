from fastapi import FastAPI
import uuid
app = FastAPI()

pedido = {}

def carregar_pedidos():
    file = open("pedido_service.txt", "r")
    pedidos = file.read().splitlines()
    return pedidos

@app.post("/pedido/{user_id}/add")
async def criar_pedido(user_id: int):
   pedido["order_id"] = str(uuid.uuid4())
   pedido["user_id"] = user_id
   file = open("pedido_service.txt", "a")
   file.write(f"{pedido}\n")
   file.close()
   return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": pedido["order_id"]}

@app.get("/pedidos")
async def listar_pedidos():
    return carregar_pedidos()