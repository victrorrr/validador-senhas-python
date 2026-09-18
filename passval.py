with open ('leaks.txt', 'r', encoding='utf-8') as arquivo:
    wordlist = arquivo.read().splitlines()

#pede a senha do usuario
while True:
    user_password = input("Digite sua senha aqui! ")

    #verificaçao do tamanho da senha 
    if len(user_password) < 8:
        print("Senha muito curta!")
    #verifica senhas fracas
    elif user_password in wordlist:
        print("Senha fraca detectada!")
    else:
        print("Senha cadastrada com sucesso!")
        
        break