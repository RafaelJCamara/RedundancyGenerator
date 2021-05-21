# Apenas sei fazer um Hello World em Python, um BOM Hello World 
# mas vamos ver o que sai daqui
# Good luck boohoo =D

import configparser

def readfile():
    parser = configparser.ConfigParser()
    file = input("Qual o nome do ficheiro de configurações: ")
    parser.read(file)

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

    #base1 = str(parser.get("config","base1"))

def OutputFile():
    parser = configparser.ConfigParser()
    configfile = input("Qual o nome do ficheiro de configurações: ")
    parser.read(configfile)
    base_1 = int(parser.get("config","leaf_switches"))
    base_2 = int(parser.get("config","spine_switches"))
    ip_base = str(parser.get("config","network"))

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
    f.write("                   ipBase='"+ip_base+"')\n")
    f.write("\n")
    f.write("    info( '*** Adding controller\\n' )\n")
    f.write("    c0 = net.addController(name='c0',\n")
    f.write("                   controller=Controller,\n")
    f.write("                   protocol='tcp',\n")
    f.write("                   port=6633)\n")
    f.write("    info( '*** Add switches\\n')\n")
    # Quero algo assim "s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')"


    for switch_numero in range(0,base_1):
        # f.write("    s"+str(switch_numero+1)+" = net.addSwitch('s"+str(switch_numero+1)+"', cls=OVSKernelSwitch, failMode='standalone')\n")
        f.write("    l"+str(switch_numero+1)+" = net.addSwitch('l"+str(switch_numero+1)+"', cls=OVSKernelSwitch, failMode='standalone')\n")

    #Pensamento para estas duas variaveis, conforme o número de switchs adicionados na base 1
    #vamos ter o mesmo número de switchs na base 2
    # base_2_start = base_1
    # base_2_end = base_1 + base_2

    for switch_numero in range(0,base_2):
        # f.write("    s"+str(switch_numero+1)+" = net.addSwitch('s"+str(switch_numero+1)+"', cls=OVSKernelSwitch, failMode='standalone')\n")
        f.write("    c"+str(switch_numero+1)+" = net.addSwitch('c"+str(switch_numero+1)+"', cls=OVSKernelSwitch, failMode='standalone')\n")

    f.write("\n")
    f.write("    info( '*** Add hosts\\n')\n")
    for host_numero in range(0,base_1):
        f.write("    h"+str(host_numero+1)+" = net.addHost('h"+str(host_numero+1)+"', cls=Host)\n")

    f.write("\n")
    f.write("    info( '*** Add links\\n')\n")
    #Link dos hosts
    for host_numero in range(0,base_1):
        #Quero algo assim "net.addLink(h1, s1)"
        f.write("    net.addLink(h"+str(host_numero+1)+", l"+str(host_numero+1)+")\n")
    


    # TEM AQUI UM BUG VER OUTPUT FILE, FICA A FALTAR SWITCHS
    #for x_base1 in range(0,base_1):
        #for y_base2 in range(0,base_2_end):
            #if x_base1 > y_base2:
                #f.write("    net.addLink(s"+str(x_base1+1)+", s"+str(y_base2+1)+")\n")

    #Bug fix ? Testar a ver se já printa todas os switchs, parece que sim
    # for x in range(0,base_2_end):
    #     for y in range(0,base_1):
    #         if x > y:
    #             f.write("    net.addLink(s"+str(x+1)+", s"+str(y+1)+")\n")
    for x in range(base_1):
        for y in range(base_2):
            f.write("    net.addLink(l" + str(x + 1) + ", c" + str(y + 1) + ")\n")

    f.write("\n")
    f.write("    info( '*** Starting network\\n')\n")
    f.write("    net.build()\n")

    f.write("    info( '*** Starting controllers\\n')\n")
    f.write("    for controller in net.controllers:\n")
    f.write("        controller.start()\n")
    f.write("\n")
    f.write("    info( '*** Starting switches\\n')\n")
    for host_numero in range(base_1):
        f.write("    net.get('l"+str(host_numero+1)+"').start([c0])\n")
    for host_numero in range(base_2):
        f.write("    net.get('c"+str(host_numero+1)+"').start([c0])\n")
    
    f.write("\n")
    f.write("\n")
    f.write("    CLI(net)\n")
    f.write("    net.stop()\n")
    f.write("\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    setLogLevel( 'info' )\n")
    f.write("    myNetwork()\n")
    f.write("\n")

    f.close()
    print("Gravado com sucesso em "+user_output_file)

def CreateFile():
    config_output_file = input("Qual o nome do ficheiro de output: ")
    spine_switches= input("Numero de spine switchs ? ")
    leaf_switchs = input("Numero de leaf switchs ? ")
    redundancy = input("Nivel de redundancia ? ")
    network = input("Game de endereços ? Por exemplo, 192.168.0.0/16 ")

    f = open(config_output_file, "w")
    f.write("[config]\n")
    f.write("spine_switches="+spine_switches+"\n")
    f.write("leaf_switchs="+leaf_switchs+"\n")
    f.write("redundancy="+redundancy+"\n")
    f.write("network="+network+"\n")
    f.close()
    print("Gravado com sucesso em "+config_output_file)

def menu():

    loop = True
    input_user = -1

    #Enquanto o valor de loop for True mostrar o menu
    while loop: 
        print(30 * "-", "SDN Gerador de redudancia", 30 * "-")
        print("1. Ler o ficheiro de configurações ")
        print("2. Criar o ficheiro de output ")
        print("3. Criar o ficheiro de configurações ")          
        print("9. Sair deste programa ")
        print(73 * "-")
        input_user = input("Escolher a opção a realizar: ")

        if input_user == '1':
            readfile()
        elif input_user == '2':
            OutputFile()
        elif input_user == '3':
            CreateFile()
        elif input_user == '4':
            loop = False
        elif input_user == '9':
            print("Sair..")
            loop = False  # Termina o loop do menu
        else:
            # Para valores colocados fora do pretendido print de mensagem de aviso
            input("Numero colocado não corresponde a nenhuma opção, tentar novamente..")

menu()