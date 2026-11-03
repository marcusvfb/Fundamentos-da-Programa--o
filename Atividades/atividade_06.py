# Dia da Semana + frete - Exercício 

dia_da_semana = input("Digite o dia da semana (segunda/terça/etc): ").lower()
valor_do_pedido = float(input("Digite o valor do seu pedido: "))
distancia = float(input("Digite a distância da sua localização (km): "))
frete = 5
frete_2 = 10

if dia_da_semana in ("terça", "terca") and valor_do_pedido > 40 and distancia <= 5.9:
    print(f"""
          =============================  
            Seu pedido é uma ordem!🍕
Você ganhou uma sobremesa por nossa conta hoje!👌
          Valor total do seu pedido: {valor_do_pedido + frete}
          =============================    
    """)

elif dia_da_semana in ("terça", "terca") and valor_do_pedido > 40 and distancia <= 10:
  print(f"""
          =============================  
            Seu pedido é uma ordem!🍕
Você ganhou uma sobremesa por nossa conta hoje!👌
          Valor total do seu pedido: {valor_do_pedido + frete_2}
          =============================    
    """)
elif distancia >= 10.1:
  print(f"""
          =============================  
      Sinto muito! Infelizmente não entregamos
      na sua região.😔
          =============================    
    """)

if dia_da_semana in ("quarta") and distancia <= 5.9:
    print(f"""
          =============================
            Seu pedido é uma ordem!🍕
    Você ganhou um disconto de 15% hoje!💲👏
        Valor total do seu pedido: {(valor_do_pedido + frete) * 0.85}
          =============================
    """)
elif dia_da_semana in ("quarta") and distancia <= 10:
    print(f"""
          =============================
            Seu pedido é uma ordem!🍕
    Você ganhou um disconto de 15% hoje!💲👏
        Valor total do seu pedido: {(valor_do_pedido + frete_2) * 0.85}
          =============================
    """)

if dia_da_semana in ("sabado", "sábado", "domingo") and valor_do_pedido > 100:
    print(f"""
          =============================
            Seu pedido é uma ordem!🍕
      Você ganhou um fretes grátis hoje!🏍️👏
          Valor total do seu pedido: {valor_do_pedido}
          =============================
    """)

if dia_da_semana in ("segunda", "quinta", "sexta") and distancia <= 5.9:
   print(f""""
             =============================
               Seu pedido é uma ordem! 🍕
       Aguarde por alguns minutos e logo a melhor pizza
       do bairro está nas suas mãos!😍
              Valor total do seu pedido: {valor_do_pedido + frete}
             =============================
       """)
elif dia_da_semana in ("segunda", "quinta", "sexta") and distancia <= 10:
   print(f""""
             =============================
               Seu pedido é uma ordem! 🍕
       Aguarde por alguns minutos e logo a melhor pizza
       do bairro está nas suas mãos!😍
              Valor total do seu pedido: {valor_do_pedido + frete_2}
             =============================
       """)
