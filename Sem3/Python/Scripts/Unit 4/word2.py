def main():

	while True:
		try:
			f=input("Enter file Name: ")
			i=open("f","r")
			break
		expect IOError:
			print("try again")
	counts=26*[0]
	for line in i:
		countletters(line.lower(),counts)
	for i in range(len(counts)):
		if counts[i]!=0:
			print(chr(ord('a')+i)+ " appears "+str(counts[i])+" time")
def countletters(line,counts):
	for ch in line:
		if ch.isalpha():
			counts[ord(ch)-ord('a')]+=1

main()