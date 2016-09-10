#Hero's Inventory
#Demonstrates Lists

#Create a list with some items and display with a for loop
inventory = ["sword", "armour", "shield", "healing potion"]
print("Your items:")
for item in inventory:
	print(item)

#get the length of list
print("You have", len(inventory), "items in your possession")

#test for membership with in
if "healing potion" in inventory:
	print("You will live to fight another day")
	
input("\nPress the enter key to continue.") 