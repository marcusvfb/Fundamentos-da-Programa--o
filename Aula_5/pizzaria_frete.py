# # Exercicio 01 

# distancia = float(input("Digite a distância em km: "))

# frete_minimo = distancia <= 3
# frete_maximo = 3 < distancia <= 8
# frete_invalido = distancia >= 12

# if frete_minimo == True:
#     print(f""" 
#     Digite a distância em km: {distancia}
#     Frete : R$ 5,00
#     """)

# elif frete_maximo == True:
#     print (f""" 
#     Digite a distância em km: {distancia}
#     Frete : R$ 10,00
#     """)

# elif frete_invalido == True:
#     print (f""" 
#         Digite a distância em km: {distancia}
#         Não entregamos nessa distância. 😕
#         """)

# # Exercicio 02

# # distancia = float(input("Digite a distância em km: "))


# # frete_minimo = distancia <= 5
# # frete_maximo = 6 < distancia < 10 
# # frete_invalido = distancia >= 10

# # valor_minimo = 5 + distancia * distancia
# # valor_maximo = 5 + distancia * 2 


# # if frete_minimo == True :
# #    print(f"""
# #    Digite a distância em km: {distancia}
# #    Frete: R$ {valor_minimo:.2f}
# #    """.replace(".", ","))

# # elif frete_maximo == True :
# #     print (f""" 
# #     Digite a distância em km: {distancia}
# #     Frete: R$ {valor_maximo:.2f}
# #     """.replace(".", ","))

# # elif frete_invalido == True : 
# #     print(f"""
# #     Digite a distância em km: {distancia}
# #     Não entregamos nessa distância. 😕
# # """)


# Exercicio 3 
    
# dia = input("Dia da semana: ").lower()
# valor = float(input("Valor do pedido: R$ "))
# desconto = valor - (valor * 0.15)
# frete = 5
# valor_total = valor + frete
# total = valor + frete
# quarta = desconto + frete

# if dia == "terça" and valor >= 40 :
#     print (f""" 
#     Dia da semana: terça
#     Valor do pedido: R$ {valor:.2f}
#     🍰 Você ganhou uma sobremesa grátis!
#     Total a pagar: R$ {frete:.2f}

# """.replace(".", ",")) 

# elif dia == "terça" and valor <= 40 :
#       print (f"""
#       Dia da semana: terça
#       Valor do pedido: R$ {valor:.2f}
#       Total a pagar: R$ {valor_total:.2f}
#     """.replace(".", ",")) 

# elif dia == "quarta" :
#     print(f"""
# Dia da semana: quarta
# Valor do pedido: R$ {valor:.2f}
# Desconto de 15% aplicado!
# Total a pagar: R$ {(quarta)}
# """.replace(".", ","))

# elif dia == "sábado" or "domingo" and valor > 100: 
#     print(f"""
# Dia da semana: {dia}
# Valor do pedido: R$ {valor:.2f}
# 🚚 Frete grátis!
# Total a pagar : R$ {valor:.2f}
# """.replace(".", ","))
    
#     if dia == "sábado" or "domingo" and valor <= 100:
#        print(f"""
#        Dia da semana: {dia}
#        Valor do pedido: R$ {valor:.2f}
#        Total a pagar : R$ {valor_total:.2f}
#        """.replace(".", ","))


# else :
#    print(f"""
# Dia da semana: {dia}
# Valor do pedido: R$ {valor:.2f}
# Total a pagar: R$ {frete:.2f}
# """.replace(".", ","))

