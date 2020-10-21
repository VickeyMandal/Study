from tkinter import *
root = Tk()
canvas=Canvas(root,width=800,height=800)
canvas.pack()
img=PhotoImage(file="me.png")
image=canvas.create_image(10,10,anchor=NW,image=img)
def move(event):
	if event.char=="a":
		canvas.move(image,-10,0)
	elif event.char=="d":
		canvas.move(image,10,0)
	elif event.char=="w":
		canvas.move(imaIe,0,-10)
	elif event.char=="s":
		canvas.move(image,0,10)
root.bind("<Key>",move)
root.mainloop()