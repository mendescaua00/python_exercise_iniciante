#4️ Soma de 5 Números
#Peça **5 números** ao usuário e mostre a soma total.

soma = 0

for x in range(5):
    numero = int(input("Digite 5 numeros: "))
    soma += numero 

print("O resultado é: ", soma)
