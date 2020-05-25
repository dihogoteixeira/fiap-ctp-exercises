numero_1 = int(input("Digite o primeiro numero inteiro:  "))
numero_2 = int(input("Digite o segundo numero inteiro:   "))
numero_1Lista = list(str(numero_1))
calculo01 = int(numero_1Lista[1]) *3
calculo02 = int(13 - 2)
calculo03 = calculo02 + numero_2
resultado = (calculo01) + (calculo02) + (calculo03)

if resultado <= 0:
    print("Resultado enor ou igual a zero")
elif resultado > 0 and resultado <= 20:
    print("Resultado maior que zero e menor ou igual a 20")
else:
    print("Resultado maior que 20")