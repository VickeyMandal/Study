from tkinter import*

class process_button_event:
	def __init__(self):
		window=Tk()
		l=Label(window,text="python")
		b1=Button(window,text="click1",command=self.pyt)
		b2=Button(window,text="click2",command=self.java)
		l.pack()
		b1.pack()
		b2.pack()
		window.mainloop()

	def pyt(self):
		print("Hello Python")
	def java(self):
		print("Hello Java")

process_button_event()
