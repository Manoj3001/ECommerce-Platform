from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import Font
import runpy
ot=Tk()
ot.title('ALM-Reckon - Other Languages')
ot.geometry('2000x2000+0+0')
ot.state('zoomed')
ot.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
my_canvas=Canvas(ot,width=2000,height=2000,bd=0,highlightthickness=0,bg='black')
my_canvas.pack(fill="both",expand=True)
font1=Font(family="Arial Black",size=15)
def add_cin():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/mom.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="In a small Korean province in 1986, two detectives struggle with the case of \nmultiple young women being found raped and murdered by an unknown culprit."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Memories Of Murder",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.1   2003   U/A   2 h 12 min    Crime/Drama/Mystery   Korean",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Kang-ho Song, Kim Sang-kyung, Roe-ha Kim",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin1():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/fy.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Memories in a bowl of steaming noodles, a fading beauty finding her way \nand a bittersweet first love -- all in these stories of city life in China."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Flavors Of Youth",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 6.6   2018   U   1 h 14 min    Animation/Drama/Romance    Japanese",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Taito Ban,Mariya Ise,Minako Kotobuki",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin2():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/poppy hill.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="A  group of Yokohama teens look to save their school's clubhouse \nfrom the wrecking ball in preparations for the 1964 Tokyo Olympics."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="From Up On Poppy Hill",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.4   2011   U   1 h 31 min    Animation/Family/Drama   Japanese",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:   Sarah Bolger, Chris Noth, Anton Yelchin",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin3():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/kgf.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="In the 1970s, a fierce rebel rises against brutal oppression and \nbecomes the symbol of hope to legions of downtrodden people."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="K.G.F - Chapter 1",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.2   2018   U/A   2 h 36 min    Action/Drama    Kannada",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:   Yash, Srinidhi Shetty, Ramachandra Raju",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

def add_cin4():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/veronica.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Madrid, 1991. A teen girl finds herself besieged by an evil \nsupernatural force after she played Ouija with two classmates."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Veronica",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 6.6   2017   A   1 h 46 min    Horror/Supernatural Thriller    Spanish",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Sandra Escacena, Bruna Gonz??lez, Claudia Placer",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

def add_cin6():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/para.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Greed and class discrimination threaten the newly formed symbiotic \nrelationship between the wealthy Park family and the destitute Kim clan."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Parasite",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.6   2019   U/A   2 h 12 min    Comedy/Thriller/Drama    Korean",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Kang-ho Song, Sun-kyun Lee, Yeo-jeong Cho",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin5():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ano.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Four high school teachers consume alcohol on a daily basis \nto see how it affects their social and professional lives."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Alcootest or Another Round",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.8   2021   U/A   1 h 57 min    Drama/Comedy   Danish/English",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Mads Mikkelsen, Thomas Bo Larsen, Magnus Millang",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin7():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/cc.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Daniel experiences a spiritual transformation in a detention center. \nAlthough his criminal record prevents him from applying to the seminary, \nhe has no intention of giving up his dream and decides to minister a small-town parish."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Corpus Christi / Boze Cialo ",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.7   2019   U/A   1 h 55 min    Drama   Polish/English" ,bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Bartosz Bielenia, Aleksandra Konieczna, Eliza Rycembel",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin8():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ut.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man \nfrom the projects to be his caregiver."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Intouchables",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.5   2011   U   1 h 52 min    Comedy/Drama   French",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Fran??ois Cluzet, Omar Sy, Anne Le Ny",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin9():
	ot.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ot.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Based on real events, this crime action film depicts a Seoul detective's attempts to\n keep peace while two Chinese-Korean gangs battle over turf in the neighborhood."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="The Outlaws",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.2   2017   U/A   2 h 1 min    Action/Crime     Korean",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Ma Dong-seok, Yoon Kyesang, Jo Jae-yoon",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('ot_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

l0=Label(ot,text="Reckon",font=font1,bg="black",fg="Deeppink2")
_l0=my_canvas.create_window(25,15,anchor="nw",window=l0)
l1=Label(ot,text="Recommended For You",font=font1,bg="black",fg="white")
_l1=my_canvas.create_window(110,15,anchor="nw",window=l1)
def close():
	ot.destroy()
	runpy.run_path('reckon.pyw')
bt1=Button(ot,text="Close",bg="deep pink",fg="white",font='helvetica 10 bold italic',height=1,width=10,command=close)
_bt1=my_canvas.create_window(1200,15,anchor="nw",window=bt1)

m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/mom.jpg"))
my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin)
_xrbtn=my_canvas.create_window(25,310,anchor="nw",window=xr_btn)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/fy.jpg"))
my_image1=my_canvas.create_image(275,50,image=m2,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin1)
_xrbtn=my_canvas.create_window(275,310,anchor="nw",window=xr_btn)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/poppy hill.jpg"))
my_image1=my_canvas.create_image(525,50,image=m3,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin2)
_xrbtn=my_canvas.create_window(525,310,anchor="nw",window=xr_btn)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/kgf.jpg"))
my_image1=my_canvas.create_image(775,50,image=m4,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin3)
_xrbtn=my_canvas.create_window(775,310,anchor="nw",window=xr_btn)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/veronica.jpg"))
my_image1=my_canvas.create_image(1025,50,image=m5,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin4)
_xrbtn=my_canvas.create_window(1025,310,anchor="nw",window=xr_btn)

l2=Label(ot,text="Critically-Acclaimed",fg="white",bg="black",font=font1)
_l2=my_canvas.create_window(25,350,anchor="nw",window=l2)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ano.jpg"))
my_image1=my_canvas.create_image(25,390,image=m6,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin5)
_xrbtn=my_canvas.create_window(25,650,anchor="nw",window=xr_btn)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/para.jpg"))
my_image1=my_canvas.create_image(275,390,image=m7,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin6)
_xrbtn=my_canvas.create_window(275,650,anchor="nw",window=xr_btn)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/cc.jpg"))
my_image1=my_canvas.create_image(525,390,image=m8,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin7)
_xrbtn=my_canvas.create_window(525,650,anchor="nw",window=xr_btn)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ut.jpg"))
my_image1=my_canvas.create_image(775,390,image=m9,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin8)
_xrbtn=my_canvas.create_window(775,650,anchor="nw",window=xr_btn)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ot.jpg"))
my_image1=my_canvas.create_image(1025,390,image=m10,anchor="nw")
xr_btn=Button(ot,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin9)
_xrbtn=my_canvas.create_window(1025,650,anchor="nw",window=xr_btn)
ot.mainloop()