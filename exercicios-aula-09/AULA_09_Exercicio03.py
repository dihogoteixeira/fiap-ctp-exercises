primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero : "))
terceiroNumero = int(input("Digite o terceiro numero: "))

if(terceiroNumero > segundoNumero):
    tempVar = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = tempVar

if(segundoNumero > primeiroNumero):
    tempVar = segundoNumero
    segundoNumero = primeiroNumero
    primeiroNumero = tempVar

if(terceiroNumero > segundoNumero):
    tempVar = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = tempVar

print("Primeiro maior numero: ", primeiroNumero, \
      "\nSegundo maior numero: ",segundoNumero, \
      "\nTerceiro maior numero: ",terceiroNumero)