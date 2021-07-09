from tkinter import*
from math import *
import tkinter.messagebox

def btnclick(numbers):
	global operator
	operator+=str(numbers)
	text_input.set(operator)

def btnclear():
	global operator
	operator=""
	text_input.set("")

def btnequal():
	global operator
	global sump
	sump=str(eval(operator))
	text_input.set(sump)
	operator=""

def deleting():
	global operator
	length=len(text_display.get())
	text_display.delete(length-1,'end')
	operator=operator[:-1]

def answer():
	global sump
	global operator
	operator=sump

def entered1z(event):
	global btn1z
	btn1z.config(bg="black",fg="white")
def left1z(event):
	global btn1z
	btn1z.config(bg="white",fg="black")

def entered2z(event):
	global btn2z
	btn2z.config(bg="black",fg="white")
def left2z(event):
	global btn2z
	btn2z.config(bg="white",fg="black")

def entered3z(event):
	global btn13z
	btn3z.config(bg="black",fg="white")
def left3z(event):
	global btn3z
	btn3z.config(bg="white",fg="black")

def entered4z(event):
	global btn4z
	btn4z.config(bg="black",fg="white")
def left4z(event):
	global btn4z
	btn4z.config(bg="white",fg="black")

def entered5z(event):
	global btn5z
	btn5z.config(bg="black",fg="white")
def left5z(event):
	global btn5z
	btn5z.config(bg="white",fg="black")

def entered6z(event):
	global btn6z
	btn6z.config(bg="black",fg="white")
def left6z(event):
	global btn6z
	btn6z.config(bg="white",fg="black")

def entered7z(event):
	global btn7z
	btn7z.config(bg="black",fg="white")
def left7z(event):
	global btn7z
	btn7z.config(bg="white",fg="black")

def entered8z(event):
	global btn8z
	btn8z.config(bg="black",fg="white")
def left8z(event):
	global btn8z
	btn8z.config(bg="white",fg="black")

def entered9z(event):
	global btn9z
	btn9z.config(bg="black",fg="white")
def left9z(event):
	global btn9z
	btn9z.config(bg="white",fg="black")

def entered0z(event):
	global btn0z
	btn0z.config(bg="black",fg="white")
def left0z(event):
	global btn0z
	btn0z.config(bg="white",fg="black")

def enteredaddz(event):
	global addbuttz
	addbuttz.config(bg="black",fg="white")
def leftaddz(event):
	global addbuttz
	addbuttz.config(bg="white",fg="black")

def enteredmultz(event):
	global multbuttz
	multbuttz.config(bg="black",fg="white")
def leftmultz(event):
	global multbuttz
	multbuttz.config(bg="white",fg="black")

def enteredminusz(event):
	global minusbuttz
	minusbuttz.config(bg="black",fg="white")
def leftminusz(event):
	global minusbuttz
	minusbuttz.config(bg="white",fg="black")

def entereddivz(event):
	global divbuttz
	divbuttz.config(bg="black",fg="white")
def leftdivz(event):
	global divbuttz
	divbuttz.config(bg="white",fg="black")

def enteredcbz(event):
	global btnCBz
	btnCBz.config(bg="black",fg="white")
def leftcbz(event):
	global btnCBz
	btnCBz.config(bg="white",fg="black")

def enteredobz(event):
	global btnOBz
	btnOBz.config(bg="black",fg="white")
def leftobz(event):
	global btnOBz
	btnOBz.config(bg="white",fg="black")

def entereddotz(event):
	global btndotz
	btndotz.config(bg="black",fg="white")
def leftdotz(event):
	global btndotz
	btndotz.config(bg="white",fg="black")

def enteredbaz(event):
	global backinz
	backinz.config(bg="blue",fg="black")
def leftbaz(event):
	global backinz
	backinz.config(bg="white",fg="black")

def entered1(event):
	btn1.config(bg="black",fg="white")
def left1(event):
	btn1.config(bg="white",fg="black")

def entered2(event):
	btn2.config(bg="black",fg="white")
def left2(event):
	btn2.config(bg="white",fg="black")

def entered3(event):
	btn3.config(bg="black",fg="white")
def left3(event):
	btn3.config(bg="white",fg="black")

def entered4(event):
	btn4.config(bg="black",fg="white")
def left4(event):
	btn4.config(bg="white",fg="black")

def entered5(event):
	btn5.config(bg="black",fg="white")
def left5(event):
	btn5.config(bg="white",fg="black")

def entered6(event):
	btn6.config(bg="black",fg="white")
def left6(event):
	btn6.config(bg="white",fg="black")

def entered7(event):
	btn7.config(bg="black",fg="white")
def left7(event):
	btn7.config(bg="white",fg="black")

def entered8(event):
	btn8.config(bg="black",fg="white")
def left8(event):
	btn8.config(bg="white",fg="black")

def entered9(event):
	btn9.config(bg="black",fg="white")
def left9(event):
	btn9.config(bg="white",fg="black")

def entered0(event):
	btn0.config(bg="black",fg="white")
def left0(event):
	btn0.config(bg="white",fg="black")

def enteredadd(event):
	addbutt.config(bg="black",fg="white")
def leftadd(event):
	addbutt.config(bg="white",fg="black")

def enteredmult(event):
	multbutt.config(bg="black",fg="white")
def leftmult(event):
	multbutt.config(bg="white",fg="black")

def enteredminus(event):
	minusbutt.config(bg="black",fg="white")
def leftminus(event):
	minusbutt.config(bg="white",fg="black")

def entereddiv(event):
	divbutt.config(bg="black",fg="white")
def leftdiv(event):
	divbutt.config(bg="white",fg="black")

def enteredcb(event):
	btnCB.config(bg="black",fg="white")
def leftcb(event):
	btnCB.config(bg="white",fg="black")

def enteredob(event):
	btnOB.config(bg="black",fg="white")
def leftob(event):
	btnOB.config(bg="white",fg="black")

def entereddot(event):
	btndot.config(bg="black",fg="white")
def leftdot(event):
	btndot.config(bg="white",fg="black")

def enteredba(event):
	backin.config(bg="blue",fg="black")
def leftba(event):
	backin.config(bg="white",fg="black")

def simplecalci():
	btn7.grid_remove()
	btn8.grid_remove()
	btn9.grid_remove()
	btn0.grid_remove()
	btn1.grid_remove()
	btn2.grid_remove()
	btn3.grid_remove()
	btn4.grid_remove()
	btn5.grid_remove()
	btn6.grid_remove()
	btnCB.grid_remove()
	btnC.grid_remove()
	btnE.grid_remove()
	addbutt.grid_remove()
	minusbutt.grid_remove()
	multbutt.grid_remove()
	divbutt.grid_remove()
	btnOB.grid_remove()
	btndot.grid_remove()
	backin.grid_remove()
	btnsin.grid_remove()
	btncos.grid_remove()
	btnpi.grid_remove()
	backtan.grid_remove()
	backsqr.grid_remove()
	bacdot.grid_remove()
	butte.grid_remove()
	buttabs.grid_remove()
	buttlog.grid_remove()
	buttln.grid_remove()
	buttreci.grid_remove()
	buttepower.grid_remove()
	buttans.grid_remove()
	text_display.grid_remove()

	global btn1z
	global btnCBz
	global btnOBz
	global btn0z
	global btn2z
	global btn3z
	global btn4z
	global btn5z
	global btn6z
	global btn7z
	global btn8z
	global btn9z
	global addbuttz
	global multbuttz
	global minusbuttz
	global divbuttz
	global btnEz
	global btnCz
	global backinz
	global btndotz

	root.title("Simple Calculator")
	menu=Menu(root)
	root.config(menu=menu)
	submenu=Menu(menu)
	menu.add_cascade(label="Options",menu=submenu)
	submenu.add_command(label="Scientific Calculator",command=scientificcalci)
	submenu.add_separator()
	submenu.add_command(label="Exit",command=root.destroy)

	text_display1=Entry(root,width=27,bg="silver",textvariable=text_input,justify='right',font=('Times New Roman',20,'bold'),bd=30,insertwidth=4)
	text_display1.grid(row=0,column=0,columnspan=4)

	btn7z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="7",bg="white",command=lambda:btnclick(7))
	btn7z.grid(row=1,column=0)
	btn8z=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="8",bg="white",command=lambda:btnclick(8))
	btn8z.grid(row=1,column=1)
	btn9z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="9",bg="white",command=lambda:btnclick("9"))
	btn9z.grid(row=1,column=2)
	addbuttz=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="+",bg="white",command=lambda:btnclick("+"))
	addbuttz.grid(row=1,column=3)

	#====================================================================================================================================
	btn4z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="4",bg="white",command=lambda:btnclick(4))
	btn4z.grid(row=2,column=0)
	btn5z=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="5",bg="white",command=lambda:btnclick(5))
	btn5z.grid(row=2,column=1)
	btn6z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="6",bg="white",command=lambda:btnclick(6))
	btn6z.grid(row=2,column=2)
	minusbuttz=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="-",bg="white",command=lambda:btnclick("-"))
	minusbuttz.grid(row=2,column=3)
#==============================================================================================================================
	btn3z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),bg="white",text="3",command=lambda:btnclick(3))
	btn3z.grid(row=3,column=0)
	btn2z=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="2",bg="white",command=lambda:btnclick(2))
	btn2z.grid(row=3,column=1)
	btn1z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1",bg="white",command=lambda:btnclick(1))
	btn1z.grid(row=3,column=2)
	multbuttz=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="*",bg="white",command=lambda:btnclick("*"))
	multbuttz.grid(row=3,column=3)
#=============================================================================================================================
	btn0z=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="0",bg="white",command=lambda:btnclick(0))
	btn0z.grid(row=4,column=0)
	btnCz=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="C",bg="red",command=btnclear)
	btnCz.grid(row=4,column=1)
	btnEz=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="=",bg="green",command=btnequal)
	btnEz.grid(row=4,column=2)
	divbuttz=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="/",bg="white",command=lambda:btnclick("/"))
	divbuttz.grid(row=4,column=3)

#=====================================================================================================================================================

	btndotz=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=".",bg="white",command=lambda:btnclick(","))
	btndotz.grid(row=5,column=0)
	btnOBz=Button(root,padx=36,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="(",bg="white",command=lambda:btnclick("("))
	btnOBz.grid(row=5,column=1)
	btnCBz=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=")",bg="white",command=lambda:btnclick(")"))
	btnCBz.grid(row=5,column=2)
	backinz=Button(root,padx=16,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="Del",bg="white",command=deleting)
	backinz.grid(row=5,column=3)

	btn7z.bind("<Enter>",entered7z)
	btn7z.bind("<Leave>",left7z)
	btn8z.bind("<Enter>",entered8z)
	btn8z.bind("<Leave>",left8z)
	btn9z.bind("<Enter>",entered9z)
	btn9z.bind("<Leave>",left9z)	
	addbuttz.bind("<Enter>",enteredaddz)
	addbuttz.bind("<Leave>",leftaddz)

	btn3z.bind("<Enter>",entered3z)
	btn3z.bind("<Leave>",left3z)
	btn2z.bind("<Enter>",entered2z)
	btn2z.bind("<Leave>",left2z)
	btn1z.bind("<Enter>",entered1z)
	btn1z.bind("<Leave>",left1z)	
	multbuttz.bind("<Enter>",enteredmultz)
	multbuttz.bind("<Leave>",leftmultz)

	btn0z.bind("<Enter>",entered0z)
	btn0z.bind("<Leave>",left0z)
	divbuttz.bind("<Enter>",entereddivz)
	divbuttz.bind("<Leave>",leftdivz)

	btn4z.bind("<Enter>",entered4z)
	btn4z.bind("<Leave>",left4z)
	btn5z.bind("<Enter>",entered5z)
	btn5z.bind("<Leave>",left5z)
	btn6z.bind("<Enter>",entered6z)
	btn6z.bind("<Leave>",left6z)	
	minusbuttz.bind("<Enter>",enteredminusz)
	minusbuttz.bind("<Leave>",leftminusz)

	btndotz.bind("<Enter>",entereddotz)
	btndotz.bind("<Leave>",leftdotz)
	btnOBz.bind("<Enter>",enteredobz)
	btnOBz.bind("<Leave>",leftobz)
	btnCBz.bind("<Enter>",enteredcbz)
	btnCBz.bind("<Leave>",leftcbz)	
	backinz.bind("<Enter>",enteredbaz)
	backinz.bind("<Leave>",leftbaz)

	root.mainloop()

def scientificcalci():
	btn9.grid_remove()
	btn0.grid_remove()
	btn1.grid_remove()
	btn2.grid_remove()
	btn3.grid_remove()
	btn4.grid_remove()
	btn5.grid_remove()
	btn6.grid_remove()
	btnCB.grid_remove()
	btnC.grid_remove()
	btnE.grid_remove()
	addbutt.grid_remove()
	minusbutt.grid_remove()
	multbutt.grid_remove()
	divbutt.grid_remove()
	btnOB.grid_remove()
	btn7.grid_remove()
	btn8.grid_remove()
	
	btndot.grid_remove()
	backin.grid_remove()
	text_display.grid_remove()

	root.title("Scientific Calculator")
	menu=Menu(root)
	root.config(menu=menu)
	submenu=Menu(menu)
	menu.add_cascade(label="Options",menu=submenu)
	submenu.add_command(label="Simple Calculator",command=simplecalci)
	submenu.add_separator()
	submenu.add_command(label="Exit",command=root.destroy)

	text_display2=Entry(root,bg="silver",width=35,textvariable=text_input,justify='right',font=('Times New Roman',20,'bold'),bd=30,insertwidth=4)
	text_display2.grid(row=0,column=0,columnspan=10)

	btn7y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="7",bg="blue",command=lambda:btnclick(7))
	btn7y.grid(row=1,column=0)
	btn8y=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="8",bg="blue",command=lambda:btnclick(8))
	btn8y.grid(row=1,column=1)
	btn9y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="9",bg="blue",command=lambda:btnclick("9"))
	btn9y.grid(row=1,column=2)
	addbutty=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="+",bg="blue",command=lambda:btnclick("+"))
	addbutty.grid(row=1,column=3)

#====================================================================================================================================
	btn4y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="4",bg="cyan",command=lambda:btnclick(4))
	btn4y.grid(row=2,column=0)
	btn5y=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="5",bg="cyan",command=lambda:btnclick(5))
	btn5y.grid(row=2,column=1)
	btn6y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="6",bg="cyan",command=lambda:btnclick(6))
	btn6y.grid(row=2,column=2)
	minusbutty=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="-",bg="cyan",command=lambda:btnclick("-"))
	minusbutty.grid(row=2,column=3)
#==============================================================================================================================
	btn3y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),bg="aquamarine",text="3",command=lambda:btnclick(3))
	btn3y.grid(row=3,column=0)
	btn2y=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="2",bg="aquamarine",command=lambda:btnclick(2))
	btn2y.grid(row=3,column=1)
	btn1y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1",bg="aquamarine",command=lambda:btnclick(1))
	btn1y.grid(row=3,column=2)
	multbutty=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="*",bg="aquamarine",command=lambda:btnclick("*"))
	multbutty.grid(row=3,column=3)
#=============================================================================================================================
	btn0y=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="0",bg="steel blue",command=lambda:btnclick(0))
	btn0y.grid(row=4,column=0)
	btnCy=Button(root,padx=30,pady=33,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="C",bg="red",command=btnclear)
	btnCy.grid(row=1,column=5,rowspan=2)
	btnEy=Button(root,padx=32,pady=33,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="=",bg="gold",command=btnequal)
	btnEy.grid(row=3,column=5,rowspan=2)
	divbutty=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="/",bg="steel blue",command=lambda:btnclick("/"))
	divbutty.grid(row=4,column=3)

#=====================================================================================================================================================

	btndoty=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=",",bg="dodger blue",command=lambda:btnclick(","))
	btndoty.grid(row=5,column=0)
	btnOBy=Button(root,padx=36,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="(",bg="dodger blue",command=lambda:btnclick("("))
	btnOBy.grid(row=5,column=1)
	btnCBy=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=")",bg="dodger blue",command=lambda:btnclick(")"))
	btnCBy.grid(row=5,column=2)
	backiny=Button(root,padx=19,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="Del",bg="dodger blue",command=deleting)
	backiny.grid(row=5,column=5)

#============================================================================================================================

	btnsiny=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="sin",bg="medium spring green",command=lambda:btnclick("sin("))
	btnsiny.grid(row=6,column=0)
	btnpiy=Button(root,padx=26,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="pi",bg="steel blue",command=lambda:btnclick("pi"))
	btnpiy.grid(row=4,column=2)
	btncosy=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="cos",bg="medium spring green",command=lambda:btnclick("cos("))
	btncosy.grid(row=6,column=1)
	backtany=Button(root,padx=19,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="tan",bg="medium spring green",command=lambda:btnclick("tan("))
	backtany.grid(row=6,column=2)

#==================================================================================

	e=2.7182818284590
	backsqry=Button(root,padx=18,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="x^y",bg="light steel blue",command=lambda:btnclick("pow("))
	backsqry.grid(row=8,column=5)
	bacdoty=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=".",bg="dodger blue",command=lambda:btnclick("."))
	bacdoty.grid(row=5,column=3)
	buttey=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="e",bg="steel blue",command=lambda:btnclick("e"))
	buttey.grid(row=4,column=1)
	buttabsy=Button(root,padx=11,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="mod",bg="medium spring green",command=lambda:btnclick("abs("))
	buttabsy.grid(row=6,column=3)

#=======================================================================================================

	GJB=0.4342944819032
	buttlogy=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="log",bg="light steel blue",command=lambda:btnclick("GJB*log("))
	buttlogy.grid(row=8,column=2)
	buttlny=Button(root,padx=28,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="ln",bg="light steel blue",command=lambda:btnclick("log("))
	buttlny.grid(row=8,column=1)
	buttreciy=Button(root,padx=18,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1/x",bg="light steel blue",command=lambda:btnclick("1/"))
	buttreciy.grid(row=8,column=0)
	buttepowery=Button(root,padx=15,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="e^x",bg="light steel blue",command=lambda:btnclick("pow(e,"))
	buttepowery.grid(row=8,column=3)
	buttansy=Button(root,padx=12,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="ANS",bg="medium spring green",command=answer)
	buttansy.grid(row=6,column=5)

	root.mainloop()

root=Tk()
operator=""
sump=""
text_input=StringVar()

tkinter.messagebox.showinfo("Calculator","Make a choice")
answ=tkinter.messagebox.askquestion("Welcome to my Calculator","Do you want Scientific Calculator?")

if answ=='yes':
	root.title("Scientific Calculator")
	menu=Menu(root)
	root.config(menu=menu)
	submenu=Menu(menu)
	menu.add_cascade(label="Options",menu=submenu)
	submenu.add_command(label="Simple Calculator",command=simplecalci)
	submenu.add_separator()
	submenu.add_command(label="Exit",command=root.destroy)

	text_display=Entry(root,bg="silver",width=35,textvariable=text_input,justify='right',font=('Times New Roman',20,'bold'),bd=30,insertwidth=4)
	text_display.grid(row=0,column=0,columnspan=10)

	btn7=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="7",bg="blue",command=lambda:btnclick(7))
	btn7.grid(row=1,column=0)
	btn8=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="8",bg="blue",command=lambda:btnclick(8))
	btn8.grid(row=1,column=1)
	btn9=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="9",bg="blue",command=lambda:btnclick("9"))
	btn9.grid(row=1,column=2)
	addbutt=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="+",bg="blue",command=lambda:btnclick("+"))
	addbutt.grid(row=1,column=3)

#====================================================================================================================================
	btn4=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="4",bg="cyan",command=lambda:btnclick(4))
	btn4.grid(row=2,column=0)
	btn5=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="5",bg="cyan",command=lambda:btnclick(5))
	btn5.grid(row=2,column=1)
	btn6=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="6",bg="cyan",command=lambda:btnclick(6))
	btn6.grid(row=2,column=2)
	minusbutt=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="-",bg="cyan",command=lambda:btnclick("-"))
	minusbutt.grid(row=2,column=3)
#==============================================================================================================================
	btn3=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),bg="aquamarine",text="3",command=lambda:btnclick(3))
	btn3.grid(row=3,column=0)
	btn2=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="2",bg="aquamarine",command=lambda:btnclick(2))
	btn2.grid(row=3,column=1)
	btn1=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1",bg="aquamarine",command=lambda:btnclick(1))
	btn1.grid(row=3,column=2)
	multbutt=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="*",bg="aquamarine",command=lambda:btnclick("*"))
	multbutt.grid(row=3,column=3)
#=============================================================================================================================
	btn0=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="0",bg="steel blue",command=lambda:btnclick(0))
	btn0.grid(row=4,column=0)
	btnC=Button(root,padx=30,pady=33,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="C",bg="red",command=btnclear)
	btnC.grid(row=1,column=5,rowspan=2)
	btnE=Button(root,padx=32,pady=33,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="=",bg="gold",command=btnequal)
	btnE.grid(row=3,column=5,rowspan=2)
	divbutt=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="/",bg="steel blue",command=lambda:btnclick("/"))
	divbutt.grid(row=4,column=3)

#=====================================================================================================================================================

	btndot=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=",",bg="dodger blue",command=lambda:btnclick(","))
	btndot.grid(row=5,column=0)
	btnOB=Button(root,padx=36,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="(",bg="dodger blue",command=lambda:btnclick("("))
	btnOB.grid(row=5,column=1)
	btnCB=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=")",bg="dodger blue",command=lambda:btnclick(")"))
	btnCB.grid(row=5,column=2)
	backin=Button(root,padx=19,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="Del",bg="dodger blue",command=deleting)
	backin.grid(row=5,column=5)

#============================================================================================================================

	btnsin=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="sin",bg="medium spring green",command=lambda:btnclick("sin("))
	btnsin.grid(row=6,column=0)
	btnpi=Button(root,padx=26,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="pi",bg="steel blue",command=lambda:btnclick("pi"))
	btnpi.grid(row=4,column=2)
	btncos=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="cos",bg="medium spring green",command=lambda:btnclick("cos("))
	btncos.grid(row=6,column=1)
	backtan=Button(root,padx=19,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="tan",bg="medium spring green",command=lambda:btnclick("tan("))
	backtan.grid(row=6,column=2)

#==================================================================================

	e=2.7182818284590
	backsqr=Button(root,padx=18,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="x^y",bg="light steel blue",command=lambda:btnclick("pow("))
	backsqr.grid(row=8,column=5)
	bacdot=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=".",bg="dodger blue",command=lambda:btnclick("."))
	bacdot.grid(row=5,column=3)
	butte=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="e",bg="steel blue",command=lambda:btnclick("e"))
	butte.grid(row=4,column=1)
	buttabs=Button(root,padx=11,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="mod",bg="medium spring green",command=lambda:btnclick("abs("))
	buttabs.grid(row=6,column=3)

#=======================================================================================================
	GJB=0.4342944819032
	buttlog=Button(root,padx=20,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="log",bg="light steel blue",command=lambda:btnclick("GJB*log("))
	buttlog.grid(row=8,column=2)
	buttln=Button(root,padx=28,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="ln",bg="light steel blue",command=lambda:btnclick("log("))
	buttln.grid(row=8,column=1)
	buttreci=Button(root,padx=18,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1/x",bg="light steel blue",command=lambda:btnclick("1/"))
	buttreci.grid(row=8,column=0)
	buttepower=Button(root,padx=15,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="e^x",bg="light steel blue",command=lambda:btnclick("pow(e,"))
	buttepower.grid(row=8,column=3)
	buttans=Button(root,padx=12,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="ANS",bg="medium spring green",command=answer)
	buttans.grid(row=6,column=5)

	root.mainloop()

else:
	root.title("Simple Calculator")
	menu=Menu(root)
	root.config(menu=menu)
	submenu=Menu(menu)
	menu.add_cascade(label="Options",menu=submenu)
	submenu.add_command(label="Scientific Calculator",command=scientificcalci)
	submenu.add_separator()
	submenu.add_command(label="Exit",command=root.destroy)

	text_display=Entry(root,width=27,bg="silver",textvariable=text_input,justify='right',font=('Times New Roman',20,'bold'),bd=30,insertwidth=4)
	text_display.grid(row=0,column=0,columnspan=4)

	btn7=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="7",bg="white",command=lambda:btnclick(7))
	btn7.grid(row=1,column=0)
	btn8=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="8",bg="white",command=lambda:btnclick(8))
	btn8.grid(row=1,column=1)
	btn9=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="9",bg="white",command=lambda:btnclick("9"))
	btn9.grid(row=1,column=2)
	addbutt=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="+",bg="white",command=lambda:btnclick("+"))
	addbutt.grid(row=1,column=3)

	#====================================================================================================================================
	btn4=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="4",bg="white",command=lambda:btnclick(4))
	btn4.grid(row=2,column=0)
	btn5=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="5",bg="white",command=lambda:btnclick(5))
	btn5.grid(row=2,column=1)
	btn6=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="6",bg="white",command=lambda:btnclick(6))
	btn6.grid(row=2,column=2)
	minusbutt=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="-",bg="white",command=lambda:btnclick("-"))
	minusbutt.grid(row=2,column=3)
#==============================================================================================================================
	btn3=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),bg="white",text="3",command=lambda:btnclick(3))
	btn3.grid(row=3,column=0)
	btn2=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="2",bg="white",command=lambda:btnclick(2))
	btn2.grid(row=3,column=1)
	btn1=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="1",bg="white",command=lambda:btnclick(1))
	btn1.grid(row=3,column=2)
	multbutt=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="*",bg="white",command=lambda:btnclick("*"))
	multbutt.grid(row=3,column=3)
#=============================================================================================================================
	btn0=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="0",bg="white",command=lambda:btnclick(0))
	btn0.grid(row=4,column=0)
	btnC=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="C",bg="red",command=btnclear)
	btnC.grid(row=4,column=1)
	btnE=Button(root,padx=30,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="=",bg="green",command=btnequal)
	btnE.grid(row=4,column=2)
	divbutt=Button(root,padx=32,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="/",bg="white",command=lambda:btnclick("/"))
	divbutt.grid(row=4,column=3)

#=====================================================================================================================================================

	btndot=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=".",bg="white",command=lambda:btnclick(","))
	btndot.grid(row=5,column=0)
	btnOB=Button(root,padx=36,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="(",bg="white",command=lambda:btnclick("("))
	btnOB.grid(row=5,column=1)
	btnCB=Button(root,padx=34,bd=8,fg="black",font=('Times New Roman',20,'bold'),text=")",bg="white",command=lambda:btnclick(")"))
	btnCB.grid(row=5,column=2)
	backin=Button(root,padx=16,bd=8,fg="black",font=('Times New Roman',20,'bold'),text="Del",bg="white",command=deleting)
	backin.grid(row=5,column=3)

	btn7.bind("<Enter>",entered7)
	btn7.bind("<Leave>",left7)
	btn8.bind("<Enter>",entered8)
	btn8.bind("<Leave>",left8)
	btn9.bind("<Enter>",entered9)
	btn9.bind("<Leave>",left9)	
	addbutt.bind("<Enter>",enteredadd)
	addbutt.bind("<Leave>",leftadd)

	btn3.bind("<Enter>",entered3)
	btn3.bind("<Leave>",left3)
	btn2.bind("<Enter>",entered2)
	btn2.bind("<Leave>",left2)
	btn1.bind("<Enter>",entered1)
	btn1.bind("<Leave>",left1)	
	multbutt.bind("<Enter>",enteredmult)
	multbutt.bind("<Leave>",leftmult)

	btn0.bind("<Enter>",entered0)
	btn0.bind("<Leave>",left0)
	divbutt.bind("<Enter>",entereddiv)
	divbutt.bind("<Leave>",leftdiv)

	btn4.bind("<Enter>",entered4)
	btn4.bind("<Leave>",left4)
	btn5.bind("<Enter>",entered5)
	btn5.bind("<Leave>",left5)
	btn6.bind("<Enter>",entered6)
	btn6.bind("<Leave>",left6)	
	minusbutt.bind("<Enter>",enteredminus)
	minusbutt.bind("<Leave>",leftminus)

	btndot.bind("<Enter>",entereddot)
	btndot.bind("<Leave>",leftdot)
	btnOB.bind("<Enter>",enteredob)
	btnOB.bind("<Leave>",leftob)
	btnCB.bind("<Enter>",enteredcb)
	btnCB.bind("<Leave>",leftcb)	
	backin.bind("<Enter>",enteredba)
	backin.bind("<Leave>",leftba)

	root.mainloop()


