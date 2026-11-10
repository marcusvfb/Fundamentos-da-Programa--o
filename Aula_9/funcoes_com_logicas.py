def calcular_preco_pizza(sabor, tamanho, borda_recheada=False):
    "Calcula o preço final de uma pizza com opções."

    tabela = {
        "p": 45.0,
        "m": 65.0,
        "g":85.0,
        "f":100.0
    }   

    preco = tabela[tamanho]
    if borda_recheada:
        preco += 18.0
    print(f"""
    A pizza é de {sabor} 
    e o tamanho é {tamanho} 
    a borda é recheada? {borda_recheada}
    Preço total: R${preco}
""")

calcular_preco_pizza("Calabresa", "g")




