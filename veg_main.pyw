from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter.font import Font
import mysql.connector
import runpy




D=Tk()
D.title('A-LOTMart')
D.config(bg='white')
D.geometry('2000x2000+0+0')
D.state('zoomed')
D.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
font1=Font(family="Poppins Semibold",size=15,weight="bold")
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/veg_main.png"))
my_canvas=Canvas(D,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
my_image=my_canvas.create_image(0,0,image=bg,anchor="nw")


def log_out():
	D.destroy()
	runpy.run_path('e-Commerce_main.pyw')
def fruits():
	D.destroy()
	runpy.run_path('Fruits.pyw')
def veg():
	D.destroy()
	runpy.run_path('vegetables.pyw')
def spo():
	D.destroy()
	runpy.run_path('cuts.pyw')
def loc():
	D.destroy()
	runpy.run_path('local.pyw')
def log_out():
	D.destroy()
	runpy.run_path('e-Commerce_main.pyw')
	

#log_out_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/signout.png')
#del_lab=Label(D,text="📍 Delivery at ",bg="#9ce503",fg="black",font=font1)
#del_lab=my_canvas.create_window(400,100,anchor="nw",window=del_lab)

log_out_btn=Button(D,text="HOME",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=log_out)
log_out_btn_win=my_canvas.create_window(1000,60,anchor="nw",window=log_out_btn)



veg_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/ff.png')
veg_btn=Button(D,image=veg_img,borderwidth=0,bg="white",command=fruits)
veg_btn_win=my_canvas.create_window(25,200,anchor="nw",window=veg_btn)
#veg_lbl=Label(D,text="veg",font="helvetica 15 bold italic",bg="white",fg="blue")
#veg_lbl_win=my_canvas.create_window(70,330,anchor="nw",window=veg_lbl)

vege_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/fv.png')
vege_btn=Button(D,image=vege_img,borderwidth=0,bg="white",command=veg)
vege_btn_win=my_canvas.create_window(350,200,anchor="nw",window=vege_btn)


sp_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/fc.png')
sp_btn=Button(D,image=sp_img,borderwidth=0,bg="white",command=spo)
sp_btn_win=my_canvas.create_window(675,200,anchor="nw",window=sp_btn)

lo_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/lo.png')
lo_btn=Button(D,image=lo_img,borderwidth=0,bg="white",command=loc)
lo_btn_win=my_canvas.create_window(1000,200,anchor="nw",window=lo_btn)


D.mainloop()
