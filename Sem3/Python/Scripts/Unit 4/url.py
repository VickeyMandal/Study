import urllib.request
def main():
	url=input("Enter url: ")
	i=urllib.request.urlopen(url)
	d=i.read().decode()
	print(d)
main()
