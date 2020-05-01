nome = input("Ola, digite o seu nome: ")
print("Bem-vindo, {}!\n".format(nome), end=" ")
valorProduto = float(input("\nDigite o valor do produto: "))

if valorProduto <= 20.00:
    print("Aplicado lucro de 45%. o valor a ser pago e de: ", valorProduto + valorProduto/100*45)
elif valorProduto > 20.00:
    print("Aplicado lucro de 30%. o valor a ser pago e de: ",  valorProduto + valorProduto/100*30)