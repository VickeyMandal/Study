class Valuelarge(Exception):
	pass
class Valuelsmall(Exception):
	pass

n=10

while True:
	try:
		i=int(input("Enter number: "))
		if i<n:
			raise Valuelsmall
		elif i>n:
			raise Valuelarge
		break
	except Valuelsmall:
		print("Too small")
	except Valuelarge:
		print("too large")
print("Correct Guess")
