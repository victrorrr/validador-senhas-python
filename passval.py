import sqlite3 

#  o bloco 'with' gerencia a abertura e fechamento automaticamente
with sqlite3.connect('dados.db') as conexao:
    cursor = conexao.cursor()

    #pede a senha do usuario
    while True:
        user_password = input("Digite sua senha aqui: ")
        #vai no banco de dados verifica se a senha existe
        cursor.execute("SELECT * FROM leaks WHERE senha = ?", (user_password,))
        resultado = cursor.fetchone()

        #verificaçao do tamanho da senha 
        if len(user_password) < 8:
            print("Senha muito curta!")
        #verifica se a existe e retona none
        elif resultado is not None:
            print("Senha fraca detectada!")
        else:
            print("Senha cadastrada com sucesso!")
            break