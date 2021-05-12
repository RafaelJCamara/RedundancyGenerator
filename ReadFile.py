import configparser

parser = configparser.ConfigParser()
parser.read("demofile.txt")

print("Spine switches:")
print(parser.get("config","spine_switches"))
spine_switches = parser.get("config","spine_switches")

print("leaf switches:")
print(parser.get("config","leaf_switches"))
leaf_switches = parser.get("config","leaf_switches")


print("redundancy:")
print(parser.get("config","redundancy"))
redundancy = parser.get("config","redundancy")

print("Network:")
print(parser.get("config","network"))
network = str(parser.get("config","network"))
