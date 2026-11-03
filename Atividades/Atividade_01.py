# Jogador
Nome = "Marcus Vinícius" #string
Idade = 33 #inteiro
Nivel = 80 #inteiro
Horas_Jogadas = 125.5 #float
Possui_Conta_Ativa = True #booling

# Personagem
Nome = "Darth Vader" #string
Nivel_do_Personagem = 80 #inteiro
Creditos = 1500000 #inteiro
Esta_Online = False #booling

# Pate 1
Variavel_1 = Creditos + 500000
Variavel_2 = Nivel - Nivel_do_Personagem
Variavel_3 = Horas_Jogadas + 10.5 

print(f"O jogador terá {Variavel_1} se adicionar mais 500.000 créditos")
print(f"A diferença entre o nivel máximo e o nivel do personagem é: {Variavel_2}")
print(f"Se o jogador jogar mais 10.5 horas ele terá: {Variavel_3}")

# Parte 2
print(f"O jogador possui conta ativa? {Possui_Conta_Ativa}")
print(f"O jogador tem mais de 18 anos? {Idade > 18}")
print(f"O personagem está no nivel máximo? {Nivel_do_Personagem == 80}")
print(f"O personagem tem mais de 1 milhão de créditos? {Creditos > 1000000}")
print(f"O personagem está online? {Esta_Online}")
print(f"O jogador tem mais de 100 horas jogadas? {Horas_Jogadas > 100}")
print(f"O jogador tem exatamente 30 anos? {Idade == 30}")
print(f"O personagem está offline? {not Esta_Online}")

# Parte 3
print(f"O jogador tem mais de 18 anos e possui conta ativa? {Idade > 18 and Possui_Conta_Ativa}")
print(f"O jogador está online ou possui conta ativa? {Esta_Online or Possui_Conta_Ativa}")
print(f"O jogador possui nenhum crédito ou possui mais de 1 milhão de créditos? {Creditos == 0 or Creditos > 1000000}")
print(f"O jogador possui conta ativa e está no nível máximo? {Possui_Conta_Ativa and Nivel_do_Personagem == 80}")
