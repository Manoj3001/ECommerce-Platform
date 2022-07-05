from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import runpy
from tkinter.font import Font
reckon=Tk()
reckon.geometry('2000x2000+0+0')
reckon.title('ALM-Reckon')
reckon.config(bg='black')
reckon.state('zoomed')
reckon.iconbitmap(r'\Users\i5\Desktop\PYTHON PRGS\E Commerce project\reckon.ico')
bg=ImageTk.PhotoImage(Image.open("C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/coverreckon4.jpg"))
my_canvas=Canvas(reckon,width=2000,height=2000,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")
font1=Font(family="Arial Black",size=15)
def tamil():
	reckon.destroy()
	runpy.run_path('tamil_reckon.pyw')
def telugu():
	reckon.destroy()
	runpy.run_path('telugu_reckon.pyw')
def malayalam():
	reckon.destroy()
	runpy.run_path('mala_reckon.pyw')
def english():
	reckon.destroy()
	runpy.run_path('english_reckon.pyw')
def  hindi():
	reckon.destroy()
	runpy.run_path('hindi_reckon.pyw')
def ot():
	reckon.destroy()
	runpy.run_path('ot_reckon.pyw')
l1=Label(reckon,text="Reckon Originals",bg="black",fg="white",font=font1)
_l1=my_canvas.create_window(20,500,anchor="nw",window=l1)

b1=Button(reckon,text="Tamil\nதமிழ்",bg="black",fg="yellow",font=font1,width=10,command=tamil)
_b1=my_canvas.create_window(100,400,anchor="nw",window=b1)

b2=Button(reckon,text="Telugu\nతెలుగు",bg="black",fg="blue",font=font1,width=10,command=telugu)
_b2=my_canvas.create_window(300,400,anchor="nw",window=b2)

b3=Button(reckon,text="Malayalam\nമലയാളം",bg="black",fg="green",font=font1,width=10,command=malayalam)
_b3=my_canvas.create_window(500,400,anchor="nw",window=b3)

b4=Button(reckon,text="English",bg="black",fg="red",font=font1,height=2,width=10,command=english)
_b4=my_canvas.create_window(700,400,anchor="nw",window=b4)

b5=Button(reckon,text="Hindi\nहिंदी",bg="black",fg="orange",font=font1,width=10,command=hindi)
_b5=my_canvas.create_window(900,400,anchor="nw",window=b5)

b7=Button(reckon,text="Other\nLanguages",bg="black",fg="pink",font=font1,width=10,command=ot)
_b7=my_canvas.create_window(1100,400,anchor="nw",window=b7)
def veg():
	reckon.destroy()
	runpy.run_path('english_reckon.pyw')

watch=PhotoImage(file='C:/Users/i5/Desktop/PYTHON PRGS/E Commerce project/watchnow.png')
vege_btn=Button(reckon,image=watch,borderwidth=0,bg="white",command=veg)
vege_btn_win=my_canvas.create_window(150,300,anchor="nw",window=vege_btn)


#log_out_btn=Button(D,text="HOME",borderwidth=0,bg="black",fg="white",font="helvetica 15 italic bold",command=log_out)
#log_out_btn_win=my_canvas.create_window(1000,60,anchor="nw",window=log_out_btn)


reckon.mainloop()