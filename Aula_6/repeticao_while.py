# Aprendendo a usar o While e fazer a lista

sabores_de_pizza = ["Mussarela", "Calabresa", "Pepperoni", "Quatro Queijos", "Frango com Catupiry", "Bacon com Ovos", "Lombo Canadense", "Camarão com Catupiry", "Portuguesa", "Baiana"]
pizza = "" # Aqui ficará armazenado o pedido do cliente

print("Faça seu pizza (digite 'sair' para encerrar): ")

# Enquanto o sair não for digitado, o While continuará sendo executado

while pizza.lower() != "sair":
    pizza = input("Escolha um de nossos sabores de pizza: ").capitalize() # Muda a primeira letra pra maiuscula
    if pizza in sabores_de_pizza:
        print(f"sua pizza de {pizza} já está sendo preparada.")
    elif pizza.lower() == "sair":
        print("Pedido encerrado!")
    else:
        print("Você digitou errado ou pediu algo fora do cardápio, tente de novo seu idiota!")

# Break -> Encerra definitivamente    