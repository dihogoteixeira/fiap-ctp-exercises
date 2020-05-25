nome = input("Ola, digite o seu nome: ")
print("Bem-vindo, {}!\n".format(nome), end=" ")
numero = float(input("Digite um numero': "))

if numero >=0 and numero <=30:
    print(str(nome), ", o número digitado está compreendido entre 0 e 30.")
elif numero >=40 and numero <=79:
    print(str(nome), ", o número digitado está compreendido entre 40 e 79.")
else:
    print(str(nome), ", o número digitado está fora dos limites estabelecidos.")