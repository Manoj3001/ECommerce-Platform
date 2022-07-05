from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import smtplib
import random
import runpy
T=Tk()
T.geometry('2000x2000+0+0')
T.title('Reckon - Subscription')
T.iconbitmap(r'C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/reckon.ico')
T.state('zoomed')
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/trans_page.jpg"))
my_canvas=Canvas(T,width=2000,height=2000,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")
def pay():
	sub_btn.destroy()
	lbl0=Label(T,text="Email-Id",bg="black",fg="deep pink",font="helvetica 15 bold")
	_lbl0=my_canvas.create_window(1000,350,anchor="nw",window=lbl0)
	em=StringVar()
	ent0=Entry(T,textvariable=em,width=20,font="helvetica 15 bold")
	_ent0=my_canvas.create_window(1100,350,anchor="nw",window=ent0)
	lbl1=Label(T,text="Card Number",bg="black",fg="deep pink",font="helvetica 15 bold")
	_lbl1=my_canvas.create_window(600,350,anchor="nw",window=lbl1)
	cd=StringVar()
	ent1=Entry(T,textvariable=cd,width=20,font="helvetica 15 bold")
	_ent1=my_canvas.create_window(750,350,anchor="nw",window=ent1)
	lbl2=Label(T,text="Expiry Year",bg="black",fg="deep pink",font="helvetica 15 bold")
	_lbl2=my_canvas.create_window(600,400,anchor="nw",window=lbl2)
	ey=StringVar()
	ent2=Entry(T,textvariable=ey,width=10,font="helvetica 15 bold")
	_ent2=my_canvas.create_window(750,400,anchor="nw",window=ent2)
	def otp():
		_cd=cd.get()
		_ey=ey.get()
		_em=em.get()
		if((len(_cd) and len(_ey) and len(_em))==0):
			messagebox.showerror("Reckon","Please Enter your Card Number,Email-Id  and expiry year")
			return
		if(len(_cd)<12):
			messagebox.showerror("Reckon","please enter your Correct card number")
			return
		msg='Hello User!\n\n\tYour Have Successfully Subcribed to Reckon \n\t Enjoy your movies\n\tThank You'
		sender_email="almalotmart@gmail.com"
		sender_password="commerce2021"
		server=smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(sender_email,sender_password)
		print('done')
		_em=em.get()
		server.sendmail(sender_email,_em,msg)
		print("sent")
		mg=messagebox.showinfo("ALM-Reckon","You have successfully subscribed for ALM-Reckon")
		if(mg=='ok'):
			T.destroy()
			runpy.run_path('reckon.pyw')

	otp_btn=Button(T,text="Pay",width=10,bg="green",fg="white",font="helvetiac 15 bold",command=otp)
	_otp_btn=my_canvas.create_window(900,450,anchor="nw",window=otp_btn)


sub_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/sub.png')
sub_btn=Button(T,image=sub_img,borderwidth=0,bg="white",command=pay)
sub_btn_win=my_canvas.create_window(65,490,anchor="nw",window=sub_btn)
T.mainloop()