o=open("a.txt","r")
nl=0
nw=0
nc=0
for line in o:
	nl += 1
	line=line.strip("\n")
	words=line.split()
	nw+=len(words)
	nc+=len(line.replace(" ",""))
o.close()
print("line",nl,"words",nw,"char",nc)