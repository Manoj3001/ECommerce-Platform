from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import Font
import openpyxl
from xlrd import open_workbook
import os
import runpy
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)
B=Tk()
B.title("A-LOTMart - Login")
B.iconbitmap(B,r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
B.geometry('2000x2000+0+0')
B.state('zoomed')
#B.config(bg="white")
userid=StringVar()
pwd=StringVar()
font1=Font(family="Poppins-Semibold",size=25)
font2=Font(family="Poppins-Semibold",size=15)
#font3=Font(family="Poppins regular",size=15)
def login():
	loc=os.path.join('details','C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/login_details.xlsx')
	wb=open_workbook(loc)
	sheet1=wb.sheet_by_index(0)
	_userid=userid.get()
	_pwd=pwd.get()
	if((len(_userid) and len(_pwd))==0):
		messagebox.showerror('A-LOTMart','Please Enter your E-Mail Id and Password')
	else:
		for i in range(10000):
			try:
				user_id=sheet1.cell_value(i,0)
			except:
				continue
			password=sheet1.cell_value(i,1)
			if(user_id==_userid):
				if(password==_pwd):
					
					B.destroy()
					file2=runpy.run_path('e-Commerce_main.pyw')

					break
				else:
					messagebox.showerror('A-LOTMart','Please Enter the Correct Password')
					break
		else:
			messagebox.showerror('A-LOTMart','Please Enter the Correct E-mail Id')



	
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/login.jpg"))
my_canvas=Canvas(B,width=200,height=200,bd=0,highlightthickness=0)
my_canvas.pack(fill='both',expand='true')
my_image=my_canvas.create_image(0,0,image=bg,anchor="nw")

title_label=Label(B,text="Login ?",font=font1,bg="black",fg="White")

_title=my_canvas.create_window(620,75,anchor="nw",window=title_label)

log_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/login.png')
log_btn=Button(B,image=log_img,borderwidth=0,bg="black",command=login)

User_label=Label(B,text="Mail id:",font=font2,fg="white",bg="black")
User_label_win=my_canvas.create_window(500,200,anchor="nw",window=User_label)

#user_note=Label(B,text="")

User_entry=Entry(B,textvariable=userid,font=font2,bd=0,fg="black",width=20)
User_entry_win=my_canvas.create_window(600,200,anchor="nw",window=User_entry)

pwd_label=Label(B,text="Password:",font=font2,fg="white",bg="black")
pwd_label_win=my_canvas.create_window(500,300,anchor="nw",window=pwd_label)

pwd_entry=Entry(B,textvariable=pwd,font=font2,show="●",bd=0,fg="black",width=20)
pwd_entry_win=my_canvas.create_window(600,300,anchor="nw",window=pwd_entry)


login_btn_win=my_canvas.create_window(495,400,anchor="nw",window=log_btn)


B.mainloop()
