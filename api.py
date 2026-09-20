from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

# inicia a API
app = FastAPI()

# molde do que esperamos recever da internet
class RequestPassword (BaseModel):
    password_typed: str

# a rota (Endpoint) - é o endereço que a internet vai chamar
@app.post("/validar-senha")
def validate(dados: RequestPassword):

    # a senha que chegou pela internet usando o nosso molde
    user_password = dados.password_typed

    with sqlite3.connect('dados.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM leaks WHERE senha = ?", (user_password,))
        resultado = cursor.fetchone()

        #verificaçao do tamanho da senha 
        if len(user_password) < 8:
            return {"status": "erro", "mensagem": "Senha muito curta!"}
        #verifica se a existe e retona none
        elif resultado is not None:
            return {"status": "erro", "mensagem": "Senha muito fraca!"}
        else:
            return {"mensagem": "Senha cadastrada com sucesso!"}