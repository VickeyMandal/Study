from tkinter import *
# class mouse_key_event:

# 	def __init__(self):
# 		window=Tk()
# 		canvas=Canvas(window,width=200,height=100)
# 		canvas.pack()
# 		canvas.bind('<Button-1>',self.process_mouse_event)
# 		canvas.bind('<Key>',self.process_key_event)
# 		canvas.focus_set()
# 		window.mainloop()
# 	def process_mouse_event(self,event):
# 		print("clicked at",event.x,event.y)
# 		print("position in screen",event.x_root,event.y_root)
# 		print("Which button is clicked",event.num)
# 	def process_key_event(self,event):
# 		print("keysym",event.keysym)
# 		print("keycode",event.keycode)
# mouse_key_event()


# class my_button:
# 	def __init__(self,root):
# 		self.f=Frame(root,height=350,width=500)
# 		self.f.propagate(0)
# 		self.f.pack()
# 		self.l1=Label(text="User Name")
# 		self.l2=Label(text="Password")
# 		self.e1=Entry(self.f,width=25,font=('Arial',14))
# 		self.e2=Entry(self.f,width=25,show='*')
# 		self.e1.bind('<Return>',self.display)
# 		self.e2.bind('<Return>',self.display)
# 		self.l1.place(x=50,y=100)
# 		self.l2.place(x=50,y=150)
# 		self.e1.place(x=200,y=100)
# 		self.e2.place(x=200,y=150)
# 	def display(self,event):
# 		str1=self.e1.get()
# 		str2=self.e2.get()
# 		lb1=Label(text="Your us: "+str1).place(x=50,y=200)
# 		lb1=Label(text="Your pass: "+str2).place(x=50,y=220)

# root=Tk()
# mb=my_button(root)
# root.mainloop()



# class my_button:
# 	def __init__(self,root):
# 		self.f=Frame(root,height=350,width=500)
# 		self.f.propagate(0)
# 		self.f.pack()
# 		self.val1=IntVar()
# 		self.val2=StringVar()
# 		self.s1=Spinbox(self.f,from_=5,to=15,textvariable=self.val1)
# 		self.s2=Spinbox(self.f,values=('Kolkata','Delhi','Punjab'),textvariable=self.val2)
# 		self.b=Button(self.f,text="get values from spinbox",command=self.display)
# 		self.s1.place(x=50,y=50)
# 		self.s2.place(x=50,y=100)
# 		self.b.place(x=50,y=150)
# 	def display(self):
# 		a=self.val1.get()
# 		b=self.val2.get()
# 		lb1=Label(text="Selected value: "+str(a)).place(x=50,y=200)
# 		lb2=Label(text="Selcted city: "+s).place(x=50,y=220)

# root=Tk()
# mb=my_button(root)
# root.mainloop()




# class my_button:
# 	def __init__(self,root):
# 		self.f=Frame(root,height=350,width=500)
# 		self.f.propagate(0)
# 		self.f.pack()
# 		self.lb1=Label(self.f,text="Select University")
# 		self.lb1.place(x=50,y=50)
# 		self.lb=Listbox(self.f,activestyle='underline',selectmode='Multiple')
# 		self.lb.place(x=50,y=100)
# 		for i in ['Oxford','Texas','Cambridge']:
# 			self.lb.insert(END,i)
# 		self.lb.bind('<<ListboxSelect>>',self.on_select)
# 		self.t=Text(self.f,width=40,height=6,wrap=WORD)
# 		self.t.place(x=300,y=100)
# 	def on_select(self,event):
# 		self.lst=[]
# 		indexes=self.lb.curselection()
# 		for i in indexes:
# 			self.lst.append(self.lb.get(i))
# 		self.t.delete(0.0,END)
# 		self.t.insert(0.0,self.lst)

# root=Tk()
# mb=my_button(root)
# root.mainloop()



# class my_menu:
# 	def __init__(self,root):
# 		self.menubar=Menu(root)
# 		root.config(menu=self.menubar)
# 		self.filemenu=Menu(root,tearoff=0)
# 		self.filemenu.add_command(label='New',command=self.dosome)
# 		self.filemenu.add_command(label='Open',command=self.dosome)
# 		self.filemenu.add_command(label='Save',command=self.dosome)
# 		self.filemenu.add_separator()
# 		self.filemenu.add_command(label='Exit',command=root.destroy)
# 		self.menubar.add_cascade(label='File',menu=self.filemenu)
# 	def dosome(self):
# 		pass
# root=Tk()
# mb=my_menu(root)
# root.geometry('600x350')
# root.mainloop()




# class my_button:
# 	def __init__(self,root):
# 		self.t=Text(root,width=70,height=15,wrap=NONE)
# 		for i in range(50):
# 			self.t.insert(END,'This is bla bla')
# 		self.t.pack()
# 		self.h=Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)
# 		self.t.config(xscrollcommand=self.h.set)
# 		self.h.pack(side=BOTTOM,fill=X)


# root=Tk()
# mb=my_button(root)
# root.mainloop()




# root=Tk()
# s=Scrollbar(root)
# s.pack(side='RIGHT',fill=Y)
# m=Listbox(root,yscrollcommand=s.set)
# for line in range(70):
# 	m.insert(END,"This is python"+str(line))
# m.pack(side=left)


