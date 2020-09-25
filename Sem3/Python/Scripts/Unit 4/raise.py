import os.path
import sys
def main():
	f1=input("Enter File: ").strip()
	f2=input("Target file: ").strip()
	if os.path.isfile(f2):
		print("exists")
		sys.exit()
	i=open(f1,"r")
	o=open(f2,"w")
	c1=0
	cc=0
	for line in i:
		c1+=1
		cc+=len(line)
		o.write()
	print(c1,"lines",cc,"char")
	i.close()
	o.close()
main()