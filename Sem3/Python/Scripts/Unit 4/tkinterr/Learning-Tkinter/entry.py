from tkinter import *

root = Tk()


e=Entry(root,width=20,bg="blue",fg="white")
e.grid(row=0,column=0)
e.insert(0,"Enter your name")

def click():
	hello = "Hello! "+e.get()
	mylabel=Label(root,text=hello)
	mylabel.grid(row=2,column=0)

#creating a label
button1=Button(root,text="Click me!",padx=50,pady=20,fg="blue",bg="lime green",command=click)
button1.grid(row=1,column=0)

root.mainloop()
