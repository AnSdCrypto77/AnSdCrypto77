# FERRAMENTA CRIADA PARA INSTALAÇÕES INICIAIS !
# SCRIPT DE CODIGO ABERTO.

# Codado by AN$_Cryptø
# Atualizado por Sr.Shift

import os
import pyfiglet

banner = pyfiglet.figlet_format(">> ConfT <<")
print(banner)

print("\n[*] Script Basica Para instalação De Pacotes !")
print('')
msg = input("Deseja continuar? [y / n]: ")

if msg == 'y' or msg == 'Y':
    print("[+] Instalando pacotes..")
    try:
        os.system("apt install python2 python3 nano vim tor nmap php dirb clang+  -y > /dev/null 2>&1")
        print("Os pacotes foram instalados: python2 nano vim tor nmap php dirb clang+  ")
    except:
        print("Houve uma falha ao instalar os pacotes [X]")

else:
    print("Saindo...")
