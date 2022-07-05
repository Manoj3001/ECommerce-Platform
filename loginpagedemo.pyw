from tkinter import *
from tkinter import messagebox
l=Tk()
e1=StringVar()
e2=StringVar()
def login():
	pass
a=Label(l,text="username").pack()
b=Label(l,text="password").pack()
a1=Entry(l,textvariable=e1).pack()
b1=Entry(l,textvariable=e2).pack()
btn=Button(l,text="submit",command=login).pack()
l.mainloop()