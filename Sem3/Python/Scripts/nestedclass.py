class student:
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
		self.lap = self.laptop()
	class laptop:
		def __init__(self):
			self.brand = "Msi"
			self.cpu = "i5"
			self.ram = 8

lap1=student.laptop()
print(lap1.brand)
s1 = student("Vickey",34)
print(s1.name, s1.roll)
print(s1.lap.brand,
	s1.lap.cpu,
	s1.lap.ram)
s2 = student("Tapas", 40)
print(s2.name,s2.roll)
print(s2.lap.brand,
	s2.lap.cpu,
	s2.lap.ram)

