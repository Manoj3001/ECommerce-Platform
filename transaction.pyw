from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import runpy
from tkinter import ttk
from tkinter.font import Font
import smtplib
import random
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

          
#----------------------------------------------------------------------------------------

def finish():
     A.destroy()
     def pay():
          global OTP
          #otpent=StringVar()
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
               mail_id=emailid.get()
               server.sendmail(sender_email,mail_id,msg)
               print("sent")

     
     c_no=Cardnumber.get()
     if(len(c_no)==0):
          messagebox.showinfo("ALM-Reckon","Pls enter your Card Number",icon="warning")
          return
     if(len(c_no)<12):
          messagebox.showinfo("ALM-Reckon","Transaction denied ; Pls Enter your correct Card number",icon="warning")
          return
     
     exp_yr=Expiryyear.get()
     if(len(exp_yr)==0):
          messagebox.showinfo("ALM-Reckon","Pls enter your Expiry year",icon="warning")
          return
     if(len(exp_yr)<4):
          messagebox.showinfo("ALM-Reckon","Transaction denied Pls Enter your correct Expiry year",icon="warning")
          return
     
     cvv=CVV.get()
     if(len(cvv)==0):
          messagebox.showinfo("ALM-Reckon","Pls enter your CVV code",icon="warning")
          return
     if(len(exp_yr)<3):
          messagebox.showinfo("ALM-Reckon","Transcaction denied pls Enter your correct CVV Code",icon="warning")
          return
     
     
     c_name=Cardname.get()
     if(len(c_name)==0):
          messagebox.showinfo("ALM-Reckon","Pls enter the name on your card",icon="warning")
          return  
     
     e_m=emailid.get()
     if(len(e_m)==0):
          messagebox.showinfo("ALM-Reckon","Pls enter your Email-id",icon="warning")
          return

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
     mail_id=emailid.get()
     server.sendmail(sender_email,mail_id,msg)
     print("sent",OTP)
     otp1=Label(f1,text="OTP:",bg="white",fg="red",font=font3).grid(row=25,column=0,padx=5,pady=5)
     #_otp1=my_canvas.create_window(500,500,anchor="nw",window=otp1)
     otpent=StringVar()
     otp_ent=Entry(f1,textvariable=otpent,font=font3,width=20,bg="white",fg="black").grid(row=25,column=1,padx=5,pady=5)
    # _otp_ent=my_canvas.create_window(600,500,anchor="nw",window=otp_ent)
     #fin_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/sub1.png')
     fin_btn=Button(f1,text="PAY NOW",borderwidth=0,fg="white",bg="orange",font=font3,command=pay)
     fin_btn.grid(row=28,column=1,padx=5,pady=5)
     
     #mg=messagebox.showinfo("ALM-Reckon","You have successfully subscribed for ALM-Reckon")
     #if(mg=="ok"):
     #     page5.destroy()
     #     runpy.run_path('reckon.pyw')


#------------------------------OTP------------------------------------------------------          

#---------------------------------------------------------------------------------------
page5=Tk()
page5.title("Payment")
page5.geometry('2000x2000') 
page5.configure(background="black")
page5.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
font3=Font(family="Poppins-Semibold",size=15)
my_img=Image.open(r"C:\Users\i5\Desktop\PYTHON PRGS\E Commerce project\trans.jpg")
resized=my_img.resize((1370,1370),Image.ANTIALIAS)
new_img=ImageTk.PhotoImage(resized)
my_label=Label(image=new_img)
my_label.pack()




#------------------------------------------------------------------------------------------
Cardnumber=StringVar()
Expiryyear=StringVar()
CVV=StringVar()
emailid=StringVar()
Cardname=StringVar()

f1=Frame(page5,bg='white',bd=10,relief=FLAT)
f1.place(x=350,y=280)
lbl0=Label(f1,text="Payment")
lbl1=Label(f1,text="Card number",bg="white",fg="red",font=font3).grid(row=2,column=0,padx=5,pady=5)
a1=Entry(f1,bg="ivory2",textvariable=Cardnumber,width=25,font=font3).grid(row=2,column=4,padx=5,pady=5)
lbl2=ttk.Label(f1,text="Expiry month",background="white",foreground="red",font=font3).grid(row=6,column=0,
                                                                      padx=5,pady=5)
z=StringVar()
date_of_birth=ttk.Combobox(f1,width=5,font=font3,textvariable=z,state='readonly')
date_of_birth['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
date_of_birth.grid(row=7,column=0,padx=5,pady=5)
date_of_birth.current(0)
lbl3=Label(f1,text="Expiry year",bg="white",fg="red",font=font3).grid(row=6,column=4,padx=5,pady=5)
a3=Entry(f1,bg="ivory2",textvariable=Expiryyear,width=15,font=font3).grid(row=7,column=4,padx=5,pady=5)
lbl4=Label(f1,text="CVV Code",bg="white",fg="red",font=font3).grid(row=12,column=0,padx=5,pady=5)
a4=Entry(f1,bg="ivory2",textvariable=CVV,width=15,font=font3).grid(row=12,column=4,padx=5,pady=5)
lbl5=Label(f1,text="Email-id",bg="white",fg="red",font=font3).grid(row=16,column=0,padx=5,pady=5)
a7=Entry(f1,bg="ivory2",width=25,textvariable=emailid,font=font3).grid(row=16,column=4,padx=5,pady=5)

Label(f1,text="Name on the card",bg="white",fg="red",font=font3).grid(row=20,column=0,padx=5,pady=5)
a6=Entry(f1,bg="ivory2",width=25,textvariable=Cardname,font=font3).grid(row=20,column=4,padx=5,pady=5)

#-----------------------------------------------------------------------------------------
reg_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/com.png')
A=Button(f1,image=reg_img,bd=0,bg="white",command=finish)
A.grid(row=28,column=1,padx=5,pady=5)
page5.state('zoomed')
page5.mainloop()



