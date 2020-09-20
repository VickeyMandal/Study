class computer:

	def __init__(self,cpu,ram):
		self.cpu=cpu
		self.ram=ram

	def p(self):
		print(self.cpu,self.ram)
		
obj=computer("i5","8GB")
obj1=computer("Ryzen 3","4GB")
obj.p()
obj1.p()	