import configparser

parser = configparser.ConfigParser()
parser.read("config_file.txt")

#Guardar na variavel o valor que vem do ficheiro
#Dar print desse valor
spine_switches = parser.get("config","spine_switches")
print("Spine switches:" + spine_switches)


leaf_switches = parser.get("config","leaf_switches")
print("Leaf switches:" + leaf_switches)


redundancy = parser.get("config","redundancy")
print("Redundancy:" + redundancy)


network = str(parser.get("config","network"))
print("Network:" + network )
