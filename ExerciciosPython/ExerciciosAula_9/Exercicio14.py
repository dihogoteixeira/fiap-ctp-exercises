userName = input("Ola tudo bem? qual o seu nome?: ")
print("Bem-vindo, {}!\n".format(userName), end=" ")
print("\nInforme tes valores reais para definirmos que tipo de triângulo teremos\n")

primeiroNumero = float(input("Primeiro valor real: "))
segundoNumero = float(input("Segundo valor real: "))
terceiroNumero = float(input("Terceiro valor real: "))

if (primeiroNumero + segundoNumero < terceiroNumero) or \
   (primeiroNumero + terceiroNumero < segundoNumero) or \
   (segundoNumero + terceiroNumero < primeiroNumero):
    print("Seus números nao formam um triangulo!")
elif (primeiroNumero == segundoNumero) and (primeiroNumero == terceiroNumero):
    print("Seu triangulo e: Equilatero")
elif (primeiroNumero == segundoNumero) or \
     (primeiroNumero == terceiroNumero) or \
     (segundoNumero == terceiroNumero):
    print("Seu triangulo e: Isósceles")
else:
    print("Seu triangulo e: Escaleno")

