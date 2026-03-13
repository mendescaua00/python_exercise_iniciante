# 13️ Sistema de Login
#Crie um sistema simples de login.

usuario = (input("Digite o usuário: "))
senha = (input("Digite a senha: "))

if senha != "1234" and usuario != "admin":
    print("Usuário e Senha errados")
elif senha != "1234":
    print("Senha errada")
elif  usuario != "admin":
    print("Usuário errado")
else:
    print("Acesso liberado")
    