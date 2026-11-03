# Exercício Registro de Pizza

pizzas = 0 # Variável no escopo global.
faturamento = 0
maior_venda = 0
menor_venda = 0
acima_50 = 0

while True:
    valor = float(input("Valor da pizza vendida (digite 0 para encerrar): R$ ")) # Variável no escopo local.
    if valor == 0:
        break
    if valor < 0:
        print("Valor invalido, digite um valor positivo.")
        continue
    pizzas += 1
    faturamento += valor
    if valor > maior_venda: # na primeira venda, ele é maior.
        maior_venda = valor
    if pizzas == 1 or valor < menor_venda:
        menor_venda = valor
    if valor > 50:
        acima_50 += 1
        
#Shit+Tab volta a identação; TAB = pula 4 espaços / Shit+Tab = volta 4 espaços.
if pizzas == 0:
    print("Nenhuma venda registrada hoje.")
else:
    ticket_medio = faturamento / pizzas

    print(f"""
====================
FATURAMENTO DO CAIXA
pizza vendida: {pizzas}
Faturamento total: R${faturamento:.2f}
Ticket médio: R${ticket_medio:.2f}
Maior venda: R${maior_venda:.2f}
Menor venda: R${menor_venda:.2f}
Pizzas acima de R$50.00: {acima_50}
""")
