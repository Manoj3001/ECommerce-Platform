from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import Font
import runpy
tamil=Tk()
tamil.title('ALM-Reckon - TAMIL')
tamil.geometry('2000x2000+0+0')
tamil.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
my_canvas=Canvas(tamil,width=2000,height=2000,bd=0,highlightthickness=0,bg='black')
my_canvas.pack(fill="both",expand=True)
font1=Font(family="Arial Black",size=15)
def add_cin():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/96.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Ramachandran (Vijay Sethupathi) first met Janaki (Trisha) when they were in school and \nhas been in love with her since.Seeing her again,22 years later at a school reunion, \nRam is overcome by feelings of nostalgia and longing for his childhood sweetheart."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="'96",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.6   2018   U   2 h 28 min    Romance",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Vijay Sethupathi, Adithya Bhaskar, Trisha Krishnan",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	main.state('zoomed')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)

	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin1():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/petta.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="In a bid to save Anwar, his best friend's son, hostel warden Kaali,stands up against \nthe local goons.However, everything goes haywire when Kaali is forced to face his past."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Petta",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.3   2019   U/A   2 h 51 min    Action/Drama",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Rajnikanth,Vijay Sethupathi,M. Sasikumar, Nawazuddin Siddiqui",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin2():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/nkp.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="A veteran lawyer comes out of retirement to help three women who \nhave been falsely implicated in a criminal case. As he represents \nthem in court, he faces powerful foes and patriarchal attitudes."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Nerkonda Paarvai",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 7.8   2019   U/A   2 h 37 min    Action/Crime/Drama",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Ajith Kumar, Shraddha Srinath,Vidhya Balan",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,250,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin3():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/karnan.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="A fearless village youth, must fight for the rights of the people of his village. \nThe people of the village belong to a marginalised community that has been \noppressed for decades, mainly by the dominant caste groups in the region aided \nby the government officials and the police who intend to keep them suppressed."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Karnan",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.3   2021   U/A   2 h 36 min    Action/Drama",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Dhanush, Lal, Rajisha Vijayan",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

def add_cin4():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/vish.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="An ambitious woman studying in the USA, marries a dance master.\nOn being suspicious of his behaviour, she hires a detective,who\n reveals his true identity and past"
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Vishwaroopam",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.1   2013   U/A   2 h 28 min    Action/Thriller",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:  Kamal Haasan,Pooja Kumar,Rahul Bose",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

def add_cin6():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/sd.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Sex, stigma and spirituality merge in these eccentric stories of an angsty teenager, an unfaithful \nwife and a transgender woman returning to her past."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Super Deluxe",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.4   2019   A   2 h 55 min    Comedy/Crime/Drama",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:Vijay Sethupathi,Fahadh Faasil,Samantha Ruth Prabhu",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin5():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ratchasn.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="A sub-inspector sets out in pursuit of a mysterious serial killer who targets teen school girls and \nmurders them brutally."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Ratchasan",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.5   2018   U/A   2 h 50 min    Action/Crime/Thriller",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:Vishnu Vishal, Amala Paul",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin7():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/vtv.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="A Hindu assistant director, Karthik, falls in love with Jessie, a Christian from a traditional family.\nThings change when Karthik becomes busy during a forty-day shoot in Goa."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Vinnaithaandi Varuvaayaa",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8   2010   U/A   2 h 37 min    Drama/Romance",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: T.R. Silambarasan, Trisha Krishnan",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin8():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/kai.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Dilli, a convicted criminal, is out on parole to meet his daughter. However, a drug bust sets him off \non a mission to save the life of police officers."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Kaithi",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 8.5   2019   U/A   2 h 30 min    Action/Thriller",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars:Karthi,Arjun Das,Narian,Dheena",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()
def add_cin9():
	tamil.destroy()
	main=Tk()
	main.geometry('2000x2000')
	main.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
	my_canvas=Canvas(main,width=2000,height=2000,bd=0,highlightthickness=0,bg="black")
	font1=Font(family="Arial Black",size=15)
	font2=Font(family="Arial Black",size=25)
	bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/untitled1.jpg"))
	my_canvas.pack(fill="both",expand=True)
	my_canvas.create_image(0,0,image=bg,anchor="nw")
	m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/sp.jpg"))
	my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
	l1=Label(main,text="Nedumaaran Rajangam sets out to make the common man fly and in the process \ntakes on the world's most capital intensive industry and several enemies who stand in his way."
		,bg="black",fg="deep pink",font=font1)
	_l1=my_canvas.create_window(250,200,anchor="w",window=l1)
	l2=Label(main,text="Soorarai Pottru",bg="black",fg="white",font=font2)
	_l2=my_canvas.create_window(250,50,anchor="nw",window=l2)
	l3=Label(main,text=" IMDb 9.1   2020   U/A   2 h 33 min    Action/Drama",bg="black",fg="grey",font=font1)
	_l3=my_canvas.create_window(250,100,anchor="nw",window=l3)
	xr_btn=Button(main,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn=my_canvas.create_window(250,300,anchor="nw",window=xr_btn)
	xr_btn1=Button(main,text="Download",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1)
	_xrbtn1=my_canvas.create_window(350,300,anchor="nw",window=xr_btn1)
	l4=Label(main,text="Stars: Suriya,Aparna Balamurali, Paresh Rawal",bg="black",fg="grey",font=font1)
	_l4=my_canvas.create_window(250,260,anchor="nw",window=l4)
	def back():
			main.destroy()
			runpy.run_path('tamil_reckon.pyw')
	back_btn=Button(main,text="Back To Home",bg="Deeppink2",fg="white",font="helvetica 10 italic bold",width=12,height=1,command=back)
	back_btn_win=my_canvas.create_window(450,300,anchor="nw",window=back_btn)
	main.state('zoomed')
	l5=Label(main,text="Customers Also Watch",bg="black",fg="deep pink",font=font1)
	_l5=my_canvas.create_window(25,340,anchor="nw",window=l5)
	main.mainloop()

l0=Label(tamil,text="Reckon",font=font1,bg="black",fg="Deeppink2")
_l0=my_canvas.create_window(25,15,anchor="nw",window=l0)
l1=Label(tamil,text="Recommended For You",font=font1,bg="black",fg="white")
_l1=my_canvas.create_window(110,15,anchor="nw",window=l1)
def close():
	tamil.destroy()
	runpy.run_path('reckon.pyw')
bt1=Button(tamil,text="Close",bg="deep pink",fg="white",font='helvetica 10 bold italic',height=1,width=10,command=close)
_bt1=my_canvas.create_window(1200,15,anchor="nw",window=bt1)

tamil.state('zoomed')
m1=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/96.jpg"))
my_image1=my_canvas.create_image(25,50,image=m1,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin)
_xrbtn=my_canvas.create_window(25,310,anchor="nw",window=xr_btn)

m2=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/petta.jpg"))
my_image1=my_canvas.create_image(275,50,image=m2,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin1)
_xrbtn=my_canvas.create_window(275,310,anchor="nw",window=xr_btn)

m3=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/nkp.jpg"))
my_image1=my_canvas.create_image(525,50,image=m3,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin2)
_xrbtn=my_canvas.create_window(525,310,anchor="nw",window=xr_btn)

m4=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/karnan.jpg"))
my_image1=my_canvas.create_image(775,50,image=m4,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin3)
_xrbtn=my_canvas.create_window(775,310,anchor="nw",window=xr_btn)

m5=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/vish.jpg"))
my_image1=my_canvas.create_image(1025,50,image=m5,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin4)
_xrbtn=my_canvas.create_window(1025,310,anchor="nw",window=xr_btn)

l2=Label(tamil,text="Critically-Acclaimed",fg="white",bg="black",font=font1)
_l2=my_canvas.create_window(25,350,anchor="nw",window=l2)

m6=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/ratchasn.jpg"))
my_image1=my_canvas.create_image(25,390,image=m6,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin5)
_xrbtn=my_canvas.create_window(25,650,anchor="nw",window=xr_btn)

m7=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/sd.jpg"))
my_image1=my_canvas.create_image(275,390,image=m7,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin6)
_xrbtn=my_canvas.create_window(275,650,anchor="nw",window=xr_btn)

m8=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/vtv.jpg"))
my_image1=my_canvas.create_image(525,390,image=m8,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin7)
_xrbtn=my_canvas.create_window(525,650,anchor="nw",window=xr_btn)

m9=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/kai.jpg"))
my_image1=my_canvas.create_image(775,390,image=m9,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin8)
_xrbtn=my_canvas.create_window(775,650,anchor="nw",window=xr_btn)

m10=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/pic/reckon/sp.jpg"))
my_image1=my_canvas.create_image(1025,390,image=m10,anchor="nw")
xr_btn=Button(tamil,text="Play Now",bg="deep pink",fg="white",font="helvetica 10 bold italic",width=10,height=1,command=add_cin9)
_xrbtn=my_canvas.create_window(1025,650,anchor="nw",window=xr_btn)
tamil.mainloop()