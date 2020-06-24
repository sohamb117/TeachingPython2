print("this is such a nice example", end = ',')
print("and i'm so glad that this line is on the same line as the other one", end="\t")
print("this one is tabbed out from the last one\n truly strange that this one is on a new line")
words = input()
if words == "password":
	print("You got the password!")
elif words == "password2":
	print("You got the second password!")
else:
	print("You did not get the password")