from tkinter import *

root = Tk()
#creating a label
label1=Label(root, text="Hello Tkinter").grid(row=0,column=0)
label2=Label(root, text="Hello!").grid(row=0,column=2)
label3=Label(root, text="        ").grid(row=0,column=1)

# label1.grid(row=0,column=0)
# label2.grid(row=0,column=2)
# label3.grid(row=0,column=1)

root.mainloop()