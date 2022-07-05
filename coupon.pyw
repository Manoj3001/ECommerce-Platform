from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import Font
from tkinter import ttk
import smtplib
import runpy
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

mobile=Tk()
mobile.geometry('2000x2000+0+0')
mobile.title('A-LOTMart - Offers For You')
mobile.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
mobile.state('zoomed')

font1=Font(family='Poppins-Light',size=8,weight='bold')
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/coupon.png"))
my_canvas=Canvas(mobile,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
my_canvas.create_image(0,0,image=bg,anchor="nw")
def back():
	mobile.destroy()
	runpy.run_path('e-Commerce_main.pyw')
back_btn=Button(mobile,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 20 italic bold",command=back)
back_btn_win=my_canvas.create_window(1250,500,anchor="nw",window=back_btn)

'''
def buy_xr():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["APPLE iPhone XR","Rs.46,999"])
		messagebox.showinfo('A-LOTMart','APPLE iPhone XR is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add APPLE iPhone XR to cart')

def buy_promax():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["REDMI Note 10 Pro Max","Rs.23,195"])
		messagebox.showinfo('A-LOTMart','REDMI Note 10 Pro Max is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add REDMI Note 10 Pro Max to cart')

def buy_A12():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["SAMSUNG Galaxy A12","Rs.12,999"])
		messagebox.showinfo('A-LOTMart','SAMSUNG Galaxy A12 is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add SAMSUNG Galaxy A12 to cart')
def buy_x3():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["POCO X3 Pro","Rs.20,999"])
		messagebox.showinfo('A-LOTMart','POCO X3 Pro is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add POCO X3 Pro to cart')
def buy_f19():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["OPPO F19 Pro","Rs.23,490"])
		messagebox.showinfo('A-LOTMart','OPPO F19 Pro is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add OPPO F19 Pro to cart')
def buy_v20():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["ViVO V20","Rs.24,490"])
		messagebox.showinfo('A-LOTMart','ViVO V20 is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add ViVO V20 to cart')
def buy_c21():
	global mobile_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		mobile_list.append(["realme C21","Rs.7,999"])
		messagebox.showinfo('A-LOTMart','realme C21 is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add realme C21 to cart')
'''
def purchasexr():
	mobile.destroy()
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
		total_price=(m.get()) * 700
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chudi1.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Hindustan Designs Chudihar",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹700",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)


	bill.mainloop()

def purchaseA21():
	mobile.destroy()
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
		total_price=(m.get()) * 1949
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/wjeans.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Levi's Womens Skinny Jeans",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1,949",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()


def purchasef19():
	mobile.destroy()
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
		total_price=(m.get()) * 1490
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/jeans.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Levi's Men Skinny Jeans",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1,490",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)
	s.current(0)
	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def purchasex3():
	mobile.destroy()
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
		total_price=(m.get()) * 299
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/tops.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Clothzy Womens Tops",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹299",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def purchasev20():
	mobile.destroy()
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
		total_price=(m.get()) * 490
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/t shirt1.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Levi's Mens T Shirt",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹490",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def purchasec21():
	mobile.destroy()
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
		total_price=(m.get()) * 1999
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/uni1.png"))
	my_image=my_canvas.create_image(10,60,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Wrangler Combo Casual\n Full Sleeve ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1,999",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(210,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(260,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def purchasenote10():
	mobile.destroy()
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
		total_price=(m.get()) * 2999
		print(total_price)
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
			runpy.run_path('coupon.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	
	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/blazer.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="ARROW Mens Blazer",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2,999",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(0)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()


font2=Font(family="Poppins SemiBold",size=10)
m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chudi1.jpg"))
my_image=my_canvas.create_image(25,60,image=m1,anchor="nw")
xr=Label(mobile,text="Hindustan Designs\n₹700",font=font1,bg="white",fg="blue")
_xr=my_canvas.create_window(50,3,anchor="nw",window=xr)
xr_btn=Label(mobile,text="Save ₹300",bg="white",fg="red",font=font2)
_xrbtn=my_canvas.create_window(50,380,anchor="nw",window=xr_btn)
purchase_xr=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasexr)
_purchase_xr=my_canvas.create_window(50,410,anchor="nw",window=purchase_xr)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/blazer.jpg"))
my_image=my_canvas.create_image(220,50,image=m2,anchor="nw")
note=Label(mobile,text="ARROW Regular fit\n mens Blazer\n₹2,999",font=font1,bg="white",fg="blue")
_note=my_canvas.create_window(220,3,anchor="nw",window=note)
note_btn=Label(mobile,text="Save ₹4000",bg="white",fg="red",font=font2)
_notebtn=my_canvas.create_window(220,380,anchor="nw",window=note_btn)
purchase_note=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasenote10)
_purchase_note=my_canvas.create_window(220,410,anchor="nw",window=purchase_note)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/wjeans.jpg"))
my_image=my_canvas.create_image(390,60,image=m4,anchor="nw")
sam=Label(mobile,text="Levi's Womens Skinny Jeans\n₹1,949",font=font1,bg="white",fg="blue")
_sam=my_canvas.create_window(390,3,anchor="nw",window=sam)
sam_btn=Label(mobile,text="Save ₹1000",fg="red",bg="white",font=font2)
_notesam=my_canvas.create_window(390,380,anchor="nw",window=sam_btn)
purchase_A12=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchaseA21)
_purchase_xr=my_canvas.create_window(390,410,anchor="nw",window=purchase_A12)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/jeans.jpg"))
my_image=my_canvas.create_image(560,60,image=m5,anchor="nw")
oppo=Label(mobile,text="Levi's Men Skinny Jeans\n₹1,490",font=font1,bg="white",fg="blue")
_oppo=my_canvas.create_window(560,3,anchor="nw",window=oppo)
oppo_btn=Label(mobile,text="Save ₹500",fg="red",bg="white",font=font2)
_opposam=my_canvas.create_window(560,380,anchor="nw",window=oppo_btn)
purchase_f19=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasef19)
_purchase_f19=my_canvas.create_window(560,410,anchor="nw",window=purchase_f19)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/tops.jpg"))
my_image=my_canvas.create_image(730,50,image=m6,anchor="nw")
x3=Label(mobile,text="Clothzy Womens Tops\n₹299",font=font1,bg="white",fg="blue")
_x3=my_canvas.create_window(730,3,anchor="nw",window=x3)
x3_btn=Label(mobile,text="Save ₹800",fg="red",bg="white",font=font2)
_x3sam=my_canvas.create_window(730,380,anchor="nw",window=x3_btn)
purchase_x3=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasex3)
_purchase_x3=my_canvas.create_window(730,410,anchor="nw",window=purchase_x3)


m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/t shirt1.jpg"))
my_image=my_canvas.create_image(900,50,image=m7,anchor="nw")
v20=Label(mobile,text="Levi's Mens T Shirt\n₹490",font=font1,bg="white",fg="blue")
_v20=my_canvas.create_window(900,3,anchor="nw",window=v20)
v20_btn=Label(mobile,text="Save ₹525",fg="red",bg="white",font=font2)
_v20sam=my_canvas.create_window(900,380,anchor="nw",window=v20_btn)
purchase_v20=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasev20)
_purchase_v20=my_canvas.create_window(900,410,anchor="nw",window=purchase_v20)


m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/uni1.png"))
my_image=my_canvas.create_image(1080,70,image=m8,anchor="nw")
c21=Label(mobile,text="Wrangler Combo Casual \nFull Sleeve (3pcs)\n₹1,999",font=font1,bg="white",fg="blue")
_c21=my_canvas.create_window(1100,3,anchor="nw",window=c21)
c21_btn=Label(mobile,text="Save ₹1000",bg="white",fg="red",font=font2)
_c21sam=my_canvas.create_window(1150,380,anchor="nw",window=c21_btn)
purchase_c21=Button(mobile,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=purchasec21)
_purchase_c21=my_canvas.create_window(1150,410,anchor="nw",window=purchase_c21)


mobile_list=[]

mobile.mainloop()

