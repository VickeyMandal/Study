class students:
	school = "Kendriya Vidyalaya"
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def avg(self):
		print((self.m1+self.m2+self.m3)/3)
	def get_school_name(cls):
		print(cls.school)
	def info():
		print("Hello there!")
s1 = students(21,23,43)
s2 = students(43,65,21)
s1.avg()
s2.avg()
s1.get_school_name()
students.info()


		