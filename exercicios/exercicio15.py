#15️ Fatorial
#Peça um número e calcule o **fatorial** dele.

fatorial = 1

numero = int(input("Digite um numero: "))

for i in range(1, numero+1):
    fatorial = fatorial * i



print("O fatorial de", numero, "é", fatorial)
    