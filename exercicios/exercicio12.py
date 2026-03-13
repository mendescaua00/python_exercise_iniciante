# 12️ Palíndromo
#Verifique se uma palavra é um **palíndromo**.

palavra = (input("digite uma palavra: "))

palindromo = palavra [::-1]

if palindromo == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

