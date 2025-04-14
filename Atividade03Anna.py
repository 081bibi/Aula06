n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
divisao=0
while n2 == 0:
    n2=int(input("Número inválido, não pode ser ZERO.\n"
                  "Digite novamente: "))
divisao = n1/n2
print(divisao)