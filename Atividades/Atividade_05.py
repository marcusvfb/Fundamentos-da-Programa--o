# Dia da Semana - Exercício 

dia_da_semana = input("Digite o dia da semana (segunda/terça/etc): ").lower()
valor_do_pedido = float(input("Digite o valor do seu pedido: "))
frete = 5 

if dia_da_semana in ("terça", "terca") and valor_do_pedido > 40:
    print(f"""
          =============================  
            Seu Pedido é uma ordem!🍕
Você ganhou uma sobremesa por nossa conta hoje!👌
  Valor total do seu pedido: {valor_do_pedido + frete}
          =============================    
    """)
elif dia_da_semana in ("quarta"):
    print(f"""
          =============================
            Seu pedido é uma ordem!🍕
    Você ganhou um disconto de 15% hoje!💲👏
        Valor total do seu pedido: {(valor_do_pedido + frete) * 0.85}
          =============================
    """)
elif dia_da_semana in ("sábado", "sábado", "domingo") and valor_do_pedido > 100:
    print(f"""
          =============================
            Seu pedido é uma ordem!🍕
      Você ganhou um fretes grátis hoje!🏍️👏
          Valor total do seu pedido: {valor_do_pedido}
          =============================
    """)
else:
    print(f""""
          =============================
            Seu pedido é uma ordem! 🍕
    Aguarde por alguns minutos e logo a melhor pizza
    do bairro está nas suas mãos!😍
           Valor total do seu pedido: {valor_do_pedido + frete}
          =============================
    """)


