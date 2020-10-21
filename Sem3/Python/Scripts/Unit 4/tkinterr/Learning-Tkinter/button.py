from tkinter import *

root = Tk() 


def click():
	mylabel=Label(root,text="oo LA la")
	mylabel.grid(row=1,column=0)

#creating a label
button1=Button(root,text="Click me!",padx=50,pady=20,fg="blue",bg="lime green",command=click)
button1.grid(row=0,column=0)

root.mainloop()
