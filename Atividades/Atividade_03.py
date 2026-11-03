# Atividade de Abertura de Matrícula

Nome_do_aluno = input(f"""
        Bem-Vindo ao nosso Curso Técnico!🏫
        Por favor digite o seu nome:
""")

Idade_do_aluno = int(input(f"""
        Estamos cada vez mais perto da sua Mátricula!
        Nos fale agora a sua idade:
"""))

Frequencia_escolar = int(input(f"""
        Ainda falta alguns detalhes, quase lá.😊
        Coloque sua frequência escolar:
"""))

Nota_do_aluno = float(input(f"""
        Quase lá, só mais um detalhe, eu prometo.🤣
        Coloque sua nota final do ano letivo:
"""))

if Nota_do_aluno >= 9.0 and Idade_do_aluno >= 18: #Eu coloquei aqui a idade tb como requisito pra mátricula, então a aprovação automática vai ignorar apenas a frequência.
    print(f"""
    ========================================

        Parabéns {Nome_do_aluno}! 🎉
    Você se destacou com uma nota excelente!
    Graças a sua nota final, sua matrícula foi aceita automaticamente! 🏆
    Você deu mais um passo para um carreira triunfal! Pode confiar que 
    sua futuro está em boas mãos. 🚀🏆
    
    ========================================
    """)

elif Idade_do_aluno >= 18 and Frequencia_escolar >= 75 and Nota_do_aluno >= 6.0:
    print(f"""
    ========================================

        Parabéns {Nome_do_aluno}! 🎉
    Você está apto a se matricular no nosso curso técnico. 🏫
    Você deu mais um passo para um carreira triunfal! Pode confiar que 
    sua futuro está em boas mãos. 🚀🏆
    
    ========================================
    """)

else:
    print(f"""
    ========================================

        Infelizmente {Nome_do_aluno}. 😔
    Você não está apto a se matricular no nosso curso técnico. 🏫
    Você precisa de uma idade mínima de 18 anos, frequência escolar acima de 75%
    e nota final do ano letivo acima de 6.0.
    Mas não desanime!╰(*°▽°*)╯ 
    Espere os seus 18 anos! ou continue se esforçando e melhorando suas notas e frequência escolar.
    Com dedicação e esforço, você poderá se matricular no futuro! 🚀🏆
    
    ========================================
    """)

    # Vou admitir aqui ao senhor, que eu fiz sem IA, mas eu usei pra me ajudar num detalhe que eu estava errando. Eu estava colocando vários if(s) separados, e não estava conseguindo fazer a lógica correta. Toda vez que eu aprovava a matrícula pelo cenário da nota maior que 9, idependente da frequência dele, eu obtinha os dois resultados quando executava, tantoa  aprovação pela nota quanto a reprovação pela frequencia. Aí eu perguntei ao ChatGPT o porque disso e ele explicou justamente isso, de eu ter colocado diversos if(s) separados. Agora eu entendi a importancia do elif. :D