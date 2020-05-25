contaCliente = input("Digite seu codigo de verificacao de 3 digitos: ")
verificadorCliente = contaCliente[::-1]
somaNumeroConta = int(contaCliente) + int(verificadorCliente)
multiplicaDigito = list(str(somaNumeroConta))
digitoVerificador = int(multiplicaDigito[0]) *1 + int(multiplicaDigito[1]) *2 + int(multiplicaDigito[2]) *3
exibirDigitoVerificador = list(str(digitoVerificador))
print("Valor da verificacao: ",  exibirDigitoVerificador[1])