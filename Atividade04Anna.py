pin=12345
tentativas=1
resposta="Excesso de tentativas, login bloqueado."
while tentativas<=3:
    senha=int(input("Digite sua senha: "))
    if senha==pin:
        resposta="Login efetuado com sucesso!"
        break
    tentativas+=1
print(resposta)