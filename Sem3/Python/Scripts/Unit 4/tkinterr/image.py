from tkinter import *
class imagedemo:
	def __init__(self):
		window=Tk()
		a=PhotoImage(file="me.png")
		frame1=Frame(window)
		frame1.pack()
		canvas=Canvas(frame1)
		canvas.create_image(90,50,image=a)
		canvas["width"]=200
		canvas["height"]=100
		canvas.pack(side=LEFT)
		frame2=Frame(window)
		frame2.pack()
		Button(frame2,image=a).pack(side=LEFT)
		Checkbutton(frame2,image=a).pack(side=LEFT)
		Radiobutton(frame2,image=a).pack(side=LEFT)
		window.mainloop()
imagedemo()