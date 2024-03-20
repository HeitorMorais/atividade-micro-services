from fastapi import FastAPI, HTTPException

app = FastAPI()

def carregar_credenciais():
    file = open("login_service.txt", "r")
    credenciais = file.read().splitlines()
    return credenciais

@app.post("/login/{username}&{password}")
async def login(username: str, password: str):
    credenciais = carregar_credenciais()
    auth = {"username":credenciais[0], "password":credenciais[1]}
    if username == auth["username"] and password == auth["password"]:
        return {"status": "sucesso", "mensagem": "Usuário autenticado", "u": auth["username"], "p": auth["password"]}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")