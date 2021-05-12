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



#f = open("demofile.txt", "r")
#print(f.read(5))


# Append
#f = open("demofile2.txt", "a")
#f.write("Now the file has more content!")
#f.close()

#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())


# Overwrite
#f = open("demofile3.txt", "w")
#f.write("Woops! I have deleted the content!")
#f.close()

#open and read the file after the appending:
#f = open("demofile3.txt", "r")
#print(f.read())