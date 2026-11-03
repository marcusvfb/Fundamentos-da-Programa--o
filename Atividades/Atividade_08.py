# Atividade em sala - 1

contagem = int(input("Digite um numero para acionar a contagem de autodestruição agente: "))

print(f"Contagem iniciada, autodestruição em {contagem}")

while contagem > 0:
    print(f"{contagem - 1}")
    contagem -= 1

print(f"""Obrigado pelos serviços 007. Boa sorte em sua missão.
    
    🔥🔥🔥🔥🔥🔥KAAAAAAAABOOOOOOOM!!!!!!!🔥🔥🔥🔥🔥🔥
    
    """)
    
# Atividade 2
    
while True:
    senha = input("""Bem-vido novo cliente, por favor crie uma senha, ela precisará ter: 
    
    ============
    8 caracteres
    ============
    
    Insira a senha:
    """)

    if len(senha) < 8: # Len é referente ao comprimento do texto.
        print("Senha invalida, a senha precisa ter no mínimo 8 caracteres.")
        continue
    else:
        print("Senha criada com sucesso.🔑")
        break

     