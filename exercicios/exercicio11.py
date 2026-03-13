# 11️ Contador de Letras
#Peça uma frase e conte quantas letras ela possui **sem contar espaços**.

total = 0

frase = (input("Digite uma palvra: "))

for letras in frase:
    if letras != " ":
        total +=1

print("A quantidade de letrar na sua palavra é: ", total)