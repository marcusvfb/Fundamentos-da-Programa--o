# Comandos principais do Python

print() -> Exibe informações no terminal.
input() -> Exibe informações e/ou recebe.
f""" """ -> f-string. Concatena variáveis e textos. - com 3 aspas, você consegue escreve em mais de uma linha.

# Cases utilizados nas linguagens de programação 
 NOME DO USUARIO
 1. cammelCase. Ex: nomeDoUsuario
 2. PascalCase. Ex: NomeDoUsuario
 3. ``snake_case. Ex: nome_do_usuario`` - case padrão na linguagem python.
 4. kebab-case. Ex: nome-do-usuario

# Python não tem constante, mas tem boa prática.
CPF = "154.182.937.96" # Constante, boa prática.

# Operadores Matemáticos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão
// -> divisão inteira
% -> resto da divisão (módulo)
** -> exponenciação (potência)

# Operadores lógicos
and -> Retorna True se ambos forem verdadeiros, caso contrário retorna falso
or -> Retorna True se um ou ambos forem verdadeiros, caso contrario retorna falso
not -> Inverte o valor lógico 
# Operadores de Comparação
== -> igual a
!= -> diferente de
< -> menor que
> -> maior que
<= -> menor ou igual a
>= -> maior ou igual a

# Escopo global x Ecopo local
> global:
- Pode ser acessada por qualquer parte do sistema. No entanto, em python ela escapa. Isso quer dizer que, o valor da variável é modificado em alguma estrutura e o valor fica sendo o último usado na estrutura.

> local:
- Ela é criada dentro de uma estrutura. Ela vale somente naquela estrutura e se em um outro nível ela ser utilizada, ela escapa porém pode ser reutilizada. 