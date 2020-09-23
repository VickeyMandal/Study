import os.path

def movedata(oldfile,newfile):
	f1=open(oldfile,"r")
	f2=open(newfile,"w")
	while True:
		text=f1.readline()
		if text=="":
			break
		if text[0]=="#":
			continue
		f2.write(text)
	f1.close()
	f2.close()



a = open("a.txt","w")
a.write("#java\n")
a.write("python\n")
a.write("c")
a.close()

movedata("a.txt","ga.txt")

# b=open("ga.txt","r")
# print(b.read())

print(os.path.isfile("ga.txt"))