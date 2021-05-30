import configparser

user_output_file = ""

def readfile():
    parser = configparser.ConfigParser()
    file = input("Qual o nome do ficheiro de configurações: ")
    parser.read(file)

    spine_switches = parser.get("config","spine_switches")
    print("Spine switches: " + spine_switches)

    leaf_switches = parser.get("config","leaf_switches")
    print("Leaf switches: " + leaf_switches)

    redundancy = parser.get("config","redundancy")
    print("Redundancy: " + redundancy)

    network = str(parser.get("config","network"))
    print("Network: " + network )


def generateMininetEditScript(network, numberOfSpineSwitches, numberOfLeafSwitches, redundancyLevel):
    f = open(user_output_file+".mn", "w")
    f.write("{\n")
    f.write('   "application": {\n')
    f.write('       "dpctl": "",\n')
    f.write(f'       "ipBase": "{network}",\n')
    f.write('       "netflow": {\n')
    f.write('           "nflowAddId": "0",\n')
    f.write('           "nflowTarget": "",\n')
    f.write('           "nflowTimeout": "600"\n')
    f.write('       },\n')
    f.write('       "openFlowVersions": {\n')
    f.write('           "ovsOf10": "1",\n')
    f.write('           "ovsOf11": "0",\n')
    f.write('           "ovsOf12": "0",\n')
    f.write('           "ovsOf13": "0"\n')
    f.write('       },\n')
    f.write('       "sflow": {\n')
    f.write('           "sflowHeader": "128",\n')
    f.write('           "sflowPolling": "30",\n')
    f.write('           "sflowSampling": "400",\n')
    f.write('           "sflowTarget": ""\n')
    f.write('       },\n')
    f.write('       "startCLI": "0",\n')
    f.write('       "switchType": "ovs",\n')
    f.write('       "terminalType": "xterm"\n')
    f.write('   },\n')
    f.write('   "controllers": [\n')
    f.write('       {\n')
    f.write('           "opts": {\n')
    f.write('               "controllerProtocol": "tcp",\n')
    f.write('               "controllerType": "ref",\n')
    f.write('               "hostname": "c0",\n')
    f.write('               "remoteIP": "127.0.0.1",\n')
    f.write('               "remotePort": 6633\n')
    f.write('           },\n')
    f.write('           "x": "400.0",\n')
    f.write('           "y": "70.0"\n')
    f.write('       }\n')
    f.write('   ],\n')
    f.write('   "hosts": [\n')
    for i in range(numberOfLeafSwitches):
        f.write('       {\n')
        f.write(f'           "number": "{i+1}",\n')
        f.write('           "opts": {\n')
        f.write(f'               "hostname": "h{i+1}",\n')
        f.write(f'               "nodeNum": {i+1},\n')
        f.write('               "sched": "host"\n')
        f.write('           },\n')
        f.write(f'           "x": "{50+100*i}",\n')
        f.write('           "y": "400"\n')
        if i<numberOfLeafSwitches-1:
            f.write('       },\n')
        else:
            f.write('       }\n')
    f.write('   ],\n')


    f.write('   "links": [\n')
    for i in range(numberOfLeafSwitches):
        for a in range(redundancyLevel):
            f.write('       {\n')
            f.write(f'           "dest": "c{a+1}",\n')
            f.write('           "opts": {},\n')
            f.write(f'           "src": "l{i+1}"\n')
            f.write('       },\n')

    for i in range(numberOfLeafSwitches):
        f.write('       {\n')
        f.write(f'          "dest": "l{i + 1}",\n')
        f.write('           "opts": {},\n')
        f.write(f'          "src": "h{i + 1}"\n')
        if i < numberOfLeafSwitches -1:
            f.write('       },\n')
        else:
            f.write('       }\n')

    f.write('   ],\n')


    f.write('   "switches": [\n')
    for i in range(numberOfSpineSwitches):
        f.write('       {\n')
        f.write(f'          "number": "{i+1}",\n')
        f.write('           "opts": {\n')
        f.write('               "controllers": [\n')
        f.write('                   "c0"\n')
        f.write('               ],\n')
        f.write(f'               "hostname": "c{i+1}",\n')
        f.write(f'               "nodeNum": {i+1},\n')
        f.write('               "switchType": "default"\n')
        f.write('           },\n')
        f.write(f'           "x": "{50+100*i}",\n')
        f.write(f'           "y": "150"\n')
        f.write('       },\n')
    for a in range(numberOfLeafSwitches):
        f.write('       {\n')
        f.write(f'           "number": "{numberOfSpineSwitches + a + 1}",\n')
        f.write('           "opts": {\n')
        f.write('               "controllers": [\n')
        f.write('                   "c0"\n')
        f.write('               ],\n')
        f.write(f'               "hostname": "l{a+1}",\n')
        f.write(f'               "nodeNum": {numberOfSpineSwitches+a+1},\n')
        f.write('               "switchType": "default"\n')
        f.write('           },\n')
        f.write(f'           "x": "{50+a*130}",\n')
        f.write('           "y": "300"\n')
        if a < numberOfLeafSwitches - 1:
            f.write('       },\n')
        else:
            f.write('       }\n')
    f.write('   ],\n')
    f.write('   "version": "2"\n')
    f.write("}\n")
    f.write("\n")
    f.close()
    print("Mininet topology saved with success in "+user_output_file+".mn")

def OutputFile():
    parser = configparser.ConfigParser()
    configfile = input("Qual o nome do ficheiro de configurações: ")
    parser.read(configfile)
    base_1 = int(parser.get("config","leaf_switches"))
    base_2 = int(parser.get("config","spine_switches"))
    ip_base = str(parser.get("config","network"))
    redundancy = int(parser.get("config","redundancy"))

    global user_output_file
    user_output_file = input("Qual o nome do ficheiro de output: ")
    f = open(user_output_file+".py", "w")

    f.write("#!/usr/bin/env python\n")
    f.write("\n")
    f.write("from mininet.topo import Topo\n")
    f.write("from mininet.link import TCLink\n")
    f.write("class MyTopo( Topo ):\n")
    f.write("   def build(self):\n")

    for i in range(base_1):
        f.write(f"      h{i+1} = self.addHost('h{i+1}', ip='10.0.0.{i+1}')\n")
    for i in range(base_1):
        f.write(f"      l{i + 1} = self.addSwitch('l{i + 1}')\n")
    for i in range(base_2):
        f.write(f"      c{i + 1} = self.addSwitch('c{i + 1}')\n")

    for x in range(base_1):
        for y in range(base_2):
            if y+1<=redundancy:
                f.write(f"      self.addLink(l" + str(x + 1) + ", c" + str(y + 1) + ", cls=TCLink)\n")

    for x in range(base_1):
        f.write(f"      self.addLink(h" + str(x + 1) + ", l" + str(x + 1) + ", cls=TCLink)\n")


    f.write("topos = { 'mytopo': ( lambda : MyTopo() ) }\n")
    f.close()
    print("Gravado com sucesso em "+user_output_file)
    generateMininetEditScript(ip_base,base_2,base_1,redundancy)

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
            loop = False
        else:
            input("Numero colocado não corresponde a nenhuma opção, tentar novamente..")

menu()