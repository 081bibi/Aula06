n1=float(input("Digite primeira nota: "))
while n1 <0 or n1 > 10:
    n1 = float(input("Valor Inválido!"
                  "Digite primeira nota:"  ))
n2=float(input("Digite segunda nota: "))
while n2 <0 or n2 > 10:
    n2 = float(input("Valor inválido! "
                     "Digite sua segunda nota"))
media = (n1+n2)/2
print(media)
