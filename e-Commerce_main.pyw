from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter.font import Font
import mysql.connector
import runpy
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)



mydb=mysql.connector.connect(host="localhost",user="root",password="adrsm3096",database="categories",auth_plugin='mysql_native_password')
cursor=mydb.cursor()
options=[]
sql="SELECT mart_id,things_name FROM things"
cursor.execute(sql)
ids=cursor.fetchall()
for i in ids:
	options.append(str(i[0])+"-"+i[1])
D=Tk()
D.title('A-LOTMart')
D.config(bg='white')
D.geometry('2000x2000+0+0')
#style=ThemedStyle(D)
#style.set_theme("magenta2")
D.state('zoomed')
D.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\ALM.ico')
opts=StringVar()
def search():
	pass
def log_out():
	m=messagebox.askquestion(title="A-LOTMart",message="Are You sure; You want to Signout")
	if(m=="yes"):
		D.destroy()
		runpy.run_path('e-Commerce_login.pyw')
def mobile():
	D.destroy()
	file1=runpy.run_path('mobile.pyw')
def grocery():
	D.destroy()
	file2=runpy.run_path('grocery.pyw') 
def fashion():
	D.destroy()
	file3=runpy.run_path('electronics.pyw') 
def baby():
	D.destroy()
	file4=runpy.run_path('baby.pyw') 
def electronics():
	D.destroy()
	file6=runpy.run_path('fashion.pyw') 
def furniture():
	D.destroy()
	file8=runpy.run_path('furniture.pyw') 
def sports():
	D.destroy()
	file7=runpy.run_path('sports.pyw') 
def plastic():
	D.destroy()
	file9=runpy.run_path('home.pyw') 
def beauty():
	D.destroy()
	file5=runpy.run_path('beauty.pyw') 
def books():
	D.destroy()
	file5=runpy.run_path('books.pyw') 
def travel():
	D.destroy()
	file10=runpy.run_path('travel.pyw') 
def reckon():
	D.destroy()	
	file=runpy.run_path('veg_main.pyw')
font1=Font(family="Poppins Semibold",size=12,weight="bold")
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/A1.jpg"))
my_canvas=Canvas(D,width=2000,height=2000,bd=0,highlightthickness=0,bg="white")
my_canvas.pack(fill='both',expand='true')
my_image=my_canvas.create_image(0,0,image=bg,anchor="nw")
#m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/ALM.png"))
#_m1=my_canvas.create_image(50,10,image=m1,anchor="nw")
mycombo=ttk.Combobox(D,textvariable=opts,width=30,font=font1,state='readonly')
mycombo['values']=options
mycombo.set('Search for products,brands')
mycombo.pack(padx=10,pady=10)
mycombo_win=my_canvas.create_window(300,100,anchor="nw",window=mycombo)
def apply():
	_cou=cou.get()
	if(len(_cou)<9):
		messagebox.showerror('A-LOTMart','Please Enter A Valid Coupon Code ')
		return
	if(_cou != "ALM319648"):
		messagebox.showerror('A-LOTMart','Please Enter the Correct Coupon Code')
		return
	else:
		D.destroy()
		runpy.run_path('coupon.pyw')
coupon=Label(D,text="Enter Coupon Code",bg="white",fg="red",font=font1)
_cup=my_canvas.create_window(300,150,anchor="nw",window=coupon)
cou=StringVar()
coupon_ent=Entry(D,textvariable=cou,bg="white",fg="black",font=font1)
_ent=my_canvas.create_window(480,150,anchor="nw",window=coupon_ent)
font2=Font(family="Poppins Semibold",weight="bold",size=10)
coup_btn=Button(D,text="APPLY",bg="red",fg="white",font="helvetica 15 bold italic",width=6,height=1,command=apply)
coup_btn_=my_canvas.create_window(700,150,anchor="nw",window=coup_btn)

search_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/search.png')
Search_btn=Button(D,image=search_img,borderwidth=0,command=search)
Search_btn_win=my_canvas.create_window(624,97,anchor="nw",window=Search_btn)

log_out_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/signout.png')
log_out_btn=Button(D,image=log_out_img,borderwidth=0,command=log_out,width=80)
log_out_btn_win=my_canvas.create_window(700,95,anchor="nw",window=log_out_btn)

#mobile
mobile_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/mobile.png')
mobile_btn=Button(D,image=mobile_img,borderwidth=0,bg="white",command=mobile)
mobile_btn_win=my_canvas.create_window(50,200,anchor="nw",window=mobile_btn)
mobile_lbl=Label(D,text="Mobile",font=font1,bg="white",fg="magenta2")
mobile_lbl_win=my_canvas.create_window(70,330,anchor="nw",window=mobile_lbl)
#grocery
grocery_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/grocery.png')
grocery_btn=Button(D,image=grocery_img,borderwidth=0,bg="white",command=grocery)
grocery_btn_win=my_canvas.create_window(200,200,anchor="nw",window=grocery_btn)
grocery_lbl=Label(D,text="Grocery",bg="white",fg="magenta2",font=font1)
grocery_lbl_win=my_canvas.create_window(200,330,anchor="nw",window=grocery_lbl)
#electronics
ele_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/electronic.png')
ele_btn=Button(D,image=ele_img,borderwidth=0,bg="white",command=electronics)
ele_btn_win=my_canvas.create_window(350,200,anchor="nw",window=ele_btn)
ele_lbl=Label(D,text="Electronics",font=font1,bg="white",fg="magenta2")
ele_lbl_win=my_canvas.create_window(350,330,anchor="nw",window=ele_lbl)
#baby
baby_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/baby.png')
baby_btn=Button(D,image=baby_img,borderwidth=0,bg="white",command=baby)
baby_btn_win=my_canvas.create_window(500,200,anchor="nw",window=baby_btn)
baby_lbl=Label(D,text="Baby & Toys",font=font1,bg="white",fg="magenta2")
baby_lbl_win=my_canvas.create_window(500,330,anchor="nw",window=baby_lbl)
#fashion
fashion_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/fashion.png')
fashion_btn=Button(D,image=fashion_img,borderwidth=0,bg="white",command=fashion)
fashion_btn_win=my_canvas.create_window(650,200,anchor="nw",window=fashion_btn)
fashion_lbl=Label(D,text="Fashion",font=font1,bg="white",fg="magenta2")
fashion_lbl_win=my_canvas.create_window(650,330,anchor="nw",window=fashion_lbl)
#beauty
beauty_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/beauty1.png')
beauty_btn=Button(D,image=beauty_img,borderwidth=0,bg="white",command=beauty)
beauty_btn_win=my_canvas.create_window(800,200,anchor="nw",window=beauty_btn)
beauty_lbl=Label(D,text="Beauty",font=font1,bg="white",fg="magenta2")
beauty_lbl_win=my_canvas.create_window(830,330,anchor="nw",window=beauty_lbl)
#sports
sports_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/sports.png')
sports_btn=Button(D,image=sports_img,borderwidth=0,bg="white",command=sports)
sports_btn_win=my_canvas.create_window(50,370,anchor="nw",window=sports_btn)
sports_lbl=Label(D,text="Sports",font=font1,bg="white",fg="magenta2")
spots_lbl_win=my_canvas.create_window(70,500,anchor="nw",window=sports_lbl)
#furniture
furn_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/furniture.png')
furn_btn=Button(D,image=furn_img,borderwidth=0,bg="white",command=furniture)
furn_btn_win=my_canvas.create_window(200,370,anchor="nw",window=furn_btn)
furn_lbl=Label(D,text="Furniture",font=font1,bg="white",fg="magenta2")
furn_lbl_win=my_canvas.create_window(200,500,anchor="nw",window=furn_lbl)
#plastic
plas_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/home.png')
plas_btn=Button(D,image=plas_img,borderwidth=0,bg="white",command=plastic)
plas_btn_win=my_canvas.create_window(350,370,anchor="nw",window=plas_btn)
plas_lbl=Label(D,text="Home",font=font1,bg="white",fg="magenta2")
plas_lbl_win=my_canvas.create_window(350,500,anchor="nw",window=plas_lbl)
#books
books_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/book_main.png')
books_btn=Button(D,image=books_img,borderwidth=0,bg="white",command=plastic)
books_btn_win=my_canvas.create_window(500,370,anchor="nw",window=books_btn)
books_lbl=Label(D,text="Books",font=font1,bg="white",fg="magenta2")
books_lbl_win=my_canvas.create_window(520,500,anchor="nw",window=books_lbl)
#travel
travel_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/travel.png')
travel_btn=Button(D,image=travel_img,borderwidth=0,bg="white",command=travel)
travel_btn_win=my_canvas.create_window(650,370,anchor="nw",window=travel_btn)
travel_lbl=Label(D,text="Travel",font=font1,bg="white",fg="magenta2")
travel_lbl_win=my_canvas.create_window(670,500,anchor="nw",window=travel_lbl)

veg_img=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/harvest.png')
veg_btn=Button(D,image=veg_img,borderwidth=0,bg="white",command=reckon)
veg_btn_win=my_canvas.create_window(800,370,anchor="nw",window=veg_btn)
veg_lbl=Label(D,text="Fruits & Veggies",font=font1,bg="white",fg="magenta2")
veg_lbl_win=my_canvas.create_window(820,500,anchor="nw",window=veg_lbl)

#more_btn=Button(D,text="more",borderwidth=0,bg="white",fg="blue",activebackground="grey",font=font1)
#more_win=my_canvas.create_window(700,95,anchor="nw",window=more_btn)





D.mainloop()