#5️ Tabuada
#Peça um número e mostre a **tabuada de 1 até 10**.

multi = 1

numero = int(input("Digite um numero: "))

for x in range(10):
    tabuada = numero * multi
    print(tabuada)
    multi += 1
