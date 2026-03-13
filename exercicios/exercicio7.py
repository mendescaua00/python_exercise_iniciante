#O computador escolhe um número **aleatório entre 1 e 10**.
#O usuário deve tentar adivinhar.

import random

numero = random.randint(1,10)

respsota = int(input("Digite um numero: "))

if respsota == numero:
    print("Você acertou")
else:
    print("você errou, o número era: ", numero)