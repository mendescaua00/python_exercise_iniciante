#6️ Contar Vogais
#Peça uma palavra e conte quantas **vogais** existem nela.

vogais = "aeiou" 
total = 0

palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in vogais:
        total += 1

print("Total de vogais na palavra: ", total)

