class car:
	wheels=4
	def __init__(self):
		self.mil = 10
		self.com = "BMW"

car1=car()
car2=car()
car2.mil=12
car2.wheels=3	
print(car1.mil,car1.com,car	1.wheels)
print(car2.mil,car2.com,car2.wheels)