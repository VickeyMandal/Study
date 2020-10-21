from tkinter import *

def submit():
	user=e1.get()
	passw=e2.get()
	login(user,passw)
def login(user,passw):
	try:
		db = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
		cursor=db.cursor()
		s="select * from cricketers"
		cursor.execute(s)
		m=cursor.fetchall()
		for x in m:
			print(x)
		print("Query executed")
	except:
		print("error occured")
root=Tk()
root.geometry('300x300')
l1=Label(root,text='Username')
e1=Entry(root,width=35)
l1.place(x=50,y=20)
e1.place(x=150,y=20)
l2=Label(root,text='Password')
e2.eNTRY(root,width=35)
l2.place(x=50,y=50)
e2.place(x=150,y=50)
s=Button(root,text='Login',command=submit)
s.place(x=150,y=135)
root.mainloop()