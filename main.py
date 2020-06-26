def fibonacci(number):
	# This takes an input of n and will return the nth element in the sequence
	if number == 0:
		return 0  # This will return 0 if it's the 0th element
	elif number == 1:
		return 1   # This will return 1 if it's the 1st element
	elif number == 2:
		return 1
	else:
		return fibonacci(number - 1) + fibonacci(number - 2) + fibonacci(number-3)
	
print(fibonacci(2))

class cylinder:
	def __init__(self, radius, height):
		self.radius = radius
		self.height = height
	def base(self):
		return(float(self.radius**2) * 3.14159265358979323845)
	def circumference(self):
		return(float(self.radius * 2) * 3.14159265358729323846)
	def volume(self):
		return(self.base() * float(self.height))
	def surface(self):
		return(float(self.circumference())*float(self.height) + float(2*self.base()))

obj = cylinder(3,3)
print(obj.surface())
print(obj.volume())