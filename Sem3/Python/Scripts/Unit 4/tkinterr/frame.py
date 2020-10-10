from tkinter import*

class frame:
	def __init__(self):
		root=Tk()
		c=Canvas(root,bg='grey',height=100,width=200,cursor='pencil')
		id=c.create_line(0,0,50,20,fill='green',activefill='lightblue')
		id=c.create_line(0,100,50,80,fill='green',activefill='lightblue')
		id=c.create_line(150,20,200,0,fill='green',activefill='lightblue')
		id=c.create_line(150,80,200,100,fill='green',activefill='lightblue')
		c.pack()
		mainloop()


frame()

