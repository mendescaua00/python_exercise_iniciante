# 14️ Maior Número de uma Lista
#Peça **5 números**, guarde em uma lista e mostre o **maior número**.

numeros = []

for x in range(5):
    resposta = int(input(f"Digite o número: "))
    numeros.append(resposta)

maior = max(numeros)

print (maior)
