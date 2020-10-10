import pickle
# def main():
# 	o=open("ad.dat","wb")
# 	pickle.dump(12.3,o)
# 	pickle.dump([1,2,3],o)
# 	o.close()
# 	i=open("ad.dat","rb")
# 	print(pickle.load(i))
# 	print(pickle.load(i))
# 	i.close()
# main()


def main():
	o=open("ad.dat","wb")
	data=int(input("enter"))
	while(data!=0):
		pickle.dump(data,o)
		data=int(input("enter"))
	o.close()
	i=open("ad.dat","rb")
	eofile=False
	while not eofile:
		try:
			print(pickle.load(i),end=" ")
		except EOFError:
			eofile=True
	i.close()
	print("done")
main() 