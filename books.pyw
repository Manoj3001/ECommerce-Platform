from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from PIL import Image,ImageTk
import runpy
from tkinter.font import Font
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

books=Tk()
books.geometry('2000x2000+0+0')
books.title('A-LOTMart - Books')
books.state('zoomed')
books.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
my_canvas=Canvas(books,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
font1=Font(family='Poppins-Light',size=8,weight='bold')
def back():
	books.destroy()
	runpy.run_path('e-Commerce_main.pyw')
back_btn=Button(books,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 20 italic bold",command=back)
back_btn_win=my_canvas.create_window(1200,500,anchor="nw",window=back_btn)

def add_cin():
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Attitude Is Everything:Change Your Attitude","Rs.160"])
		messagebox.showinfo('A-LOTMart','Attitude Is Everything:Change Your Attitude is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Attitude Is Everything:Change Your Attitude to cart')
def buy_cin():
	books.destroy()
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
		total_price=(m.get()) * 160
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b1.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Attitude Is Everything:\nChange Your Attitude",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹160",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["One Arranged Murder","Rs.145"])
		messagebox.showinfo('A-LOTMart','One Arranged Murder  is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add One Arranged Murder  to cart')
def buy_sha():
	books.destroy()
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

		total_price=(m.get()) * 145
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
		def back():
			bill.destroy()
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b2.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="One Arranged Murder ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹145",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Believe ","Rs.235"])
		messagebox.showinfo('A-LOTMart','Believe  is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Believe to cart')
def buy_ha():
	books.destroy()
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
		total_price=(m.get()) * 235
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b3.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Believe",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹235",bg="white",fg="black",font="helvetica 15 bold italic")
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
	books.destroy()
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
		total_price=(m.get()) * 200
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b4.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Steve Jobs",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹200",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Steve Jobs","Rs.200"])
		messagebox.showinfo('A-LOTMart','Steve Jobs is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Steve Jobs to cart')

def buy_bru():
	books.destroy()
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
		total_price=(m.get()) * 699
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b5.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Ponniyin Selvan",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹699",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Ponniyin Selvan","Rs.699"])
		messagebox.showinfo('A-LOTMart','Ponniyin Selvan is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Ponniyin Selvan to cart')

def buy_su():
	books.destroy()
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b6.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="The Psychology of Money",bg="white",fg="black",font="helvetica 15 bold italic")
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
def add_su():
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["The Psychology of Money","Rs.299"])
		messagebox.showinfo('A-LOTMart','The Psychology of Money is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add The Psychology of Money to cart')

def buy_no():
	books.destroy()
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
		total_price=(m.get()) * 385
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b7.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Oxford Student Atlas",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹385",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Oxford Student Atlas","Rs.385"])
		messagebox.showinfo('A-LOTMart','Oxford Student Atlas is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Oxford Student Atlas to cart')

def buy_ml():
	books.destroy()
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
		total_price=(m.get()) * 152
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b8.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Oxford English Mini Dictionary ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹152",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Oxford English Mini Dictionary","Rs.152"])
		messagebox.showinfo('A-LOTMart','Oxford English Mini Dictionary is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Oxford English Mini Dictionary to cart')

def buy_bt():
	books.destroy()
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
		total_price=(m.get()) * 239
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b9.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Valmiki's Ramayana",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹239",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Valmiki's Ramayana","Rs.239"])
		messagebox.showinfo('A-LOTMart',"Valmiki's Ramayana is successfully added to cart")
		return
	else:
		messagebox.showinfo('A-LOTMart',"Failed to add Valmiki's Ramayana to cart")


def buy_cof():
	books.destroy()
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
		total_price=(m.get()) * 385
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b10.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Mahabharata",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹385",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["Mahabharata","Rs.385"])
		messagebox.showinfo('A-LOTMart','Mahabharata is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Mahabharata to cart')

def buy_oil():
	books.destroy()
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
		total_price=(m.get()) * 180
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b11.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="The Holy Quran",bg="white",fg="black",font="helvetica 15 bold ")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹180",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["The Holy Quran","Rs.180"])
		messagebox.showinfo('A-LOTMart','The Holy Quran is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add The Holy Quran to cart')

def buy_atta():
	books.destroy()
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
		total_price=(m.get()) * 435
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b13.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="War and Peace",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹435",bg="white",fg="black",font="helvetica 15 bold italic")
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
		books_list.append(["War and Peace","Rs.435"])
		messagebox.showinfo('A-LOTMart','War and Peace is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add War and Peace  to cart')

def buy_atta1():
	books.destroy()
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
		total_price=(m.get()) * 399
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
			runpy.run_path('books.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/payment.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b12.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="The Holy Bible",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹399",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global books_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		books_list.append(["The Holy Bible","Rs.399"])
		messagebox.showinfo('A-LOTMart','The Holy Bible is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add The Holy Bible to cart')


m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b1.jpg"))
my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr=Label(books,text="Attitude Is Everything: \nChange Your Attitude\n₹160",font=font1,bg="white",fg="blue")
_xr=my_canvas.create_window(25,3,anchor="nw",window=xr)
xr_btn=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cin)
_xrbtn=my_canvas.create_window(25,180,anchor="nw",window=xr_btn)
purchase_xr=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cin)
_purchase_xr=my_canvas.create_window(25,210,anchor="nw",window=purchase_xr)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b2.jpg"))
my_image=my_canvas.create_image(180,50,image=m2,anchor="nw")
xr1=Label(books,text="One Arranged Murder (English)\n₹145",font=font1,bg="white",fg="blue")
_xr1=my_canvas.create_window(180,3,anchor="nw",window=xr1)
xr_btn1=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_sha)
_xrbtn1=my_canvas.create_window(200,180,anchor="nw",window=xr_btn1)
purchase_xr1=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_sha)
_purchase_xr1=my_canvas.create_window(200,210,anchor="nw",window=purchase_xr1)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b3.jpg"))
my_image=my_canvas.create_image(350,50,image=m3,anchor="nw")
xr3=Label(books,text="Believe (English)\n₹235",font=font1,bg="white",fg="blue")
_xr3=my_canvas.create_window(370,3,anchor="nw",window=xr3)
xr_btn3=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ha)
_xrbtn3=my_canvas.create_window(370,180,anchor="nw",window=xr_btn3)
purchase_xr3=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ha)
_purchase_xr3=my_canvas.create_window(370,210,anchor="nw",window=purchase_xr3)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b4.jpg"))
my_image=my_canvas.create_image(550,50,image=m4,anchor="nw")
xr4=Label(books,text="Steve Jobs (English)\n ₹200",font=font1,bg="white",fg="blue")
_xr4=my_canvas.create_window(550,3,anchor="nw",window=xr4)
xr_btn4=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_pa)
_xrbtn4=my_canvas.create_window(550,180,anchor="nw",window=xr_btn4)
purchase_xr4=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_pa)
_purchase_xr4=my_canvas.create_window(550,210,anchor="nw",window=purchase_xr4)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b5.jpg"))
my_image=my_canvas.create_image(750,50,image=m5,anchor="nw")
xr5=Label(books,text="Ponniyin Selvan (Tamil)\n ₹699",font=font1,bg="white",fg="blue")
_xr5=my_canvas.create_window(750,3,anchor="nw",window=xr5)
xr_btn5=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bru)
_xrbtn5=my_canvas.create_window(750,180,anchor="nw",window=xr_btn5)
purchase_xr5=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bru)
_purchase_xr5=my_canvas.create_window(750,210,anchor="nw",window=purchase_xr5)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b6.jpg"))
my_image=my_canvas.create_image(950,50,image=m6,anchor="nw")
xr6=Label(books,text="The Psychology of Money \n(English)₹299",font=font1,bg="white",fg="blue")
_xr6=my_canvas.create_window(950,3,anchor="nw",window=xr6)
xr_btn6=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_su)
_xrbtn6=my_canvas.create_window(950,180,anchor="nw",window=xr_btn6)
purchase_xr6=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_su)
purchase_xr6=my_canvas.create_window(950,210,anchor="nw",window=purchase_xr6)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b7.jpg"))
my_image=my_canvas.create_image(25,350,image=m7,anchor="nw")
xr7=Label(books,text="Oxford Student Atlas\n ₹239",font=font1,bg="white",fg="blue")
_xr7=my_canvas.create_window(25,300,anchor="nw",window=xr7)
xr_btn7=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_no)
_xrbtn7=my_canvas.create_window(25,490,anchor="nw",window=xr_btn7)
purchase_xr7=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_no)
purchase_xr7=my_canvas.create_window(25,520,anchor="nw",window=purchase_xr7)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b8.jpg"))
my_image=my_canvas.create_image(200,350,image=m8,anchor="nw")
xr8=Label(books,text="Oxford English Mini \nDictionary ₹152",font=font1,bg="white",fg="blue")
_xr8=my_canvas.create_window(200,300,anchor="nw",window=xr8)
xr_btn8=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ml)
_xrbtn8=my_canvas.create_window(200,490,anchor="nw",window=xr_btn8)
purchase_xr8=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ml)
purchase_xr8=my_canvas.create_window(200,520,anchor="nw",window=purchase_xr8)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b9.jpg"))
my_image=my_canvas.create_image(380,350,image=m9,anchor="nw")
xr9=Label(books,text="Valmiki's Ramayana\n(English)\n₹239",font=font1,bg="white",fg="blue")
_xr9=my_canvas.create_window(380,300,anchor="nw",window=xr9)
xr_btn9=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bt)
_xrbtn9=my_canvas.create_window(380,490,anchor="nw",window=xr_btn9)
purchase_xr9=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bt)
purchase_xr9=my_canvas.create_window(380,520,anchor="nw",window=purchase_xr9)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b10.jpg"))
my_image=my_canvas.create_image(1150,50,image=m10,anchor="nw")
xr10=Label(books,text="Mahabharata (English)\n ₹385",font=font1,bg="white",fg="blue")
_xr10=my_canvas.create_window(1150,3,anchor="nw",window=xr10)
xr_btn10=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cof)
_xrbtn10=my_canvas.create_window(1150,180,anchor="nw",window=xr_btn10)
purchase_xr10=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cof)
purchase_xr10=my_canvas.create_window(1150,210,anchor="nw",window=purchase_xr10)

m11=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b11.jpg"))
my_image=my_canvas.create_image(750,350,image=m11,anchor="nw")
xr11=Label(books,text="The Holy Quran\n(English)\n ₹180",font=font1,bg="white",fg="blue")
_xr11=my_canvas.create_window(750,300,anchor="nw",window=xr11)
xr_btn11=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_oil)
_xrbtn11=my_canvas.create_window(750,490,anchor="nw",window=xr_btn11)
purchase_xr11=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_oil)
purchase_xr11=my_canvas.create_window(750,520,anchor="nw",window=purchase_xr11)

m12=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b13.jpg"))
my_image=my_canvas.create_image(950,350,image=m12,anchor="nw")
xr12=Label(books,text="War and Peace\n₹435",font=font1,bg="white",fg="blue")
_xr12=my_canvas.create_window(950,300,anchor="nw",window=xr12)
xr_btn12=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta)
_xrbtn12=my_canvas.create_window(950,490,anchor="nw",window=xr_btn12)
purchase_xr12=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta)
purchase_xr12=my_canvas.create_window(950,520,anchor="nw",window=purchase_xr12)

m13=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/b12.jpg"))
my_image=my_canvas.create_image(550,350,image=m13,anchor="nw")
xr13=Label(books,text="The Holy Bible \n (English) \n₹399",font=font1,bg="white",fg="blue")
_xr13=my_canvas.create_window(570,300,anchor="nw",window=xr13)
xr_btn13=Button(books,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta1)
_xrbtn13=my_canvas.create_window(550,490,anchor="nw",window=xr_btn13)
purchase_xr13=Button(books,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta1)
purchase_xr13=my_canvas.create_window(550,520,anchor="nw",window=purchase_xr13)

books_list=[]
books.mainloop()