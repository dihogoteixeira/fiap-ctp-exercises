import socket

resp="S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP referente a url é: ", ip)
    resp=input("Digite <s> para coninuar: ").upper()