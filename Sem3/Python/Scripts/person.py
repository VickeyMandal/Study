class person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def compare(self, other):
		if self.age==other.age:
			return True
		else:
			return False

obj=person("Vickey",22)
obj1=person("Tapas",26)
if obj.compare(obj1):
	print("They are same")
else:
	print("They are different")

