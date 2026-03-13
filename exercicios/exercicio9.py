## 9️ Média de Notas
#Peça **4 notas** e calcule a média.

#Regras:
#Média >= 7 → Aprovado
#Média < 7 → Reprovado

notas = 0

for x in range(4):
    nota = int(input("Digite suas 4 notas: "))
    notas += nota

media= notas/4

if media >= 7:
    print("você foi aprovado e sua média é: ", media)
else:
    print("você foi reprovado e sua média é: ", media)