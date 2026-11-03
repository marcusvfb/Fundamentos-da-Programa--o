# Atividade Banco Senac

limite_saques = 3
saldo = 1000 # Coloque aqui o valor hipotético para teste do sistema.
extrato = []

while True:
    print(f"""
    =======================
      MENU DO BANCO SENAC
    =======================
    Bem-vindo ao Banco Senac, 
    selecione uma opção:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [q] - Sair
    =======================    
    """)
    opcao = input("Selecione uma opção: ").lower()
    
    if not opcao in ["d", "s", "e", "q"]:
        print("Opção inválida! Por favor, selecione uma operação válida.")
        continue
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        
        if valor <= 0:
            print("Operação Falhou! O valor informado é inválido!")
        else:
            saldo += valor
            print(f"""
        Depósito de R${valor:.2f} realizado com sucesso!
        Seu saldo atual é de R${saldo:.2f}.
        """)
            print(f"\nObrigado por utilizar o Banco Senac!")
            extrato.append(f"Depósito: R${valor:.2f}")

    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))

        if saque > saldo:
            print("Operação Falhou! Você não tem saldo suficiente!")
        elif saque > 500:
            print("Operação Falhou! O valor do saque excede o limite permitido de R$500,00.")
        elif saque <= 0:
            print("Operação Falhou! O valor informado é inválido!")
        elif limite_saques <= 0:
            print("Operação Falhou! O número máximo de saques foi excedido!")
        else:
            saldo -= saque
            limite_saques -= 1
            print(f"""
        Saque de R${saque:.2f} realizado com sucesso!
        Seu saldo atual é de R${saldo:.2f}.
        Seu numero de saques diários restantes é {limite_saques}.
        """)
            print(f"\nObrigado por utilizar o Banco Senac!")
            extrato.append(f"Saque: R${saque:.2f}")
    
    elif opcao == "e":
        print(f"""
    =======================
        EXTRATO BANCÁRIO
    =======================
    """)
        if not extrato:
            print("Não foram realizadas movimentações.")
        for movimentacao in extrato:
            print(movimentacao)

        print(f"""
    =======================
    SALDO ATUAL: R${saldo:.2f}
    Número de saques restantes: {limite_saques}   
    =======================
    """)

    elif opcao == "q":
        print("Obrigado por utilizar o Banco Senac! Até a próxima!")
        break

    #Professor, eu coloquei o menu dentro do while True, para que o usuário possa sempre verificar o menu e escolher a opção desejada, sem precisar reiniciar o programa. Então quando for lançar no terminal, suba ele para vê o resultado, ou aumente a tela do terminal para que tudo fique visível. Abçs! 
