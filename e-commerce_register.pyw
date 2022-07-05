from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.font import Font
import runpy
import smtplib
import random
import openpyxl
from xlrd import open_workbook
C=Tk()
C.iconbitmap(C,r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
C.title("A-LOTMart- Register")
C.geometry('2000x2000+0+0')
C.state('zoomed')
#C.config(bg="white")
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/shop5.jpg"))
my_canvas=Canvas(C,width=2000,height=2000,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")
global OTP
otpent=StringVar()
firstname=StringVar()
#lastname=StringVar()
pwdent=StringVar()
mailid=StringVar()
_firstname=firstname.get()
#_lastname=lastname.get()
_pwdent=pwdent.get()
_mailid=mailid.get()

#font1=Font(family="Cambria",size=50,slant="italic")
#font2=Font(family="Palatino Linotype",size=20,slant="italic")
font3=Font(family="Poppins-Semibold",size=15)

def submit():
	
	_firstname=firstname.get()
	#_lastname=lastname.get()
	_pwdent=pwdent.get()
	_mailid=mailid.get()
	if(len(_firstname)==0):
		messagebox.showinfo(title="A-LOTMart",message="Please enter your First Name",icon="warning")
		return
	if(len(_mailid)==0):
		messagebox.showinfo(title="A-LOTMart",message="Please enter your E-Mail ID",icon="warning")
		return
	if(len(_pwdent)==0):
		messagebox.showinfo(title="A-LOTMart",message="Please enter your Password",icon="warning")
		return
	if(len(_pwdent)<5):
		messagebox.showinfo(title="A-LOTMart",message="Please enter a valid Password",icon="warning")
		return
	if(len(_pwdent)>5):
		messagebox.showinfo(title="A-LOTMart",message="Please enter a valid Password",icon="warning")
		return
	sub_btn.destroy()
	def finish():
		sub_btn.destroy()
		global OTP
		_otp=otpent.get()
		if(len(_otp)==0):
			messagebox.showinfo(title="A-LOTMart",message="Please enter the OTP",icon="warning")
			return
		if((_otp)!=OTP):
			messagebox.showinfo(title="A-LOTMart",message="Please enter the correct OTP",icon="warning")
			return
		if(_otp==OTP):
			msg='Hello User!\n\n\tYour account is successfully registered...'
			sender_email="almalotmart@gmail.com"
			sender_password="commerce2021"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender_email,sender_password)
			print('done')
			mail_id=mailid.get()
			server.sendmail(sender_email,mail_id,msg)
			print("sent")
			f=open_workbook('login_details.xlsx')
			sheet1=f.sheet_by_index(0)
			for i in range(100000):
				try:
					val=sheet1.cell_value(i,0)
					if val:
						continue
					else:
						break
				except:
					break
			row=i+1
			write=openpyxl.load_workbook('login_details.xlsx')
			email='A'+str(row)
			password='B'+str(row)
			name='C'+str(row)
			sheet=write['details']
			sheet[email]=_mailid
			sheet[password]=_pwdent
			sheet[name]=_firstname
			write.save('login_details.xlsx')
			C.quit()
			C.destroy()
			runpy.run_path('e-Commerce_login.pyw')


	global OTP
	digit="1234567890"
	otp_len=4
	OTP="".join(random.sample(digit,otp_len))
	msg='Hello!\n\t\tYour OTP is '+OTP+ ''
	sender_email="almalotmart@gmail.com"
	sender_password="commerce2021"
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(sender_email,sender_password)
	print("done")
	mail_id=mailid.get()
	server.sendmail(sender_email,mail_id,msg)
	print("sent",OTP)
	otp1=Label(C,text="OTP:",bg="white",fg="black",font=font3)
	_otp1=my_canvas.create_window(500,500,anchor="nw",window=otp1)
	otpent=StringVar()
	otp_ent=Entry(C,textvariable=otpent,font=font3,width=20)
	_otp_ent=my_canvas.create_window(600,500,anchor="nw",window=otp_ent)
	fin_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/sub1.png')
	fin_btn=Button(C,image=sub_img,borderwidth=0,bg="white",command=finish)
	fin_btn.place(x=500,y=550)
	#finish_btn=Button(C,text="Finish",bg=,fg="white",font='helvetica 15 bold',command=finish).place(x=100,y=550)


f_name=Label(C,text="Name:",bg="white",fg="black",font=font3)
_fname=my_canvas.create_window(500,310,anchor="nw",window=f_name)
f_entry=Entry(C,textvariable=firstname,font=font3,width=20)
_fentry=my_canvas.create_window(600,310,anchor="nw",window=f_entry)

mail_id=Label(C,text="E-Mail:",bg="white",fg="black",font=font3)
mail=my_canvas.create_window(500,360,anchor="nw",window=mail_id)
mail_entry=Entry(C,textvariable=mailid,font=font3,width=20)
_mail=my_canvas.create_window(600,360,anchor="nw",window=mail_entry)

password=Label(C,text="Password:",bg="white",fg="black",font=font3)
_pa=my_canvas.create_window(500,410,anchor="nw",window=password)
pwd_ent=Entry(C,textvariable=pwdent,font=font3,show="●",width=20)
pa=my_canvas.create_window(600,410,anchor="nw",window=pwd_ent)

pwd_label=Label(C,text="*Note: Password must be 5 letter length",bg="white",fg="red",font=font3)
_pwd_label=my_canvas.create_window(490,460,anchor="nw",window=pwd_label)

sub_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/sub1.png')
sub_btn=Button(C,image=sub_img,borderwidth=0,bg="white",command=submit)

sub_btn.place(x=500,y=550)

C.mainloop()