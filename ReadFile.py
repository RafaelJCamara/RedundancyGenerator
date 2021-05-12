# Apenas sei fazer um Hello World em Python, um BOM Hello World 
# mas vamos ver o que sai daqui
# Good luck boooooooy =D

import configparser
def readfile():
    parser = configparser.ConfigParser()
    parser.read("config_file.txt")


    #Guardar na variavel o valor que vem do ficheiro
    #Dar print desse valor
    spine_switches = parser.get("config","spine_switches")
    print("Spine switches: " + spine_switches)


    leaf_switches = parser.get("config","leaf_switches")
    print("Leaf switches: " + leaf_switches)


    redundancy = parser.get("config","redundancy")
    print("Redundancy: " + redundancy)


    network = str(parser.get("config","network"))
    print("Network: " + network )

def OutputFile():
    user_output_file = input("Qual o nome do ficheiro de output: ")
    f = open(user_output_file, "w")

    f.write("#!/usr/bin/env python\n")
    f.write("\n")
    f.write("from mininet.net import Mininet\n")
    f.write("from mininet.node import Controller, RemoteController, OVSController\n")
    f.write("from mininet.node import CPULimitedHost, Host, Node\n")
    f.write("from mininet.node import OVSKernelSwitch, UserSwitch\n")
    f.write("from mininet.node import IVSSwitch\n")
    f.write("from mininet.cli import CLI\n")
    f.write("from mininet.log import setLogLevel, info\n")
    f.write("from mininet.link import TCLink, Intf\n")
    f.write("from subprocess import call\n")
    f.write("\n")
    f.write("def myNetwork():\n")
    f.write("\n")
    f.write("    net = Mininet( topo=None,\n")
    f.write("                   build=False,\n")
    f.write("                   ipBase='10.0.0.0/8')\n")
    f.write("\n")
    f.write("    info( '*** Adding controller\\n' )\n")
    f.write("    info( '*** Add switches\\n')\n")
    # Quero algo assim "s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')"

    base_1 = int(input("Quantos switchs base 1: "))

    for switch_numero in range(0,base_1):
        f.write("    s"+str(switch_numero)+" = net.addSwitch('s"+str(switch_numero)+"', cls=OVSKernelSwitch, failMode='standalone')\n")

    f.write("\n")
    f.write("    info( '*** Add hosts\\n')\n")
    for host_numero in range(0,base_1):
        f.write("    h"+str(host_numero)+" = net.addHost('h"+str(host_numero)+"', cls=Host)\n")

    f.write("\n")
    


def menu():

    loop = True
    input_user = -1

    #Enquanto o valor de loop for True mostrar o menu
    while loop: 
        print(30 * "-", "SDN Gerador de redudancia", 30 * "-")
        print("1. Ler o ficheiro de configurações ")
        print("2. Criar o ficheiro de output ")         
        print("9. Sair deste programa ")
        print(73 * "-")
        input_user = input("Escolher a opção a realizar: ")

        if input_user == '1':
            readfile()
        elif input_user == '2':
            OutputFile()
        elif input_user == '3':
            loop = False
        elif input_user == '4':
            loop = False
        elif input_user == '9':
            print("Sair..")
            loop = False  # Termina o loop do menu
        else:
            # Para valores colocados fora do pretendido print de mensagem de aviso
            input("Numero colocado não corresponde a nenhuma opção, tentar novamente..")



menu()

