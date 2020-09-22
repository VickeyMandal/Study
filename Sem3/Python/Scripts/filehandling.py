a = open("firstfile.txt","w")
a.write("Hello python\n")
a.write("Java\n")
a.write("c++")
a.close()

#read
b = open("firstfile.txt","r")
print("1.Using read()")
# print(b.read())
# print(b.read(4))
# print(b.read(10))
# print(b.readline())
print(b.readlines())
b.close

