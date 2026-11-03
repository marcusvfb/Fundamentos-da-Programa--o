"""
Entre 3 aspas, tudo que eu escrever vira comentário

Crie um sistema que pessa o usuário para digitar uma senha para acesso de sua conta bancária. Ele tem apenas 3 tentativas para acerta a senha. 
Se ele errar 3x, o sistema bloqueia a conta. 

regras:
1- A senha correta 1234.
2- O usuário tem 3 tentativas. - input()
3- Errou 3x. Conta bloqueada.
"""
# Variáveis no escopo global.
SENHA_CORRETA = "1234" # Constante, boa prática em python. 
tentativas = 3 # Uma variável contadora, poder ser i ou j.

while tentativas > 0: # Voc~E poderia colocar também while True - daria no mesmo. 
    senha = input("Digite a sua senha: ") # variável no escopo local
    if senha == SENHA_CORRETA:
        print("🔓 Acesso autorizado. Bem-Vindo 007")
        break # Comando que finaliza o loop do While.
    else:
        tentativas -= 1 #tentativas = tentativas - 1 <- Dá no mesmo.
        print(f"🔒 Acesso negado. Apenas mais {tentativas} tentativas restantes.") 
    if tentativas == 0:
        print("Este dispositivo será destruido em 5 segundos.")

