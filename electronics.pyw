from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import smtplib
import runpy
import ctypes
from tkinter.font import Font
ctypes.windll.shcore.SetProcessDpiAwareness(1)

fashion=Tk()
fashion.title('A-LOTMart - Fashion')
fashion.geometry('2000x2000+0+0')
fashion.state('zoomed')
fashion.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
my_canvas=Canvas(fashion,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
font1=Font(family="Poppins-Light",size=8,weight='bold')
def back():
	fashion.destroy()
	runpy.run_path('e-Commerce_main.pyw')
back_btn=Button(fashion,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 20 bold italic",command=back)
back_btn_win=my_canvas.create_window(1200,400,anchor="nw",window=back_btn)

def add_cin():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["ADIDAS Self Design Men Round Neck Dark Blue T-Shirt","Rs.5359"])
		messagebox.showinfo('A-LOTMart','ADIDAS Self Design Men Round Neck Dark Blue T-Shirt is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add ADIDAS Self Design Men Round Neck Dark Blue T-Shirt to cart')
def buy_cin():
	fashion.destroy()
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
		total_price=(m.get()) * 5359
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/ts.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="ADIDAS Self Design Men \nRound Neck Dark Blue T-Shirt",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹5359",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)

	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()

def add_sha():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["PETER ENGLAND Men Slim Fit Solid Formal Shirt","Rs.1699"])
		messagebox.showinfo('A-LOTMart','PETER ENGLAND Men Slim Fit Solid Formal Shirt is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add PETER ENGLAND Men Slim Fit Solid Formal Shirt to cart')
def buy_sha():
	fashion.destroy()
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

		total_price=(m.get()) * 1699
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/shirt.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetiac 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="PETER ENGLAND Men \nSlim Fit Solid Formal Shirt",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1699",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Size",font="helvetica 15 bold italic",bg="white",fg="black")
	qty_lab_win=my_canvas.create_window(200,150,anchor='nw',window=qty_lab)
	s_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
	s_lab_win=my_canvas.create_window(400,150,anchor='nw',window=s_lab)
	m=IntVar()
	s=ttk.Combobox(bill,textvariable=m,width=10)
	s['values']=('1','2','3','4','5')
	s.current(1)
	s_win=my_canvas.create_window(450,150,anchor="nw",window=s)
	
	n=IntVar()
	qty=ttk.Combobox(bill,textvariable=n,width=10)
	qty['values']=('S','M','L','XL','XXL')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_ha():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["FUBAR Men Striped Cotton Blend Straight Kurta(Yellow)","Rs.425"])
		messagebox.showinfo('A-LOTMart','FUBAR Men Striped Cotton Blend Straight Kurta(Yellow) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add FUBAR Men Striped Cotton Blend Straight Kurta(Yellow) to cart')
def buy_ha():
	fashion.destroy()
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
		total_price=(m.get()) * 425
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/kur.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="FUBAR Men Striped Cotton \nBlend Straight Kurta(Yellow)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹425",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
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

def buy_pa():
	fashion.destroy()
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
		total_price=(m.get()) * 8860
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/saree.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Sretan Embroidered Silk \nSaree(Blue)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹8860",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Sretan Embroidered Silk Saree(Blue)","Rs.90"])
		messagebox.showinfo('A-LOTMart','Sretan Embroidered Silk Saree(Blue) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Sretan Embroidered Silk Saree(Blue) to cart')

def buy_bru():
	fashion.destroy()
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
		total_price=(m.get()) * 6999
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chudi.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="KAPANKU Georgette Embroidered \nKurta & Churidar Material",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹6999",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["KAPANKU Georgette Embroidered  Kurta & Churidar Material","Rs.6999"])
		messagebox.showinfo('A-LOTMart',' KAPANKU Georgette Embroidered Kurta & Churidar Material is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add KAPANKU Georgette Embroidered Kurta & Churidar Material to cart')

def buy_su():
	fashion.destroy()
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
		total_price=(m.get()) * 37990
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/leh.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Q QXZ Embroidered Semi \nStitched Lehenga Choli(Black)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹37990",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Q QXZ Embroidered Semi Stitched Lehenga Choli(Black)","Rs.37990"])
		messagebox.showinfo('A-LOTMart','Q QXZ Embroidered Semi Stitched Lehenga Choli(Black) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Q QXZ Embroidered Semi Stitched Lehenga Choli(Black) to cart')

def buy_no():
	fashion.destroy()
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
		total_price=(m.get()) * 1399
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/boy.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="TOMMY HILFIGER Boys \nPrinted Pure Cotton T Shirt(White)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹1399",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
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
def add_no():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["TOMMY HILFIGER Boys Printed Pure Cotton T Shirt (White)","Rs.1399"])
		messagebox.showinfo('A-LOTMart','TOMMY HILFIGER Boys Printed Pure Cotton T Shirt (White) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add TOMMY HILFIGER Boys Printed Pure Cotton T Shirt (White) to cart')

def buy_ml():
	fashion.destroy()
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
		total_price=(m.get()) * 12999
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/girl.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="rayie collection Girls\nMaxi/Full Length Party Dress",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹12999",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_price1=my_canvas.create_window(350,100,anchor='nw',window=xr_price1)
	qty_lab=Label(bill,text="Qty",font="helvetica 15 bold italic",bg="white",fg="black")
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
def add_ml():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["rayie collection Girls Maxi/Full Length Party Dress","Rs.12999"])
		messagebox.showinfo('A-LOTMart','rayie collection Girls Maxi/Full Length Party Dress is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add rayie collection Girls Maxi/Full Length Party Dress to cart')

def buy_bt():
	fashion.destroy()
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
		total_price=(m.get()) * 795
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/w1.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Fastrack NG38003PP13J \nAnalog Watch For Men & Women ",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹795",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Fastrack NG38003PP13J Analog Watch For Men & Women","Rs.795"])
		messagebox.showinfo('A-LOTMart','Fastrack NG38003PP13J Analog Watch For Men & Women is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Fastrack NG38003PP13J Analog Watch For Men & Women to cart')


def buy_cof():
	fashion.destroy()
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
		total_price=(m.get()) * 2599
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/unishirt.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="WRANGLER-Combo Shirt(3pcs)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2,599",bg="white",fg="black",font="helvetica 15 bold italic")
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
def add_cof():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["WRANGLER-Combo Shirt","Rs.2,599"])
		messagebox.showinfo('A-LOTMart','WRANGLER-Combo Shirt is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add WRANGLER-Combo Shirt to cart')

def buy_oil():
	fashion.destroy()
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
		total_price=(m.get()) * 19999
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/shoe.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Cole Haan Derby For Men(Brown)",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹19999",bg="white",fg="black",font="helvetica 15 bold italic")
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
	qty['values']=('8','9','10','11','12')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_oil():
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Cole Haan Derby For Men(Brown)","Rs.19999"])
		messagebox.showinfo('A-LOTMart','Cole Haan Derby For Men (Brown) is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Cole Haan Derby For Men (Brown) to cart')

def buy_atta():
	fashion.destroy()
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
		total_price=(m.get()) * 7500
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)

	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/slip.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Cole Haan Women\nPink Heels Sandal",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹7500",bg="white",fg="black",font="helvetica 15 bold italic")
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
	qty['values']=('8','9','10','11','12')
	qty.current(0)
	qty_window=my_canvas.create_window(250,150,anchor="nw",window=qty)
	btn=Button(bill,text="PAY NOW",bg="orange",fg="white",font="helvetica 15 italic",command=pay)
	_btn=my_canvas.create_window(350,200,anchor="nw",window=btn)
	bill.mainloop()
def add_atta():
	global grocery_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Cole Haan Women Pink Heels Sandal","Rs.7500"])
		messagebox.showinfo('A-LOTMart','Cole Haan Women Pink Heels Sandal is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Cole Haan Women Pink Heels Sandal to cart')

def buy_atta1():
	fashion.destroy()
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
		total_price=(m.get()) * 2274
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
			runpy.run_path('electronics.pyw')
		back_btn=Button(bill,text="BACK",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=back)
		back_btn_win=my_canvas.create_window(750,200,anchor="nw",window=back_btn)


	my_canvas=Canvas(bill,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
	my_canvas.pack(fill='both',expand='true')
	bill.state('zoomed')
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/vegen.png"))
	my_canvas.create_image(0,0,anchor="nw",image=bg)
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/w2.jpg"))
	my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
	xr_label=Label(bill,text="Product Name:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_label=my_canvas.create_window(200,50,anchor="nw",window=xr_label)
	xr_label1=Label(bill,text="Swiss Trend Couple16 \n For Men&Women",bg="white",fg="black",font="helvetica 15 bold italic")
	_xr_label1=my_canvas.create_window(350,50,anchor='nw',window=xr_label1)
	xr_price=Label(bill,text="Price:",font="helvetica 15 bold italic",bg="white",fg="black")
	_xr_price=my_canvas.create_window(200,100,anchor="nw",window=xr_price)
	xr_price1=Label(bill,text="₹2274",bg="white",fg="black",font="helvetica 15 bold italic")
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
	global fashion_list
	mob=messagebox.askyesno('A-LOTMart','Are You sure that you want to add this item to cart?')
	if mob:
		fashion_list.append(["Swiss Trend Couple16 Analog Watch For Men&Women","Rs.2274"])
		messagebox.showinfo('A-LOTMart','Swiss Trend Couple16 Analog Watch For Men & Women is successfully added to cart')
		return
	else:
		messagebox.showinfo('A-LOTMart','Failed to add Swiss Trend Couple16 Analog Watch For Men & Women to cart')


m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/ts.jpg"))
my_image=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr=Label(fashion,text="ADIDAS Self Design Men \nRound Neck Dark Blue\nT-Shirt ₹5,359",font=font1,bg="white",fg="blue")
_xr=my_canvas.create_window(20,3,anchor="nw",window=xr)
xr_btn=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cin)
_xrbtn=my_canvas.create_window(50,180,anchor="nw",window=xr_btn)
purchase_xr=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cin)
_purchase_xr=my_canvas.create_window(50,210,anchor="nw",window=purchase_xr)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/shirt.jpg"))
my_image=my_canvas.create_image(180,50,image=m2,anchor="nw")
xr1=Label(fashion,text="PETER ENGLAND Men \nSlim Fit Solid \nFormal Shirt₹1,699",font=font1,bg="white",fg="blue")
_xr1=my_canvas.create_window(180,3,anchor="nw",window=xr1)
xr_btn1=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_sha)
_xrbtn1=my_canvas.create_window(200,180,anchor="nw",window=xr_btn1)
purchase_xr1=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_sha)
_purchase_xr1=my_canvas.create_window(200,210,anchor="nw",window=purchase_xr1)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/kur.jpg"))
my_image=my_canvas.create_image(350,50,image=m3,anchor="nw")
xr3=Label(fashion,text="FUBAR Men Striped Cotton \nBlend Straight Kurta(Yellow)\n₹425",font=font1,bg="white",fg="blue")
_xr3=my_canvas.create_window(370,3,anchor="nw",window=xr3)
xr_btn3=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ha)
_xrbtn3=my_canvas.create_window(370,180,anchor="nw",window=xr_btn3)
purchase_xr3=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ha)
_purchase_xr3=my_canvas.create_window(370,210,anchor="nw",window=purchase_xr3)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/saree.jpg"))
my_image=my_canvas.create_image(550,50,image=m4,anchor="nw")
xr4=Label(fashion,text="Sretan Embroidered Silk \nSaree(Blue) ₹8,860",font=font1,bg="white",fg="blue")
_xr4=my_canvas.create_window(550,3,anchor="nw",window=xr4)
xr_btn4=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_pa)
_xrbtn4=my_canvas.create_window(550,180,anchor="nw",window=xr_btn4)
purchase_xr4=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_pa)
_purchase_xr4=my_canvas.create_window(550,210,anchor="nw",window=purchase_xr4)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/chudi.jpg"))
my_image=my_canvas.create_image(750,50,image=m5,anchor="nw")
xr5=Label(fashion,text="KAPANKU Georgette \nEmbroidered Kurta & Churidar \nMaterial ₹6,999",font=font1,bg="white",fg="blue")
_xr5=my_canvas.create_window(750,3,anchor="nw",window=xr5)
xr_btn5=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bru)
_xrbtn5=my_canvas.create_window(750,180,anchor="nw",window=xr_btn5)
purchase_xr5=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bru)
_purchase_xr5=my_canvas.create_window(750,210,anchor="nw",window=purchase_xr5)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/leh.jpg"))
my_image=my_canvas.create_image(950,50,image=m6,anchor="nw")
xr6=Label(fashion,text="Q QXZ Embroidered Semi \nStitched Lehenga Choli(Black)\n₹37,990",font=font1,bg="white",fg="blue")
_xr6=my_canvas.create_window(950,3,anchor="nw",window=xr6)
xr_btn6=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_su)
_xrbtn6=my_canvas.create_window(950,180,anchor="nw",window=xr_btn6)
purchase_xr6=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_su)
purchase_xr6=my_canvas.create_window(950,210,anchor="nw",window=purchase_xr6)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/boy.jpg"))
my_image=my_canvas.create_image(25,350,image=m7,anchor="nw")
xr7=Label(fashion,text="TOMMY HILFIGER Boys \nPrinted Pure Cotton T Shirt\n (White)₹1,399",font=font1,bg="white",fg="blue")
_xr7=my_canvas.create_window(25,300,anchor="nw",window=xr7)
xr_btn7=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_no)
_xrbtn7=my_canvas.create_window(25,490,anchor="nw",window=xr_btn7)
purchase_xr7=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_no)
purchase_xr7=my_canvas.create_window(25,520,anchor="nw",window=purchase_xr7)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/girl.jpg"))
my_image=my_canvas.create_image(200,350,image=m8,anchor="nw")
xr8=Label(fashion,text="rayie collection Girls \nMaxi/Full Length Party Dress\n(White)₹12,999",font=font1,bg="white",fg="blue")
_xr8=my_canvas.create_window(200,300,anchor="nw",window=xr8)
xr_btn8=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_ml)
_xrbtn8=my_canvas.create_window(200,490,anchor="nw",window=xr_btn8)
purchase_xr8=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_ml)
purchase_xr8=my_canvas.create_window(200,520,anchor="nw",window=purchase_xr8)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/w1.jpg"))
my_image=my_canvas.create_image(400,350,image=m9,anchor="nw")
xr9=Label(fashion,text="Fastrack NG38003PP13J \nAnalog Watch For \nMen & Women ₹795",font=font1,bg="white",fg="blue")
_xr9=my_canvas.create_window(400,300,anchor="nw",window=xr9)
xr_btn9=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_bt)
_xrbtn9=my_canvas.create_window(400,490,anchor="nw",window=xr_btn9)
purchase_xr9=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_bt)
purchase_xr9=my_canvas.create_window(400,520,anchor="nw",window=purchase_xr9)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/unishirt.jpg"))
my_image=my_canvas.create_image(1150,50,image=m10,anchor="nw")
xr10=Label(fashion,text="WRANGLER-Combo\nShirt(3pcs) ₹2,599",font=font1,bg="white",fg="blue")
_xr10=my_canvas.create_window(1150,3,anchor="nw",window=xr10)
xr_btn10=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_cof)
_xrbtn10=my_canvas.create_window(1150,180,anchor="nw",window=xr_btn10)
purchase_xr10=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_cof)
purchase_xr10=my_canvas.create_window(1150,210,anchor="nw",window=purchase_xr10)

m11=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/shoe.jpg"))
my_image=my_canvas.create_image(750,350,image=m11,anchor="nw")
xr11=Label(fashion,text="Cole Haan Derby For Men \n(Brown)\n₹19,999",font=font1,bg="white",fg="blue")
_xr11=my_canvas.create_window(750,300,anchor="nw",window=xr11)
xr_btn11=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_oil)
_xrbtn11=my_canvas.create_window(750,490,anchor="nw",window=xr_btn11)
purchase_xr11=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_oil)
purchase_xr11=my_canvas.create_window(750,520,anchor="nw",window=purchase_xr11)

m12=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/slip.jpg"))
my_image=my_canvas.create_image(950,350,image=m12,anchor="nw")
xr12=Label(fashion,text="Cole Haan Women \nPink Heels Sandal\n₹7,500",font=font1,bg="white",fg="blue")
_xr12=my_canvas.create_window(950,300,anchor="nw",window=xr12)
xr_btn12=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta)
_xrbtn12=my_canvas.create_window(950,490,anchor="nw",window=xr_btn12)
purchase_xr12=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta)
purchase_xr12=my_canvas.create_window(950,520,anchor="nw",window=purchase_xr12)

m13=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/w2.jpg"))
my_image=my_canvas.create_image(550,350,image=m13,anchor="nw")
xr13=Label(fashion,text="Swiss Trend Couple16 \nAnalog Watch For Men & \nWomen₹2,274",font=font1,bg="white",fg="blue")
_xr13=my_canvas.create_window(570,300,anchor="nw",window=xr13)
xr_btn13=Button(fashion,text="ADD TO CART",bg="green",fg="white",font="helvetica 10 bold italic",command=add_atta1)
_xrbtn13=my_canvas.create_window(550,490,anchor="nw",window=xr_btn13)
purchase_xr13=Button(fashion,text="BUY NOW",bg="orange",fg="white",font="helvetica 10 bold italic",width=11,command=buy_atta1)
purchase_xr13=my_canvas.create_window(550,520,anchor="nw",window=purchase_xr13)

fashion_list=[]
fashion.mainloop()
