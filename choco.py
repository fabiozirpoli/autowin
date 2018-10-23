import subprocess
import time
from subprocess import check_output

#Declarando Variaveis
programas = []
install = []
notfound = []
stop = 0
loop = 0
CREATE_NO_WINDOW = 0x08000000

print ("1 - Programas Basico + Configuração Básicas")
print ("2 - Programas Básicos")
print ("3 - Configurações Básicas")
print ("4 - Programas Específicos + Configurações Básicas")
print ("5 - Programas Específicos")
print ("6 - Procurar por Programa")

option = input("Selecione a opção desejada")

#CHOCO INSTALL
installer = "@powershell -NoProfile -ExecutionPolicy Bypass -Command 88iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))88 && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin".replace('88','"')
def chocoinstall:
    subprocess.call(installer, shell=True)

#CHOCO BASICOS
basic = "choco install googlechrome winrar teamviewer jre8 firefox anydesk dotnet4.6 -y"
def chocobasic:
    subprocess.call(basic)
    print("Instalando Programas Básicos")

#CONFIGURAÇÕES
#SET DNS
def dns:
    subprocess.call("netsh interface ip set dns name='Ethernet' source='static' address='8.8.8.8'", creationflags=CREATE_NO_WINDOW)
    subprocess.call("netsh interface ip add dns name='Ethernet' addr='8.8.4.4' index=2", creationflags=CREATE_NO_WINDOW)
    subprocess.call("netsh interface ipv4 add dnsserver 'Conexão Local' address='8.8.8.8' index=1", creationflags=CREATE_NO_WINDOW)
    subprocess.call("netsh interface ipv4 add dnsserver 'Conexão Local' address='8.8.4.4' index=2", creationflags=CREATE_NO_WINDOW)
    print("Configurando DNS da Google")

#DISABLE WINDOWS UPDATE
def dupdate:
    subprocess.call("net stop wuauserv", creationflags=CREATE_NO_WINDOW)
    subprocess.call("sc config wuauserv start= disabled", creationflags=CREATE_NO_WINDOW)
    print("Desativando Windows Update")

#DISABLE WINDOWS DEFENDER
def ddefender:
    subprocess.call("sc config WinDefend start= disabled", creationflags=CREATE_NO_WINDOW)
    subprocess.call("sc stop WinDefend", creationflags=CREATE_NO_WINDOW)
    subprocess.call("REG ADD 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender'  /t REG_DWORD /v DisableAntiSpyware /D 1 /f", creationflags=CREATE_NO_WINDOW)
    print("Desativando Windows Defender")

#DISABLE WINDOWS FIREWALL
def dfirewall:
    subprocess.call("NetSh Advfirewall set allprofiles state off", creationflags=CREATE_NO_WINDOW)
    print("Desativando Firewall do Windows")

#definindo configurações basicas
def config:
    dns()
    dupdate()
    ddefender()
    dfirewall()

#PROGRAMAS BASICOS + CONFIGURAÇÕES BASICAS
if option == 1:
    chocoinstall()
    chocobasic()
    config()

#PROGRAMAS BASICOS
if option == 2:
    chocoinstall()
    chocobasic()

#CONFIGURAÇÃO BASICA
if option == 3:
    config()

#PROGRAMAS BASICOS
#Lendo nome de programas até vazio
if option == 4:
    chocoinstall()
    config()
    print("Insira os programas que deseja instalar, caso concluido, deixe em branco e aperte ENTER!")
    while stop == 0 : 
        nameprog = raw_input("Escreva um programa: ")
        if nameprog:
            if nameprog in programas:
                print("Este programa ja esta listado.")
            else:
                programas.append(nameprog)
        else:
            stop = 1

    print ("Verificando pacotes, aguarde...")
    choco1 = ' '.join(programas)
    #verificando se possui no choco para instalar
    chocosearch = ("choco search "+ choco1)
    out = check_output(chocosearch, creationflags=CREATE_NO_WINDOW)
    for line in out.splitlines():
        for name in programas:
            if name in line.lower() and "Approved" in line:
                if name not in install:
                    install.append(name)
            else:
                if name not in notfound and name not in install:
                    notfound.append(name)

    if notfound:
        print ("Alguns programas não foram encontrados.")
    if install:
        chocoinstall3 = ' '.join(install)
        print ("Os seguintes programas estão sendo instalados: " + chocoinstall3)
        chocoinstall2 = ("choco install "+ chocoinstall +" -y")
        subprocess.call(chocoinstall2, creationflags=CREATE_NO_WINDOW)


#DNS

#DNS Windows 7

#DESATIVA ATUALIZAÇÃO
print("Desativando Atualizações Automaticas do Windows")

#DESATIVA WINDOWS DEFENDER
print("Desativando Windows Defender")

#DESATIVA WINDOWS FIREWALL
print("Desativando Firewall do Windows")

#Informa na tela e instala programas

print ("Configuracoes e Instalacoes Concluidas")




