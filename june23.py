animal_list = ["dog", "cat", "frog", "mouse"]

def add(item):
	animal_list.append(item)

def remove(item):
	if item in animal_list:
		animal_list.remove(item)

command = input("Add or Remove?")

if command == "Add":
	item = input("Item?")
	add(item)
elif command == "Remove":
	item = input("Item?")
	remove(item)

print(animal_list)