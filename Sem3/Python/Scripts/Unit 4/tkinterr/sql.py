from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class fileeditor:
	def __init__(self):
		window=Tk()
		menubar=Menu(window)
		window.config(menu=menubar)
		operationmenu=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="file",menu=operationmenu)
		operationmenu.add_command(label="open",command=self.openfile)
		operationmenu.add_command(label="save",command=self.savefile)
		operationmenu.add_command(label="exit",command=window.destroy)
		frame1=Frame(window)
		frame1.grid(row=1,column=1)
		scrollbar=Scrollbar(frame1)
		scrollbar.pack(side=RIGHT,fill=Y)
		self.text=Text(frame1,width=40,height=20,wrap=WORD,yscrollcommand=scrollbar.set)
		self.text.pack()
		scrollbar.config(command=self.text.yview)
		window.mainloop()
	def openfile(self):
		filename=askopenfilename()
		infile=open(filename,"r")
		self.text.insert(END,infile.read())
		infile.close()
	def savefile(self):
		filenamew=asksaveasfilename()
		outfile=open(filenamew,"w")
		outfile.write(self.text.get(1.0,END))
		outfile.close()

fileeditor()
