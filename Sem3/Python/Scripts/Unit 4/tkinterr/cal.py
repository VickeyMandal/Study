from tkinter import *

class MyWindow:
	def __init__(self,win):
		self.lb1=Label(win,text="First Number")
		self.lb2=Label(win,text="Second Number")
		self.lb3=Label(win,text="result")
		self.t1=Entry()
		self.t2=Entry()
		self.t3=Entry()
		self.lb1.place(x=100,y=0)
		self.lb2.place(x=200,y=75)
		self.lb3.place(x=250,y=100)
		self.t2.place(x=200,y=100)
		self.b1=Button(win,text="add",command=self.add)
		self.b2=Button(win,text="subtract")
		self.b2.bind("<Button-1>",self.sub)
		self.b1.place(x=100,y=150)
		self.b2.place(x=100,y=200)
		self.t3.place(x=200,y=200)
	def add(self):
		self.t3.delete(0,'end')
		num1=int(self.t1.get())
		num2=int(self.t2.get())
		result=num1+num2
		self.t3.insert(END,str(result))


	def sub(self,event):
		self.t3.delete(0,'end')
		num1=int(self.t1.get())
		num2=int(self.t2.get())
		result=num1-num2
		self.t3.insert(END,str(result))


window=Tk()
mywin=MyWindow(window)
window.geometry("400x400+50+50")
window=mainloop()
		