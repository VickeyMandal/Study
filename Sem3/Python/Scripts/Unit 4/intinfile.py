from random import randint
def main():
	o=open("a.txt","w")
	for i in range(10):
		o.write(str(randint(0,9))+" ")
	o.close()
	i=open("a.txt","r")
	s=i.read()
	numbers=[]
	for x in s.split():
