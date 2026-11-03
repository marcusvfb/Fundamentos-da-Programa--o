"""
Crie um programa que simulo um caixa eletrônico. o Usuário pode sacar valores até que o saldo disponível acabe ou até ele digitar "sair".

Regras:
1- Saldo inicial 500 reais
2- Peça ao usuário digitar valor para saque.
3- Se o valor for maior que o saque, avise que não há saldo suficiente.
4- Se o usuário digitar "sair", encerre o programa.
"""

SALDO_TOTAL = 500 # Boa Pratica - Constante

while SALDO_TOTAL > 0: # Continuará até ser False(acabar o saldo) ou digitar "sair".
    print(f"\nSeu saldo total é R${SALDO_TOTAL:.2f}💰") # o \n pula uma linha na exibição do terminal. :.2f é para colcoar os centavos.
    saque = input("Digite o valor para sacar ou 'sair' para encerrar.")

    if saque.lower() == "sair":
        print("🏧 Operação encerrada.")
        break
    saque = float(saque) #convertendo a string para um número.
    if saque > SALDO_TOTAL:
        print("Saldo insuficiente. Ganhe mais seu pobre")

    else:
        SALDO_TOTAL = SALDO_TOTAL - saque
        print(f"\nSaque de R${saque:.2f} realizado com sucesso")
        