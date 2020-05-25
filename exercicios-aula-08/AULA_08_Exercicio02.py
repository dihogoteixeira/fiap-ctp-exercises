# INFORMACOES DO PASSAGEIRO
nomePassageiro = input("Digite o nome do Passageiro: ")
numDestino = int(input("Veja nossa Lista de destinos:\n01 - Norte no valor de: R$ 280,00\n02 - Nordeste no valor de: R$ 380,00\n03 - Centro-Oeste no valor de: R$ 620,00\nEscolha o numero do seu destino:"))
pacoteIdaVolta = input("Deseja comprar o pacote de ida e volta? 'SIM' ou 'NAO'").upper()
# VARIAVEIS
idaNorte = 280
idaNordeste = 380
idaCentroOeste = 620
voltaNorte = 400
voltaNordeste = 628
voltaCentroOeste = 1100
# VALOR PACOTE DE IDA
if numDestino == "01" and pacoteIdaVolta == "NAO":
    print(nomePassageiro + ", o valor da passagem IDA e de: " + str(idaNorte))
elif numDestino == "02" and pacoteIdaVolta == "NAO":
    print(nomePassageiro + ", o valor da passagem IDA e de: " + str(idaNordeste))
elif numDestino == "03" and pacoteIdaVolta == "NAO":
    print(nomePassageiro + ", o valor da passagem IDA e Volta e de: " + str(idaCentroOeste))
# VALOR PACOTE DE IDA E VOLTA
if numDestino == "01" and pacoteIdaVolta == "SIM":
    print(nomePassageiro + ", o valor da passagem IDA e Volta de: " + str(voltaNorte))
elif numDestino == "02" and pacoteIdaVolta == "SIM":
    print(nomePassageiro + ", o valor da passagem IDA e Volta de: " + str(voltaNordeste))
elif numDestino == "03" and pacoteIdaVolta == "SIM":
    print(nomePassageiro + ", o valor da passagem IDA e Volta de: " + str(voltaCentroOeste))
else:
    print("Responda comprar o pacote de ida e volta com SIM ou NAO")









