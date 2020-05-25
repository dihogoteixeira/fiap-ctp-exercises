# SAUDACOES #
nomeAluno = input("Bem vindo, digite o seu nome: ")

# VARIAVEIS QUE RECEBEM NOTAS #
trabalhoLaboratorio = float(input("Digite sua nota do 'Tabalho de Laboratorio': "))
avaliacaoSemestral = float(input("Digite sua nota da 'Avaliacao Semestral': "))
exameFinal = float(input("Digite sua nota do 'Exame Final': "))

# SOMA DE NOTAS #
mediaFinal = (trabalhoLaboratorio + avaliacaoSemestral + exameFinal)/3
print(nomeAluno + ", sua media final e: " + str(mediaFinal))

# CALCULO DE MEDIA PONDERADA #

if mediaFinal >= 8.0 and mediaFinal <= 10.0:
    print(nomeAluno + ", você è Conceito A ")
elif mediaFinal >= 7.0 and mediaFinal <= 7.9:
    print(nomeAluno + ", você è Conceito B ")
elif mediaFinal >= 6.0 and mediaFinal <= 6.9:
    print(nomeAluno + ", você è Conceito C ")
elif mediaFinal >= 5.0 and mediaFinal <= 5.9:
    print(nomeAluno + ", você è Conceito D ")
elif mediaFinal >= 0.0 and mediaFinal <= 4.9:
    print(nomeAluno + ", você è Conceito E ")
else:
    print(nomeAluno + ", digite dua nota real de 0 (0.0) a 10 (10.0)\n"
                      " eu fui programado para calcular valores\n"
                      "flutuantes =[ ")
