import sqlite3 

#  o bloco 'with' gerencia a abertura e fechamento automaticamente
with sqlite3.connect('dados.db') as conexao:
    cursor = conexao.cursor()

    #criando o arquivo de senhas vazadas 
    cursor.execute("CREATE TABLE IF NOT EXISTS leaks (senha TEXT)")
    cursor.execute("INSERT INTO leaks (senha) VALUES ('12345678')")
    cursor.execute("INSERT INTO leaks (senha) VALUES ('admin')")