# Perguntas a serem feitas ao cliente
# A pizza pequena = 19,90
# A pizza média = 29,90
# A pizza grande = 39.90

FRETE = 2 
dia_semana = "segunda"

print(f"""
            =======================================================================
            🍕 SEJA BEM-VINDO A MELHOR PIZZARIA DA ZONA SUL, A PIZZARIA SABORES!!🍕
            =======================================================================
     """)
nome_cliente = input(f"""
            Digite o seu nome:
                    """)
pizza_sabor = input(f"""
           🍕 Pizzas disponíveis: 
            1- Frango com Requeijão
            2- Calabresa
            3- Mussarela
            4- Banana com Chocolate
                    """)
pizza_tamanho = input(f"""
            Escolha o tamanho da pizza:
            1- pequena
            2- média
            3- grande
                     """)
forma_entrega = input(f"""
            🏍️ Escolha a forma de entrega:
            1- Retirar no local
            2- Entrega na residência
                     """)

# Estrutura condicional para a promoção:
# Comprando qualquer pizza e qualquer tamanho no sábado o refri é gratuito.
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são grátis.
# Comprando uma pizza de calabresa tamanho grande, em qualquer dia, o frete é grátis.
if dia_semana == "sabado":
    print(f"🍕 Seu desejo é uma ordem!")
    print(f"O refri hoje é por nossa conta! ╰(*°▽°*)╯")
elif dia_semana == "domingo":
    print(f"🍕 Seu desejo é uma ordem!")
    print(f"Hoje seu frete e seu refri é por nossa conta! ╰(*°▽°*)╯")
elif pizza_sabor == "calabresa" and pizza_tamanho == "grande":
    print(f"🍕 Seu desejo é uma ordem!")
    print(f"Hoje seu frete é por nossa conta! ╰(*°▽°*)╯")
else:
    print("Hoje não é dia de nossas incríveis promoções. (┬┬﹏┬┬)")

print(f"""
         ====================== 
            RESUMO DO PEDIDO
        Nome do cliente: {nome_cliente}
        Sabor da pizza: {pizza_sabor}
        Tamanho da pizza: {pizza_tamanho}
        Forma de entrega: {forma_entrega}
         ====================== 
     """)