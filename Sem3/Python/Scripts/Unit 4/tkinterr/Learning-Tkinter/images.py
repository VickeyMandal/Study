from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Hello")
root.iconbitmap("r.ico")


my_image = ImageTk.PhotoImage(Image.open("rupees.png"))
label=Label(image=my_image)

label.pack()













button_exit=Button(root,text="Exit",command=root.quit)
button_exit.pack()
root.mainloop()
