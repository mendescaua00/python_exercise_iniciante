# 2️ Maior de Três Números
#Peça **3 números** ao usuário e mostre qual é o maior.

maior = 0

for x in range(3):
    numero = int(input("Digite um número: "))
    
    if numero > maior:
        maior = numero

print("O maior número digitado foi:", maior)