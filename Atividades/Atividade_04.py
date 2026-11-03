# Atividade Empréstimo Bancário

Idade_do_cliente = int(input("Idade do cliente: "))
Salario_do_cliente = float(input("Salário do cliente: "))
Tempo_de_trabalho_do_cliente = int(input("Tempo de trabalho do cliente (em anos): "))
emprestimo_aprovado = Idade_do_cliente >= 18 and Salario_do_cliente >= 2000 and Tempo_de_trabalho_do_cliente >= 2 or Salario_do_cliente >= 5000

# Eu fiquei na duvida professor, caso o cliente tenha 17 anos, mas ganhe R$5.000,00 de salário, se ele poderia pegar o empréstimo, eu interpretei que sim, já que no exercício o salário igual ou maior de R$5.000,00 é aprovação automatica, mesmo com reprovação automática por ser menor de idade. Imagino que um banco queria o dinheiro do rapaz de qualquer forma kkkk.

if emprestimo_aprovado == True:
    print("O empréstimo do cliente foi aprovado. ✅")
else:
    print("O empréstimo do cliente foi negado. ❌")

# Seria só isso? fiquei agora confuso se interpretei algo errado ou se era pra fazer apenas isso mesmo kkkk.
# Desafio extra

valor_do_emprestimo = float(input("Valor do empréstimo solicitado: "))
emprestimo_maximo = Salario_do_cliente * 5
juros_do_emprestimo = valor_do_emprestimo * 1.5 
parcela_do_emprestimo = (valor_do_emprestimo + juros_do_emprestimo) / (Tempo_de_trabalho_do_cliente * 12) # Isso eu soube calcular por causa do que eu aprendi em matemática financeira (Juros Simples, Juros Compostos, etc), ainda lembro de algumas coisas do tempo que tentei passar para o concurso da Caixa Econômica Fereral. não consegui a nota de corte. :(
emprestimo_negado = parcela_do_emprestimo > (Salario_do_cliente * 0.3) #Se estou correto, 30% é 0,3 vezes 100. Então posso calcula desta forma.
emprestimo_aprovado = parcela_do_emprestimo <= (Salario_do_cliente * 0.3) and emprestimo_maximo <= Salario_do_cliente * 5

if emprestimo_aprovado == True:
    print(f"""
    ========================================
    
        Parabéns! 🎉
    O empréstimo do cliente foi aprovado. ✅
    O valor máximo de empréstimo que o cliente pode solicitar é de R${emprestimo_maximo:.2f}
    O valor do empréstimo solicitado é de R${valor_do_emprestimo:.2f}
    O valor da parcela do empréstimo será de R${parcela_do_emprestimo:.2f}
    
    ========================================
    """)
else:
    print("O empréstimo do cliente foi negado. ❌")

    #Nenhuma IA foi usada! :D
