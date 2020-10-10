from tkinter import*

# root=Tk()
# root.title('Gui')
# root.geometry('800x600')
# root.mainloop()

# root=Tk()
# c=Canvas(root,bg='blue',height=600,width=900,cursor='pencil')
# id=c.create_line(50,50,100,500,fill='yellow',activefill='lightblue')
# id=c.create_oval(100,100,300,500,fill='green',activefill='lightblue')
# id=c.create_arc(100,100,300,500,start=30,extent=90,style='arc')
# c.pack()
# mainloop()

def pyt():
	print("Hello Python")
def java():
	print("Hello Java")


window=Tk()
l=Label(window,text="python")
b1=Button(window,text="click1",command=pyt)
b2=Button(window,text="click2",command=java)
l.pack()
b1.pack()
b2.pack()
window.mainloop()