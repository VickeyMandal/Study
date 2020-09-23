i=open("emp.txt","r")
bonus=10
for line in i:
	name,job,income=line.split(" ")
	# last,first=name.split()
	income=int(income)
	income=income+(income*bonus)
	print("Name: ",name,"\tJob: ",job,"\tIncome: ",income)
i.close()