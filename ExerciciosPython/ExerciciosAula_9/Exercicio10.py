primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero : "))

divisao = primeiroNumero % segundoNumero

if divisao < primeiroNumero:
    print("Primeiro numero e divisivel pelo Segundo numero.")
else:
    print("Primeiro numero 'NAO' e divisivel pelo Segundo numero.")