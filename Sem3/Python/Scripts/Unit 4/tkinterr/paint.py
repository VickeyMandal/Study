from tkinter import *

def paint(event):
	x1,y1=(event.x-1),(event.y-1)
	x2,y2=(event.x+1),(event.y+1)

w=Canvas(master,width=500,height=100)
w.pack(expand=YES,fill=BOTH)
w.bind("<B1-Motion>",paint)
message=Label(master,text="Press and drag")
message.pack(side=BOTTOM)
mainloop()