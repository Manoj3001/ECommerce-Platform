from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
import runpy
A=Tk()
A.geometry('2000x2000+0+0')
A.title("A-LOTMart")
A.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/A2.jpg"))
my_canvas=Canvas(A,width=2000,height=2000,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")
A.state('zoomed')
def login():
	A.destroy()
	file=runpy.run_path('e-Commerce_login.pyw')
def register():
	A.destroy()
	file1=runpy.run_path('e-commerce_register.pyw')
def join():
	A.destroy()
	file2=runpy.run_path('reckon_transaction.pyw')

log_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/signin.png')
log_btn=Button(A,image=log_img,borderwidth=0,bg="white",command=login)
log_btn_win=my_canvas.create_window(50,560,anchor="nw",window=log_btn)

reg_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/signup3.png')
reg_btn=Button(A,image=reg_img,borderwidth=0,bg="white",command=register)
reg_btn_win=my_canvas.create_window(220,625,anchor="nw",window=reg_btn)

join_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/join.png')
join_btn=Button(A,image=join_img,borderwidth=0,command=join)
join_btn_win=my_canvas.create_window(500,340,anchor="nw",window=join_btn)



A.mainloop()
