# Cadastro de Jogo

VALOR_MAXIMO = 500 # constante (não pode ser alterada)

# Jogador
nome_do_jogador = "Marcus Vinícius" # string
idade_do_jogador = 33 # inteiro
genero_do_jogador = "Masculino" # string
possui_conta = True # booleano (True or False)

# Jogo
nome_do_jogo = "Star Wars the Old Republic" # string
preço_do_jogo = 15.99 # float
peso_do_jogo_em_gb = 33 # inteiro
jogadores_online = 5.235 # float

print(f""" 

        ====CADASTRO DO JOGADOR====
        Nome: {nome_do_jogador}
        Idade: {idade_do_jogador}
        Gênero: {genero_do_jogador}
        Possui Conta: {possui_conta}

        ===JOGO====
        Nome: {nome_do_jogo}
        Preço: R$ {preço_do_jogo:.2f}
        Peso: {peso_do_jogo_em_gb} GB
        Jogadores Online: {jogadores_online}

Valor Máximo Permitido: R$ {VALOR_MAXIMO}
""")

