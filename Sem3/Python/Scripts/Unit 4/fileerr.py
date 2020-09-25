# f=input("Enter file: ")
# try:
# 	o=open(f,"r")
# except:
# 	print("No file")

# try:
# 	list=5*[0]
# 	x=list[5]
# except IndexError:
# 	print("Index Out of Bound")

def main():
	try:
		n1=int(input())
		n2=int(input())
		r=n1/n2
		print(r)
	except ZeroDivisionError:
		print("Division by error")
	except:
		print("Something incorrect")
	else:
		print("No exception")
	finally:
		print("finally")

main()