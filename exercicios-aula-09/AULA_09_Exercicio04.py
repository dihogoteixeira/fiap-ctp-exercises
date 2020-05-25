primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero : "))
terceiroNumero = int(input("Digite o terceiro numero: "))

if (terceiroNumero > segundoNumero):
    tempVar = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = tempVar

if (segundoNumero > primeiroNumero):
    tempVar = segundoNumero
    segundoNumero = primeiroNumero
    primeiroNumero = tempVar

if (terceiroNumero > segundoNumero):
    tempVar = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = tempVar

print("Primeiro numero: ", terceiroNumero, \
      "\nSegundo numero: ",segundoNumero, \
      "\nTerceiro numero: ",primeiroNumero)

if (primeiroNumero == segundoNumero and primeiroNumero == terceiroNumero):
    print("OS TRÊS NÚMEROS DIGITADOS SÃO IGUAIS")