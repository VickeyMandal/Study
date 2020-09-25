
def checkk(password):
	count = 0  #0 1 2
	while count<3:
		user_in=input("Enter the password: ")
		if user_in!=password:
			count = count+1  #count += 1 0+1=1
			print("Invalid Password")
			if count == 3:
				print("Access Denied")
				break
		else:
			print("welcome")
			break


#main
password="abc"
checkk(password)




