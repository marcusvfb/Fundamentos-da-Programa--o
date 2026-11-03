# Guia de estudos --- Fundamentos de Python

**Material de consulta • ADS --- Senac**

## 1. Comandos principais do Python

  -----------------------------------------------------------------------
  Comando                             Para que serve
  ----------------------------------- -----------------------------------
  `print()`                           Exibe informações no terminal.

  `input()`                           Exibe uma mensagem opcional e
                                      recebe uma entrada do usuário como
                                      texto (`str`).

  `f"..."`                            Permite inserir variáveis e
                                      expressões dentro de um texto. É
                                      chamada de *f-string*.

  `f"""..."""`                        Permite escrever textos em várias
                                      linhas, mantendo a possibilidade de
                                      inserir variáveis.
  -----------------------------------------------------------------------

Exemplos:

``` python
print("Bem-vindo ao Banco Senac!")

nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")
```

Exemplo de texto em várias linhas:

``` python
print(f"""
=======================
    MENU PRINCIPAL
=======================
Bem-vindo, {nome}!
""")
```

**Importante:** `input()` sempre recebe o conteúdo digitado como texto.
Para trabalhar com números, você pode precisar converter a entrada, por
exemplo, usando `float()` ou `int()`.

## 2. Convenções de nomenclatura (*Cases*)

Os *cases* são formas de escrever nomes de variáveis, funções e outros
elementos do código.

  -----------------------------------------------------------------------
  Tipo                    Exemplo                 Característica
  ----------------------- ----------------------- -----------------------
  `camelCase`             `nomeDoUsuario`         Primeira palavra
                                                  minúscula; seguintes
                                                  começam com maiúscula.

  `PascalCase`            `NomeDoUsuario`         Todas as palavras
                                                  começam com maiúscula.

  `snake_case`            `nome_do_usuario`       Palavras separadas por
                                                  `_`.

  `kebab-case`            `nome-do-usuario`       Palavras separadas por
                                                  `-`.
  -----------------------------------------------------------------------

Em Python, a convenção recomendada para variáveis e funções é
**`snake_case`**.

``` python
nome_do_usuario = "Marcus"
saldo_atual = 1000
limite_saques = 3
```

Atenção: `kebab-case` não é apropriado para nomes de variáveis Python,
porque o hífen é interpretado como operador de subtração.

## 3. Constantes em Python

Python não possui um mecanismo nativo que impeça uma variável de ser
alterada. Entretanto, existe uma convenção: escrever nomes de constantes
em letras maiúsculas.

``` python
TAXA_JUROS = 0.05
LIMITE_SAQUES = 3
```

A intenção é comunicar que esses valores devem ser tratados como
constantes, ou seja, não devem ser modificados durante a execução normal
do programa.

## 4. Operadores matemáticos

  Operador   Operação                    Exemplo       Resultado
  ---------- --------------------------- ----------- -----------
  `+`        Adição                      `10 + 3`             13
  `-`        Subtração                   `10 - 3`              7
  `*`        Multiplicação               `10 * 3`             30
  `/`        Divisão                     `10 / 3`       3.333...
  `//`       Divisão inteira             `10 // 3`             3
  `%`        Resto da divisão (módulo)   `10 % 3`              1
  `**`       Exponenciação               `2 ** 3`              8

O operador `//` descarta a parte fracionária do quociente, arredondando
em direção a menos infinito. Por isso, com números negativos, ele não se
comporta exatamente como uma simples remoção das casas decimais.

### Operadores de atribuição abreviada

Você já utilizou estes no Banco Senac:

  Operador   Equivalência           Exemplo
  ---------- ---------------------- ------------------
  `+=`       Soma e atribui         `saldo += valor`
  `-=`       Subtrai e atribui      `saldo -= saque`
  `*=`       Multiplica e atribui   `numero *= 2`
  `/=`       Divide e atribui       `numero /= 2`

Por exemplo, `saldo -= saque` equivale a `saldo = saldo - saque`.

## 5. Operadores lógicos

São utilizados para combinar ou inverter condições.

  --------------------------------------------------------------------------
  Operador          Explicação        Exemplo              Resultado
  ----------------- ----------------- -------------------- -----------------
  `and`             Verdadeiro se     `10 > 5 and 8 > 3`   `True`
                    ambas as                               
                    condições forem                        
                    verdadeiras.                           

  `or`              Verdadeiro se     `10 < 5 or 8 > 3`    `True`
                    pelo menos uma                         
                    condição for                           
                    verdadeira.                            

  `not`             Inverte o valor   `not True`           `False`
                    lógico.                                
  --------------------------------------------------------------------------

Exemplo:

``` python
saldo = 1000
saque = 300

if saque > 0 and saque <= saldo:
    print("Saque permitido.")
```

Nesse caso, as duas condições precisam ser verdadeiras para a mensagem
ser exibida.

## 6. Operadores de comparação

Esses operadores comparam valores e produzem um resultado lógico: `True`
ou `False`.

  Operador   Significado        Exemplo
  ---------- ------------------ ---------------------
  `==`       Igual a            `10 == 10` → `True`
  `!=`       Diferente de       `10 != 5` → `True`
  `<`        Menor que          `5 < 10` → `True`
  `>`        Maior que          `10 > 5` → `True`
  `<=`       Menor ou igual a   `5 <= 5` → `True`
  `>=`       Maior ou igual a   `10 >= 5` → `True`

**Não confunda `=` com `==`:**

-   `=` atribui um valor a uma variável.
-   `==` compara dois valores.

``` python
saldo = 1000

print(saldo == 1000)  # True
```

## 7. Métodos de texto: `upper()`, `lower()` e `capitalize()`

Esses métodos ajudam a padronizar textos antes de compará-los.

  -------------------------------------------------------------------------
  Método                  O que faz               Exemplo
  ----------------------- ----------------------- -------------------------
  `.upper()`              Converte as letras para `"sim".upper()` → `"SIM"`
                          maiúsculas.             

  `.lower()`              Converte as letras para `"SIM".lower()` → `"sim"`
                          minúsculas.             

  `.capitalize()`         Coloca a primeira letra `"MARCUS".capitalize()` →
                          em maiúscula e as       `"Marcus"`
                          demais em minúsculas.   
  -------------------------------------------------------------------------

Exemplo usando `upper()`:

``` python
resposta = input("Possui cadastro? (S/N): ").upper()
```

Se o usuário digitar `s`, `S` ou `sIm`, o texto será convertido para
maiúsculas.

**Importante:** esses métodos retornam um texto transformado. Para
guardar esse resultado, você pode atribuí-lo a uma variável, como no
exemplo acima.

## 8. Operador `in`

O `in` verifica se um elemento está presente em uma coleção, como uma
lista, ou se um trecho de texto aparece em uma string.

Exemplo com uma lista:

``` python
tipo_veiculo = input("Tipo do veículo: ").upper()

if tipo_veiculo in ["PEQUENO", "MÉDIO", "GRANDE"]:
    print("Tipo válido.")
```

Se o usuário digitar `pequeno`, o `.upper()` transforma a resposta em
`PEQUENO`, e o `in` verifica se ela está na lista.

-   Se estiver, o resultado da verificação será `True`.
-   Se não estiver, será `False`.

Você também pode usar `not in` para verificar se um elemento **não
está** presente na coleção.

## 9. Condicionais: `if`, `elif` e `else`

As condicionais permitem que o programa escolha quais instruções
executar dependendo de uma condição.

### `if` --- se

Executa o bloco quando a condição é verdadeira.

``` python
saldo = 1000

if saldo >= 500:
    print("Você possui saldo suficiente.")
```

### `else` --- caso contrário

Executa o bloco quando a condição anterior não é verdadeira.

``` python
saldo = 100

if saldo >= 500:
    print("Saldo suficiente.")
else:
    print("Saldo insuficiente.")
```

### `elif` --- caso contrário, se

Permite verificar outra condição quando a anterior não foi atendida.

``` python
opcao = input("Escolha uma opção: ").lower()

if opcao == "d":
    print("Depósito")
elif opcao == "s":
    print("Saque")
elif opcao == "e":
    print("Extrato")
else:
    print("Opção inválida.")
```

O Python verifica as condições em ordem e executa somente o primeiro
bloco cuja condição seja verdadeira. Se nenhuma for verdadeira, executa
o `else`, caso exista.

### Como funciona a indentação?

A indentação define quais instruções pertencem a cada bloco. Em Python,
normalmente utilizamos quatro espaços por nível.

``` python
if saldo > 0:
    print("Saldo positivo.")
    print("A primeira condição foi atendida.")

print("Esta linha está fora do if.")
```

As duas primeiras mensagens pertencem ao `if`. A última será executada
independentemente do resultado da condição.

**Atenção:** a indentação não é apenas estética. Uma linha colocada no
nível errado pode alterar o funcionamento do programa ou causar um erro.

## 10. Listas: `[]`

Uma lista permite armazenar vários elementos em uma única variável. Você
pode guardar textos, números e outros valores.

``` python
frutas = ["Banana", "Maçã", "Uva"]
```

Uma lista vazia é criada assim:

``` python
extrato = []
```

No seu Banco Senac, essa lista começa vazia e recebe as movimentações
realizadas.

### Adicionando elementos com `.append()`

O método `.append()` adiciona um elemento ao final da lista.

``` python
extrato = []

extrato.append("Depósito: R$ 100.00")
extrato.append("Saque: R$ 50.00")

print(extrato)
```

Resultado:

``` text
['Depósito: R$ 100.00', 'Saque: R$ 50.00']
```

Você pode combinar o `.append()` com uma f-string para guardar o valor
da operação:

``` python
extrato.append(f"Depósito: R$ {valor:.2f}")
```

Nesse exemplo:

-   `f"..."` monta o texto com o valor da variável.
-   `{valor:.2f}` exibe o valor com duas casas decimais.
-   `.append()` adiciona o texto à lista.

### Percorrendo uma lista com `for`

O `for` permite percorrer os elementos de uma lista, um por vez.

``` python
for movimentacao in extrato:
    print(movimentacao)
```

Leia essa instrução como:

> Para cada elemento de `extrato`, atribua o elemento à variável
> `movimentacao` e execute o bloco indentado.

O `for` atribui automaticamente cada elemento à variável de controle,
sem precisar escrever `movimentacao = ...` manualmente.

Por exemplo, se a lista tiver três movimentações, o `print()` será
executado três vezes, exibindo cada uma delas.

### Verificando se uma lista está vazia

Você pode utilizar:

``` python
if not extrato:
    print("Não foram realizadas movimentações.")
```

Uma lista vazia é considerada falsa em uma condição. Portanto,
`not extrato` será verdadeiro quando não houver elementos.

Se a lista tiver alguma movimentação, a condição será falsa.

## 11. Laços de repetição: `while`, `break` e `continue`

### `while`

O `while` repete um bloco enquanto sua condição for verdadeira.

``` python
contador = 1

while contador <= 3:
    print(contador)
    contador += 1
```

O programa exibe `1`, `2` e `3`. Quando `contador` chega a `4`, a
condição se torna falsa e o laço termina.

### `while True`

É uma forma de criar um laço que continua até que alguma instrução
interrompa sua execução.

``` python
while True:
    opcao = input("Digite q para sair: ").lower()

    if opcao == "q":
        break
```

### `break`

Encerra imediatamente o laço de repetição em que está sendo executado.
Se estiver dentro do `while` principal do seu programa, encerra esse
laço e permite que a execução continue após ele --- ou termine, se não
houver mais código.

### `continue`

Interrompe a repetição atual e volta ao início do laço para iniciar a
próxima iteração.

``` python
while True:
    opcao = input("Digite d para depósito ou q para sair: ").lower()

    if opcao not in ["d", "q"]:
        print("Opção inválida.")
        continue

    if opcao == "q":
        break

    print("Você escolheu depósito.")
```

Nesse exemplo, se a opção for inválida, o `continue` faz o programa
voltar ao menu sem executar as instruções restantes daquela repetição.

## Resumo rápido para revisão

  Recurso                Função principal
  ---------------------- -------------------------------------------------
  `print()`              Exibir informações
  `input()`              Receber uma entrada como texto
  `f"..."`               Inserir valores em textos
  `=`                    Atribuir valores
  `==`                   Comparar igualdade
  `and`, `or`, `not`     Combinar ou inverter condições
  `if`, `elif`, `else`   Tomar decisões
  `[]`                   Criar uma lista
  `.append()`            Adicionar um elemento à lista
  `for`                  Percorrer os elementos de uma coleção
  `while`                Repetir enquanto uma condição for verdadeira
  `break`                Encerrar o laço atual
  `continue`             Pular para a próxima repetição
  `.upper()`             Converter texto para maiúsculas
  `.lower()`             Converter texto para minúsculas
  `.capitalize()`        Colocar a primeira letra em maiúscula
  `in`                   Verificar se um elemento pertence a uma coleção

**Dica de estudo:** continue acrescentando conceitos a este material
conforme forem aparecendo nas aulas. Ele já serve como uma boa base para
revisar condicionais, listas e laços de repetição.
