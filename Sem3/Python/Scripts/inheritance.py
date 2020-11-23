class a:
	# def __init__(self):
	# 	print("In init A")
	def feature1(self):
		print("feature 1 is working")
	def feature2(self):
		print("feature 2 is working")
class b:
	def __init__(self):
		super().__init__()
		print("In init B")
	def feature3(self):
		print("feature 3 is working")
	def feature4(self):
		print("feature 4 is working")
class c(a,b):
	def __init__(self):
		super().__init__()
		print("In init C")
	def feature5(self):
		print("feature 5 is working")
	def feature6(self):
		print("feature 6 is working")	

c1 = b()
c1.feature3()
