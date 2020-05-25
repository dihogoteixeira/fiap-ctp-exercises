primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero : "))
terceiroNumero = int(input("Digite o terceiro numero: "))
lista = [primeiroNumero,segundoNumero,terceiroNumero]

if (lista == sorted(lista)):
    print("Os números foram digitados em ordem crescente.")
else:
    print("Os números não foram digitados em ordem crescente.")