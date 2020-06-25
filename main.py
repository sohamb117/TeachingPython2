food = ["caramel ice cream", "cake", "cookies", "flan", "vanilla ice cream", "brownies", "coffee ice cream"]
item = input("Which dessert do you want?")
for i in food:
	if i == item:
		print(i)
		food.remove(i)
		break
else: 
	print("Item not in menu")
print(food)
