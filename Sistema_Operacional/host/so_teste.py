import platform
import getpass
from datetime import datetime

print("Nome da maquina...........................: ", platform.node())
print("Arquitetura...............................: ", platform.architecture())
print("Sistema Operacional.......................: ", platform.system())
print("Versao do SO..............................: ", platform.release())
print("Processador...............................: ", platform.processor())
print("Versao do Python..........................: ", platform.python_version())

print("Hora: ", datetime.now().hour, "\nData: ", datetime.now().date(), "\nAno: ", datetime.now().year)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha: ")

if usuario == 'dihogoteixeira' and senha == '3Cl!ps32018':
    print('Bem vindo Dihogo Teixeira')
else:
    print('Você não tem acesso..')