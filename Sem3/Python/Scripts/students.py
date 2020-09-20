class students:
	school = "Kendriya Vidyalaya"
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def p(self):
		print(self.school,self.m1,self.m2,self.m3)
s1 = students(21,23,43)
s2 = students(43,65,21)
s1.p()
s2.p()



		