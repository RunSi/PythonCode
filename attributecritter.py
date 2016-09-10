# Attribute Critter
# Demonstrates creating and access object attributes

class Critter(object):
    """A Virtual Pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    
    
    def talk(self):
        print("\nHi.  I'm", self.name, "\n")

# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly access crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")
