from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from PIL import Image,ImageTk
import runpy
from tkinter.font import Font
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

baby=Tk()
baby.geometry('2000x2000+0+0')
baby.title('A-LOTMart - Furniture')
baby.state('zoomed')
baby.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
#bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled2.jpg"))
my_canvas=Canvas(baby,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
#my_canvas.create_image(0,0,image=bg,anchor="nw")
my_canvas.pack(fill='both',expand='true')
font1=Font(family='Poppins-Light',size=8,weight='bold')

def back():
	baby.destroy()
	runpy.run_path('e-Commerce_main.pyw')
back_btn=Button(baby,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 20 italic bold",command=back)
back_btn_win=my_canvas.create_window(1100,500,anchor="nw",window=back_btn)


def add_cin():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Godrej Interio Chocolate King Box, Drawer Bed","Rs.63,353"])
		messagebox.showinfo('A-LOTMart','Godrej Interio Chocolate King Box, Drawer Bed is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Godrej Interio Chocolate King Box, Drawer Bed to cart')
def buy_cin():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		
		print(m.get())
		total_price=(m.get()) * 63353
		print(total_price)
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		

		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bed.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Godrej Interio Chocolate\nKing Box, Drawer Bed ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹63,353",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def add_sha():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["BLUEWUD Amalet Engineered Wood Study Table","Rs.5,361"])
		messagebox.showinfo('A-LOTMart','BLUEWUD Amalet Engineered Wood Study Table is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add BLUEWUD Amalet Engineered Wood Study Table to cart')
def buy_sha():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()

		total_price=(m.get()) * 5361
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)

		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/st.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="BLUEWUD Amalet Engineered \nWood Study Table",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹5,361",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_ha():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Nilkamal Mystique Plastic Outdoor Chair(Set of 2)","Rs.2080"])
		messagebox.showinfo('A-LOTMart','Nilkamal Mystique Plastic Outdoor Chair(Set of 2) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Nilkamal Mystique Plastic Outdoor Chair(Set of 2) to cart')
def buy_ha():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 2080
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chair.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Nilkamal Mystique Plastic \nOutdoor Chair(Set of 2)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2,080",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def buy_pa():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 2835
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/mat.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Starlite Discover by Sleepwell \nFirm Single PU Foam Mattress",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2835",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_pa():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Starlite Discover by Sleepwell Firm Single PU Foam Mattress","Rs.2835"])
		messagebox.showinfo('A-LOTMart','Starlite Discover by Sleepwell Firm Single PU Foam Mattress is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Starlite Discover by Sleepwell Firm Single PU Foam Mattress to cart')

def buy_bru():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 24929
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/dt.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="RoyalOak Milan Italian Glass\n 6 Seater Dining Set",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹24,929",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_bru():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["RoyalOak Milan Italian Glass 6 Seater Dining Set","Rs.24,929"])
		messagebox.showinfo('A-LOTMart','RoyalOak Milan Italian Glass 6 Seater Dining Set is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add RoyalOak Milan Italian Glass 6 Seater Dining Set to cart')

def buy_su():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 14990
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/war.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Perfect Homes Julian Engineered\nWood 4 Door Wardrobe",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹14,990",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_su():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Perfect Homes Julian Engineered Wood 4 Door Wardrobe","Rs.14,990"])
		messagebox.showinfo('A-LOTMart','Perfect Homes Julian Engineered Wood 4 Door Wardrobe is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Perfect Homes Julian Engineered Wood 4 Door Wardrobe to cart')

def buy_no():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 1089
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/ct.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Moonstar Engineered\nWood Coffee Table",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1,089",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_no():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Moonstar Engineered Wood Coffee Table","Rs.1,089"])
		messagebox.showinfo('A-LOTMart','Moonstar Engineered Wood Coffee Table is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Moonstar Engineered Wood Coffee Table to cart')

def buy_ml():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 7921
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/drt.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Godrej Interio Genesys \nEngineered Wood Dressing Table",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹7,921",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_ml():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Godrej Interio Genesys Engineered Wood Dressing Table","Rs.7,921"])
		messagebox.showinfo('A-LOTMart','Godrej Interio Genesys Engineered Wood Dressing Table is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Godrej Interio Genesys Engineered Wood Dressing Table to cart')

def buy_bt():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 28000
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/sofa.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Choice Trade Fabric \nGrey Sofa Set ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹28,000",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_bt():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Choice Trade Fabric 3 + 1 + 1 Grey Sofa Set ","Rs.28,000"])
		messagebox.showinfo('A-LOTMart','Choice Trade Fabric 3 + 1 + 1 Grey Sofa Set  is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Choice Trade Fabric 3 + 1 + 1 Grey Sofa Set  to cart')


def buy_cof():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 573
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/sr.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Cmerchants Metal\nCollapsible Shoe Stand",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹573",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_cof():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Cmerchants Metal Collapsible Shoe Stand","Rs.573"])
		messagebox.showinfo('A-LOTMart','Cmerchants Metal Collapsible Shoe Stand added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Cmerchants Metal Collapsible Shoe Stand to cart')

def buy_oil():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 5163
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/drw.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="FURINNO Engineered Wood \nFree Standing Cabinet",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹5,163",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_oil():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["FURINNO Engineered Wood Free Standing Cabinet","Rs.5,163"])
		messagebox.showinfo('A-LOTMart','FURINNO Engineered Wood Free Standing Cabinet is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add FURINNO Engineered Wood Free Standing Cabinet to cart')

def buy_atta():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 299
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pil.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Kitefly 103 Polyester Fibre\nSolid Sleeping Pillow",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹299",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_atta():
	global grocery_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Kitefly 103 Polyester Fibre Solid Sleeping Pillow","Rs.299"])
		messagebox.showinfo('A-LOTMart','Kitefly 103 Polyester Fibre Solid Sleeping Pillow is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Kitefly 103 Polyester Fibre Solid Sleeping Pillow to cart')

def buy_atta1():
	baby.destroy()
	bill=Tk()
	bill.geometry('2000x2000+0+0')
	bill.title('A-LOTMart')
	bill.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
	def pay():
		def done():
			_add=address.get()
			_em=email.get()
			if(len(_add)==0):
				messagebox.showinfo(title='A-LOTMart',message='Please Enter your address',icon='error')
				return
			if(len(_em)==0):
				messagebox.showinfo(title="A-LOTMart",message="Please Enter your Email Id",icon='error')
				return
			msg='Hello User!\n\n\tYour order is placed successfully \n\t Product will be delivered in a week...\n\tThank You'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=email.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			bill.destroy()
		total_price=(m.get()) * 599
		address=StringVar()
		email=StringVar()
		tot_lab=Label(bill,text="Grand Total:"+str(total_price),bg="white",fg="black",font="helvetica 15 bold italic")
		_tot=my_canvas.create_window(700,20,anchor="nw",window=tot_lab)
		address=StringVar()
		email=StringVar()
		add=Label(bill,text="Address",bg="white",fg="black",font="helvetica 15 bold italic")
		_add=my_canvas.create_window(700,50,anchor="nw",window=add)
		addent=Entry(bill,textvariable=address,width=50,bd=3,font="helvetica 10 bold italic")
		_addent=my_canvas.create_window(800,50,anchor="nw",window=addent)
		Email=Label(bill,text="Email",bg="white",fg="black",font="helvetica 15 bold italic")
		_email=my_canvas.create_window(700,100,anchor="nw",window=Email)
		mailent=Entry(bill,textvariable=email,width=30,bd=3,font="helvetica 10 bold italic")
		_mailent=my_canvas.create_window(800,100,anchor="nw",window=mailent)
		cash_on_del=Button(bill,text="CASH ON DELIVERY",bg="orange",fg="white",font="helvetica 15 bold italic",command=done)
		_cash_on_del=my_canvas.create_window(750,150,anchor="nw",window=cash_on_del)
		def go():
			bill.destroy()
			runpy.run_path('transaction.pyw')
		card=Button(bill,text="CREDIT/DEBIT CARD",bg="orange",fg="white",font="helvetica 15 bold italic",command=go)
		_card=my_canvas.create_window(1000,150,anchor="nw",window=card)
		def back():
			bill.destroy()
			runpy.run_path('furniture.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bean.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Nexis Sundry XXL Tear \nDrop Bean Bag",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹599",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	m=IntVar()
	qty=ttk.Combobox(bill,textvariable=m,width=10)
	qty['values']=('1','2','3','4','5')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_atta1():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["Nexis Sundry XXL Tear Drop Bean Bag","Rs.599"])
		messagebox.showinfo('A-LOTMart','Nexis Sundry XXL Tear Drop Bean Bag is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Nexis Sundry XXL Tear Drop Bean Bag to cart')


m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bed.jpg"))
my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr=Label(baby,text="Godrej Interio Chocolate \nKing Box, Drawer Bed \n₹63,353",font=font1,bg="white",fg="blue")
_xr=my_canvas.create_window(20,3,anchor="nw",window=xr)
xr_btn=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cin)
_xrbtn=my_canvas.create_window(50,180,anchor="nw",window=xr_btn)
purchase_xr=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cin)
_purchase_xr=my_canvas.create_window(50,210,anchor="nw",window=purchase_xr)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/st.jpg"))
my_image=my_canvas.create_image(180,50,image=m2,anchor="nw")
xr1=Label(baby,text="BLUEWUD Amalet \nEngineered Wood Study Table\n₹5,361",font=font1,bg="white",fg="blue")
_xr1=my_canvas.create_window(180,3,anchor="nw",window=xr1)
xr_btn1=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_sha)
_xrbtn1=my_canvas.create_window(200,180,anchor="nw",window=xr_btn1)
purchase_xr1=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_sha)
_purchase_xr1=my_canvas.create_window(200,210,anchor="nw",window=purchase_xr1)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chair.jpg"))
my_image=my_canvas.create_image(350,50,image=m3,anchor="nw")
xr3=Label(baby,text="Nilkamal Mystique \nPlastic Outdoor Chair(Set of 2)\n₹2,080",font=font1,bg="white",fg="blue")
_xr3=my_canvas.create_window(370,3,anchor="nw",window=xr3)
xr_btn3=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ha)
_xrbtn3=my_canvas.create_window(370,180,anchor="nw",window=xr_btn3)
purchase_xr3=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ha)
_purchase_xr3=my_canvas.create_window(370,210,anchor="nw",window=purchase_xr3)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/mat.jpg"))
my_image=my_canvas.create_image(550,50,image=m4,anchor="nw")
xr4=Label(baby,text="Starlite Discover by Sleepwell \nFirm Single PU Foam Mattress\n((L x W: 72 inch x 42 inch)) ₹2,835",font=font1,bg="white",fg="blue")
_xr4=my_canvas.create_window(550,3,anchor="nw",window=xr4)
xr_btn4=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_pa)
_xrbtn4=my_canvas.create_window(550,180,anchor="nw",window=xr_btn4)
purchase_xr4=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_pa)
_purchase_xr4=my_canvas.create_window(550,210,anchor="nw",window=purchase_xr4)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/dt.jpg"))
my_image=my_canvas.create_image(750,50,image=m5,anchor="nw")
xr5=Label(baby,text="RoyalOak Milan Italian Glass\n 6 Seater Dining Set\n ₹24,929",font=font1,bg="white",fg="blue")
_xr5=my_canvas.create_window(750,3,anchor="nw",window=xr5)
xr_btn5=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bru)
_xrbtn5=my_canvas.create_window(750,180,anchor="nw",window=xr_btn5)
purchase_xr5=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bru)
_purchase_xr5=my_canvas.create_window(750,210,anchor="nw",window=purchase_xr5)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/war.jpg"))
my_image=my_canvas.create_image(950,50,image=m6,anchor="nw")
xr6=Label(baby,text="Perfect Homes Julian Engineered \nWood 4 Door Wardrobe \n₹14,990",font=font1,bg="white",fg="blue")
_xr6=my_canvas.create_window(950,3,anchor="nw",window=xr6)
xr_btn6=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_su)
_xrbtn6=my_canvas.create_window(950,180,anchor="nw",window=xr_btn6)
purchase_xr6=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_su)
purchase_xr6=my_canvas.create_window(950,210,anchor="nw",window=purchase_xr6)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/ct.jpg"))
my_image=my_canvas.create_image(25,350,image=m7,anchor="nw")
xr7=Label(baby,text="Moonstar Engineered \nWood Coffee Table ₹1,089",font=font1,bg="white",fg="blue")
_xr7=my_canvas.create_window(25,300,anchor="nw",window=xr7)
xr_btn7=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_no)
_xrbtn7=my_canvas.create_window(25,490,anchor="nw",window=xr_btn7)
purchase_xr7=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_no)
purchase_xr7=my_canvas.create_window(25,520,anchor="nw",window=purchase_xr7)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/drt.jpg"))
my_image=my_canvas.create_image(200,350,image=m8,anchor="nw")
xr8=Label(baby,text="Godrej Interio Genesys \nEngineered Wood Dressing Table\n₹7,921",font=font1,bg="white",fg="blue")
_xr8=my_canvas.create_window(200,300,anchor="nw",window=xr8)
xr_btn8=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ml)
_xrbtn8=my_canvas.create_window(200,490,anchor="nw",window=xr_btn8)
purchase_xr8=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ml)
purchase_xr8=my_canvas.create_window(200,520,anchor="nw",window=purchase_xr8)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/sofa.jpg"))
my_image=my_canvas.create_image(400,350,image=m9,anchor="nw")
xr9=Label(baby,text="Choice Trade Fabric \n3 + 1 + 1 Grey Sofa Set \n₹28,000",font=font1,bg="white",fg="blue")
_xr9=my_canvas.create_window(400,300,anchor="nw",window=xr9)
xr_btn9=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bt)
_xrbtn9=my_canvas.create_window(400,490,anchor="nw",window=xr_btn9)
purchase_xr9=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bt)
purchase_xr9=my_canvas.create_window(400,520,anchor="nw",window=purchase_xr9)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/sr.jpg"))
my_image=my_canvas.create_image(1150,50,image=m10,anchor="nw")
xr10=Label(baby,text="Cmerchants Metal \nCollapsible Shoe Stand \n₹573",font=font1,bg="white",fg="blue")
_xr10=my_canvas.create_window(1150,3,anchor="nw",window=xr10)
xr_btn10=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cof)
_xrbtn10=my_canvas.create_window(1150,180,anchor="nw",window=xr_btn10)
purchase_xr10=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cof)
purchase_xr10=my_canvas.create_window(1150,210,anchor="nw",window=purchase_xr10)

m11=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/drw.jpg"))
my_image=my_canvas.create_image(750,350,image=m11,anchor="nw")
xr11=Label(baby,text="FURINNO Engineered Wood \nFree Standing Cabinet \n₹5,163",font=font1,bg="white",fg="blue")
_xr11=my_canvas.create_window(750,300,anchor="nw",window=xr11)
xr_btn11=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_oil)
_xrbtn11=my_canvas.create_window(750,490,anchor="nw",window=xr_btn11)
purchase_xr11=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_oil)
purchase_xr11=my_canvas.create_window(750,520,anchor="nw",window=purchase_xr11)

m12=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pil.jpg"))
my_image=my_canvas.create_image(950,350,image=m12,anchor="nw")
xr12=Label(baby,text="Kitefly 103 Polyester Fibre \nSolid Sleeping Pillow Pack \nof 3 ₹299",font=font1,bg="white",fg="blue")
_xr12=my_canvas.create_window(950,300,anchor="nw",window=xr12)
xr_btn12=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta)
_xrbtn12=my_canvas.create_window(950,490,anchor="nw",window=xr_btn12)
purchase_xr12=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta)
purchase_xr12=my_canvas.create_window(950,520,anchor="nw",window=purchase_xr12)

m13=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bean.jpg"))
my_image=my_canvas.create_image(570,350,image=m13,anchor="nw")
xr13=Label(baby,text="Nexis Sundry XXL Tear \nDrop Bean Bag\n₹599",font=font1,bg="white",fg="blue")
_xr13=my_canvas.create_window(570,300,anchor="nw",window=xr13)
xr_btn13=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta1)
_xrbtn13=my_canvas.create_window(570,490,anchor="nw",window=xr_btn13)
purchase_xr13=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta1)
purchase_xr13=my_canvas.create_window(570,520,anchor="nw",window=purchase_xr13)

baby_list=[]
baby.mainloop()