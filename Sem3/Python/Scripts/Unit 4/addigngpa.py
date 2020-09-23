i = input("input file")
o = input("output file")
ifile=open(i,"r")
ofile=open(o,"w")
cgpa=0
for line in ifile:
	if line[0]=="A":
		cgpa = 9
	elif line[0]=="B":
		cgpa = 8
	else:
		cgpa = -1
	temp=str(cgpa)
	temp=temp+'\n'
	print(line[0], cgpa)
	ofile.write(temp)
ifile.close()
ofile.close()
