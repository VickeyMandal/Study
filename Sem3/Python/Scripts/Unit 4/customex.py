class NegativeAgeException(RuntimeError):
	pass

def enterage(age):
	if age<0:
		raise NegativeAgeException()
	if age%2==0:
		print("Even")
	else:
		print("odd")
try:
	num=int(input("Enter your age: "))
	enterage(num)
except NegativeAgeException:
	print("Positive number is allowed")
except:
	print("Something is wrong")