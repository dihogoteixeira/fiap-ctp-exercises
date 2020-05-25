nomeFuncionario=input("Digite o nome do funcionario: ")
salarioBruto=float(input("Digite o valor do Salario Bruto: "))
valorParcela=float(input("Digite o valor da parcela: "))

valorPermitido = salarioBruto / 100 * 30

if valorParcela > valorPermitido:
    print(nomeFuncionario + ", o Valor da parcela e maior que 30% do seu salario bruto, emprestimo negado!")
else:
    print(nomeFuncionario + ", o Valor de parcela permitido! Seu emprestimo foi aprovado")