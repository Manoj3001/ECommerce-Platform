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
baby.title('A-LOTMart - Baby and Toys')
baby.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
baby.state('zoomed')
my_canvas=Canvas(baby,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
font1=Font(family='Poppins-Light',size=8,weight='bold')
def back():
	baby.destroy()
	runpy.run_path('e-Commerce_main.pyw')
back_btn=Button(baby,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 20 italic bold",command=back)
back_btn_win=my_canvas.create_window(1100,600,anchor="nw",window=back_btn)

def add_cin():
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["HIMALAYA GENTLE BABY SHAMPOO(400 ml)","Rs.225"])
		messagebox.showinfo('A-LOTMart','HIMALAYA GENTLE BABY SHAMPOO is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add HIMALAYA GENTLE BABY SHAMPOO to cart')
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
		total_price=(m.get()) * 225
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bb.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="HIMALAYA GENTLE BABY \nSHAMPOO",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹225",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["JOHNSON'S All Day Long Baby Lotion(500 ml)","Rs.280"])
		messagebox.showinfo('A-LOTMart','JOHNSONS All Day Long Baby Lotion is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add JOHNSONS All Day Long Baby Lotion to cart')
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

		total_price=(m.get()) * 280
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bl.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="JOHNSON'S All Day Long Baby\n Lotion",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹280",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["JOHNSON'S Baby Care Collection (7 Pieces)","Rs.310"])
		messagebox.showinfo('A-LOTMart','JOHNSONS Baby Care Collection (7 Pieces) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add JOHNSONS Baby Care Collection (7 Pieces) to cart')
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
		total_price=(m.get()) * 310
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/jc.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="JOHNSON'S Baby Care Collection\n (7 Pieces)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹310",bg="white",fg="black",font="helvetica 15 bold italic")
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
		total_price=(m.get()) * 1199
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/rc.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Kidz N Toys Big and Mean \nRock Crawling  Off-Road Hummer",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1199",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["Kidz N Toys Big and Mean Rock Crawling Off-Road Hummer RC Car/Monster Truck","Rs.1199"])
		messagebox.showinfo('A-LOTMart','Kidz N Toys Big and Mean Rock Crawling Off-Road Hummer RC Car/Monster Truck is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Kidz N Toys Big and Mean Rock Crawling Off-Road Hummer RC Car/Monster Truck to cart')

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
		total_price=(m.get()) * 221
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/teddy.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="fluffies Yellow Nylex \nTeddy Bear MotherChild-40 cm",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹221",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["fluffies Yellow Nylex Teddy Bear MotherChild-40 cm","Rs.221"])
		messagebox.showinfo('A-LOTMart','fluffies Yellow Nylex Teddy Bear MotherChild-40 cm is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add fluffies Yellow Nylex Teddy Bear MotherChild-40 cm to cart')

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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/av.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="poksi avengers of ultron\n(pack of 5 avengers)(Multicolor)",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["poksi avengers of ultron (pack of 5 avengers)(Multicolor)","Rs.299"])
		messagebox.showinfo('A-LOTMart','poksi avengers of ultron (pack of 5 avengers)(Multicolor) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add poksi avengers of ultron (pack of 5 avengers)(Multicolor) to cart')

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
		total_price=(m.get()) * 265
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bag.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="DZert Kids School Bag \nMarshall Soft Plush Cartoon\nBoys/Girls Plush Bag",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹265",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["DZert Kids School Bag","Rs.265"])
		messagebox.showinfo('A-LOTMart','DZert Kids School Bag is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add DZert Kids School Bag to cart')

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
		total_price=(m.get()) * 111
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pencil.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="APSARA Kit 6 School Set",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹111",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["APSARA Kit 6 School Set","Rs.111"])
		messagebox.showinfo('A-LOTMart','APSARA Kit 6 School Set is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add APSARA Kit 6 School Set to cart')

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
		total_price=(m.get()) * 97
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/note.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Classmate Pulse A4\n Notebook Single Line 180 Pages ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹97",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["Classmate Pulse A4 Notebook Single Line 180 Pages","Rs.97"])
		messagebox.showinfo('A-LOTMart','Classmate Pulse A4 Notebook Single Line 180 Pages is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Classmate Pulse A4 Notebook Single Line 180 Pages to cart')


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
		total_price=(m.get()) * 2268
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/art.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="FABER-CASTELL Do Art \nTravel Easel",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2268",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["FABER-CASTELL Do Art Travel Easel","Rs.2268"])
		messagebox.showinfo('A-LOTMart','FABER-CASTELL Do Art Travel Easel is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add FABER-CASTELL Do Art Travel Easel to cart')

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
		total_price=(m.get()) * 99
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pen.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)

	xr_label1=Label(bill,text="Classmate Octane \nColourburst Gel Pen",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹99",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["Classmate Octane Colourburst Gel Pen","Rs.99"])
		messagebox.showinfo('A-LOTMart','Classmate Octane Colourburst Gel Pen is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Classmate Octane Colourburst Gel Pen to cart')

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
		total_price=(m.get()) * 886
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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/barbie.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="BARBIE DOLL & ACCESSORIES",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹886",bg="white",fg="black",font="helvetica 15 bold italic")
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
		baby_list.append(["BARBIE DOLL & ACCESSORIES","Rs.886"])
		messagebox.showinfo('A-LOTMart','BARBIE DOLL & ACCESSORIES is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add BARBIE DOLL & ACCESSORIES  to cart')

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
			runpy.run_path('baby.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen1.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bat.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="WILLAGE Plastic bat for \ntennis ball Cricket Bat",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global baby_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		baby_list.append(["WILLAGE Plastic bat for tennis ball Cricket Bat","Rs.99"])
		messagebox.showinfo('A-LOTMart','WILLAGE Plastic bat for tennis ball Cricket Bat is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add WILLAGE Plastic bat for tennis ball Cricket Bat to cart')


m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bb.jpg"))
my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr=Label(baby,text="HIMALAYA GENTLE \nBABY SHAMPOO(400 ml)\n₹225",font=font1,bg="white",fg="blue")
_xr=my_canvas.create_window(20,3,anchor="nw",window=xr)
xr_btn=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cin)
_xrbtn=my_canvas.create_window(50,180,anchor="nw",window=xr_btn)
purchase_xr=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cin)
_purchase_xr=my_canvas.create_window(50,210,anchor="nw",window=purchase_xr)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bl.jpg"))
my_image=my_canvas.create_image(180,50,image=m2,anchor="nw")
xr1=Label(baby,text="JOHNSON'S All Day \nLong Baby Lotion(500 ml)\n₹280",font=font1,bg="white",fg="blue")
_xr1=my_canvas.create_window(180,3,anchor="nw",window=xr1)
xr_btn1=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_sha)
_xrbtn1=my_canvas.create_window(200,180,anchor="nw",window=xr_btn1)
purchase_xr1=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_sha)
_purchase_xr1=my_canvas.create_window(200,210,anchor="nw",window=purchase_xr1)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/jc.jpg"))
my_image=my_canvas.create_image(350,50,image=m3,anchor="nw")
xr3=Label(baby,text="JOHNSON'S Baby Care \nCollection (7 Pieces)\n₹310",font=font1,bg="white",fg="blue")
_xr3=my_canvas.create_window(370,3,anchor="nw",window=xr3)
xr_btn3=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ha)
_xrbtn3=my_canvas.create_window(370,180,anchor="nw",window=xr_btn3)
purchase_xr3=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ha)
_purchase_xr3=my_canvas.create_window(370,210,anchor="nw",window=purchase_xr3)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/rc.jpg"))
my_image=my_canvas.create_image(550,50,image=m4,anchor="nw")
xr4=Label(baby,text="Kidz N Toys Big and Mean \nRock Crawling  Off-Road Hummer \nRC Car/Monster Truck ₹1,199",font=font1,bg="white",fg="blue")
_xr4=my_canvas.create_window(550,3,anchor="nw",window=xr4)
xr_btn4=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_pa)
_xrbtn4=my_canvas.create_window(550,180,anchor="nw",window=xr_btn4)
purchase_xr4=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_pa)
_purchase_xr4=my_canvas.create_window(550,210,anchor="nw",window=purchase_xr4)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/teddy.jpg"))
my_image=my_canvas.create_image(750,50,image=m5,anchor="nw")
xr5=Label(baby,text="fluffies Yellow Nylex \nTeddy Bear MotherChild-40 cm\n ₹221",font=font1,bg="white",fg="blue")
_xr5=my_canvas.create_window(750,3,anchor="nw",window=xr5)
xr_btn5=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bru)
_xrbtn5=my_canvas.create_window(750,180,anchor="nw",window=xr_btn5)
purchase_xr5=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bru)
_purchase_xr5=my_canvas.create_window(750,210,anchor="nw",window=purchase_xr5)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/av.jpg"))
my_image=my_canvas.create_image(950,50,image=m6,anchor="nw")
xr6=Label(baby,text="poksi avengers of ultron\n(pack of 5 avengers)(Multicolor)\n₹299",font=font1,bg="white",fg="blue")
_xr6=my_canvas.create_window(950,3,anchor="nw",window=xr6)
xr_btn6=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_su)
_xrbtn6=my_canvas.create_window(950,180,anchor="nw",window=xr_btn6)
purchase_xr6=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_su)
purchase_xr6=my_canvas.create_window(950,210,anchor="nw",window=purchase_xr6)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bag.jpg"))
my_image=my_canvas.create_image(25,350,image=m7,anchor="nw")
xr7=Label(baby,text="DZert Kids School Bag \nMarshall Soft Plush Cartoon\nBoys/Girls Plush Bag ₹265",font=font1,bg="white",fg="blue")
_xr7=my_canvas.create_window(25,300,anchor="nw",window=xr7)
xr_btn7=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_no)
_xrbtn7=my_canvas.create_window(25,490,anchor="nw",window=xr_btn7)
purchase_xr7=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_no)
purchase_xr7=my_canvas.create_window(25,520,anchor="nw",window=purchase_xr7)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pencil.jpg"))
my_image=my_canvas.create_image(200,350,image=m8,anchor="nw")
xr8=Label(baby,text="APSARA Kit 6 School Set\n₹111",font=font1,bg="white",fg="blue")
_xr8=my_canvas.create_window(200,300,anchor="nw",window=xr8)
xr_btn8=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ml)
_xrbtn8=my_canvas.create_window(200,490,anchor="nw",window=xr_btn8)
purchase_xr8=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ml)
purchase_xr8=my_canvas.create_window(200,520,anchor="nw",window=purchase_xr8)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/note.jpg"))
my_image=my_canvas.create_image(400,350,image=m9,anchor="nw")
xr9=Label(baby,text="Classmate Pulse A4\n Notebook Single Line \n180 Pages ₹97",font=font1,bg="white",fg="blue")
_xr9=my_canvas.create_window(400,300,anchor="nw",window=xr9)
xr_btn9=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bt)
_xrbtn9=my_canvas.create_window(400,490,anchor="nw",window=xr_btn9)
purchase_xr9=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bt)
purchase_xr9=my_canvas.create_window(400,520,anchor="nw",window=purchase_xr9)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/art.jpg"))
my_image=my_canvas.create_image(1150,50,image=m10,anchor="nw")
xr10=Label(baby,text="FABER-CASTELL Do Art \nTravel Easel\n ₹2,268",font=font1,bg="white",fg="blue")
_xr10=my_canvas.create_window(1150,3,anchor="nw",window=xr10)
xr_btn10=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cof)
_xrbtn10=my_canvas.create_window(1150,180,anchor="nw",window=xr_btn10)
purchase_xr10=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cof)
purchase_xr10=my_canvas.create_window(1150,210,anchor="nw",window=purchase_xr10)

m11=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/pen.jpg"))
my_image=my_canvas.create_image(750,350,image=m11,anchor="nw")
xr11=Label(baby,text="Classmate Octane \nColourburst Gel Pen\n(Pack of 10) ₹99",font=font1,bg="white",fg="blue")
_xr11=my_canvas.create_window(750,300,anchor="nw",window=xr11)
xr_btn11=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_oil)
_xrbtn11=my_canvas.create_window(750,490,anchor="nw",window=xr_btn11)
purchase_xr11=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_oil)
purchase_xr11=my_canvas.create_window(750,520,anchor="nw",window=purchase_xr11)

m12=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/barbie.jpg"))
my_image=my_canvas.create_image(950,350,image=m12,anchor="nw")
xr12=Label(baby,text="BARBIE DOLL & ACCESSORIES (Multicolor)\n₹886",font=font1,bg="white",fg="blue")
_xr12=my_canvas.create_window(950,300,anchor="nw",window=xr12)
xr_btn12=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta)
_xrbtn12=my_canvas.create_window(950,490,anchor="nw",window=xr_btn12)
purchase_xr12=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta)
purchase_xr12=my_canvas.create_window(950,520,anchor="nw",window=purchase_xr12)

m13=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/bat.jpg"))
my_image=my_canvas.create_image(550,350,image=m13,anchor="nw")
xr13=Label(baby,text="WILLAGE Plastic bat for \ntennis ball Cricket Bat \n₹399",font=font1,bg="white",fg="blue")
_xr13=my_canvas.create_window(570,300,anchor="nw",window=xr13)
xr_btn13=Button(baby,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta1)
_xrbtn13=my_canvas.create_window(550,490,anchor="nw",window=xr_btn13)
purchase_xr13=Button(baby,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta1)
purchase_xr13=my_canvas.create_window(550,520,anchor="nw",window=purchase_xr13)

baby_list=[]
baby.mainloop()