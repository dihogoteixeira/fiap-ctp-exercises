import math
print('''
Menu de Opções:
    1. Somar dois números
    2. Raiz quadrada de um número
    
''')
botaoMenu = int(input("\nDigite a opção desejada: "))

if botaoMenu == 1:
    numero01 = int(input("Digite o primeiro numero: "))
    numero02 = int(input("Digite o segundo numero: "))
    print("O resultado da sua soma é: ", numero01 + numero02)

elif botaoMenu == 2:
    numero03 = int(input("Digite um numero: "))
    raizQuadrada = math.sqrt(numero03)
    print("A raiz quadrada de {}".format(numero03),"é: ", raizQuadrada)