# SAUDACOES #
nomeAluno = input("Ola, digite o seu nome: ")
print("Bem-vindo, {}!\n".format(nomeAluno), end=" ")

# VARIAVEIS QUE RECEBEM NOTAS #
trabalhoLaboratorio = float(input("Digite sua nota do 'Tabalho de Laboratorio': "))
avaliacaoSemestral = float(input("Digite sua nota da 'Avaliacao Semestral': "))
exameFinal = float(input("Digite sua nota do 'Exame Final': "))
totalDeFaltas = float(input("Digite seu total de faltas: "))

# SOMA DE NOTAS #
mediaFinal = (trabalhoLaboratorio + avaliacaoSemestral + exameFinal)/3

# CALCULO DE MEDIA PONDERADA #
if mediaFinal <= 6.9:
    print("Desculpe "+ str(nomeAluno) + ", voce foi reprovado.")
elif mediaFinal <= 6.9 and totalDeFaltas >20:
   print("Desculpe "+ str(nomeAluno) + ", voce foi reprovado por notas.")
elif mediaFinal >= 7.0 and totalDeFaltas >20:
    print("Desculpe " + str(nomeAluno) + ", voce foi aprovado por media, porem reprovado por faltas.")
else:
    print("Parabens "+ nomeAluno + ", voce foi aprovado!")
