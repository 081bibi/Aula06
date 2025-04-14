soma=0
x=0
alunos=int(input("Quantos alunos tem na sala? "))
while x<alunos:
    num=int(input("Digite a nota do aluno: "))
    soma= soma+num
    x=x+1
media=soma/alunos
print(media)