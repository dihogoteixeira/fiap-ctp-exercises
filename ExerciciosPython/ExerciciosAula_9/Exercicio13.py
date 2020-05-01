userPass=str(input("Digite a senha de usuario: ")).upper()

while userPass != 'FIAP1TDS':
    print("..::Você não tem acesso ao sistema::..")
    break
else:
    print('''
             __   ___                       __   __    /       
       ..   |__) |__   |\/|    \  / | |\ | |  \ /  \  /    ..  
     ....   |__) |___  |  |     \/  | | \| |__/ \__/ .     ....
    ''')
    print("..::Acesso permitido::..")