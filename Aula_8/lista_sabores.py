# Exercício ensinando o "for" e "lista".

# sabores = ["Mussarela", "Calabresa", "Pepperoni", "Presunto", "Quatro Queijos", "Frango com Catupiry", "Bacon com Ovos", "Lombo Canadense", "Camarão com Catupiry", "Portuguesa", "Baiana"]

# # print("Sabores disponíveis na Pizzaria Sabores:")
# # for sabor in sabores:
# #     print(sabor)


# # Método Range.

# # range(1,6)
# # lista = [1,2,3,4,5] # 6 -> O 6 não entra na conta.

# print("Preparando sua pizza.")
# for minutos in range(1,6):
#     print(f"⏰ {minutos} minuto(s) se passou...")

# print("🍕 Sua pizza está pronta! Bom apetite!")



# clientes = ["João", "Maria", "Carlos", "Ana", "Pedro"]

# print("Atendimento ao cliente.")
# for i, cliente in enumerate(clientes): # -> a primeira variável no for sempre será a numeração ("i") e o segundo será sempre o item da lista ("cliente").
#     if i == 3:
#         print("Capacidade máxima atingida! Não podemos atender mais clientes agora.")
#         break

#     print(f"Atendendo {cliente}...")



pedidos = ["Mussarela", "cancelado", "Calabresa", "cancelado", "Pepperoni"]

for pedido in pedidos:
    if pedido == "cancelado":
        continue  # pula este e vai para o próximo
    print(f"Preparando pizza de {pedido}...")