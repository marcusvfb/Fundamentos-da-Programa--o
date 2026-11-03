# Estruturas condionais permitem que o programa execute blocos de códigos diferentes dependendo de uma condição. A condição é sempre avaliado como True e False.


# if -> Verifica uma condição e executa o bloco de código associado se a condição for verdadeira.
# Ex: se o usuário tiver a idade maior que 18 ele poderá entrar.
# Idade_usuario = 21 # Hardcode -> clocar um valor diretamente no código, em vez de deixar esse valor ser definido de forma dinâmica.
# if Idade_usuario > 18:
#     print("O usuário pode acessar o local.")

# else -> Permite executar o bloco de código se acondição if for falsa ( é o famoso se não).
# Ex: se o usuário tiver a idade maior que 18 ele poderá entrar.

# if Idade_usuario > 18:
#     print("👍O usuário pode acessar o local.")
# else:
#     print("💩Entrada proíbida!")    

# elif -> Ele é uma abreviação do (else if). É usado para testar várias condições. ELe só será exibido se todas as condições anteriores forem falsas.
# Ex: nota de prova.

# nota = int(input("Digite a nota do aluno: ")) # Quando for usar o comando input, ele sempre interpretará como string (texto), então caso você precise transformar para números inteiros, por exemplo, precisa escrever antes do input e coloca-lo entra parenteses.
# nota maior ou igual a 90, "Aprovado com nota excelente."
# se a nota for maior ou igual a 70: "Aprovado."
# e qualquer outra nota será exibido: "reprovado."

# if nota >= 90:
#    print("🎆 Aprovado com nota excelente.")
# elif nota >= 70:
#    print("👏🏻 Aprovado")
# else:
#    print("❌ reprovado")

# .upper() -> coloca tudo em maiusculo
# .lower() -> Coloca tudo em minusculo
# .capitalize () -> Coloca a primeira letra em maiuscuculo
