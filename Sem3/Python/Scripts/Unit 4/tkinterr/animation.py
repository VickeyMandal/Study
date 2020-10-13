from tkinter import *

class controlanimation:
	def __init__(self):
		window=Tk()
		self.width=250
		self.canvas=Canvas(window,bg="white",width=self.width,height=50)
		self.canvas.pack()
		frame=Frame(window)
		frame.pack()
		btstop=Button(frame,text="Stop",command=self.stop)
		btstop.pack(side=LEFT)
		btresume=Button(frame,text="Resume",command=self.resume)
		btresume.pack(side=LEFT)
		btfaster=Button(frame,text="faster",command=self.faster)
		btfaster.pack(side=LEFT)
		btslower=Button(frame,text="Slower",command=self.slower)
		btslower.pack(side=LEFT)
		self.x=0
		self.sleeptime=100
		self.canvas.create_text(self.x,30,text="message moving?",tags="text")
		self.dx=3
		self.isStopped=False
		self.animate()
		window.mainloop()
	def stop(self):
		self.isStopped=True
	def resume(self):
		self.isStopped=False
		self.animate()
	def faster(self):
		if self.sleeptime>5:
			self.sleeptime-=20
	def slower(self):
		self.sleeptime+=20			
	def animate(self):
		while not self.isStopped:
			self.canvas.move("text",self.dx,0)
			self.canvas.after(self.sleeptime)
			self.canvas.update()
			if self.x<self.width:
				self.x+=self.dx
			else:
				self.x=0
				self.canvas.delete("text")
				self.canvas.create_text(self.x,30,text="message moving",tags="text")

controlanimation()