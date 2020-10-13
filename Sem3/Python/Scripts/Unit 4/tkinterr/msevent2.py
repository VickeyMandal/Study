from tkinter import *
class enlargecircle:
	def __init__(self):
 		window.Tk()
 		self.radius=50
 		self.canvas=Canvas(window,bg="white",width=200,height=200)
 		self.canvas.pack()
 		self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tag='oval')
 		self.canvas.bind("<Button-1>",self.increasecircle)
 		self.canvas.bind("<Button-3>",self.decreasecircle)
 		window.mainloop()
	def increasecircle(self,event):
 		self.canvas.delete("oval")
 		if self.radius<100:
 			self.radius+=2
 			self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tag='oval')
	def decreasecircle(self,event):
 		self.canvas.delete("oval")
 		if self.radius>2:
 			self.radius-=2
 			self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tag='oval')
enlargecircle()