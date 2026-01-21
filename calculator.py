import tkinter as bold
from tkinter import *
window = Tk()
window.config(bg="black")
search = Entry(window,width=40
,borderwidth=40,font=("Arial",20))
search.place(x=0,y=0)
def click(a):
	result = search.get()
	search.delete(0,END)
	search.insert(0,str(result)+str(a))
	
	
b = Button(window,text="1",borderwidth=8,width=8,height=2,command=lambda:click(1))
b.place(x=3,y=500)
	
b = Button(window,text="2",borderwidth=8,width=8,height=2,command=lambda:click(2))
b.place(x=350,y=500)


	
b = Button(window,text="3",borderwidth=8,width=8,height=2,command=lambda:click(3))
b.place(x=700,y=500)


	
b = Button(window,text="4",borderwidth=8,width=8,height=2,command=lambda:click(4))
b.place(x=3,y=800)


	
b = Button(window,text="5",borderwidth=8,width=8,height=2,command=lambda:click(5))
b.place(x=350,y=800)


	
b = Button(window,text="6",borderwidth=8,width=8,height=2,command=lambda:click(6))
b.place(x=700,y=800)


	
b = Button(window,text="7",borderwidth=8,width=8,height=2,command=lambda:click(7))
b.place(x=3,y=1100)


	
b = Button(window,text="8",borderwidth=8,width=8,height=2,command=lambda:click(8))
b.place(x=350,y=1100)


	
b = Button(window,text="9",width=8,borderwidth=8,height=2,command=lambda:click(9))
b.place(x=700,y=1100)


def add():
	k = search.get()
	global sm
	sm = "addition"
	global i
	i = int(k)
	search.delete(0,END)
	
b = Button(window,text="+",width=8,borderwidth=8,height=2,command=add)
b.place(x=3,y=1400)

	
b = Button(window,text="0",width=8,borderwidth=8,height=2,command=lambda:click(0))
b.place(x=350,y=1400)

def subract():
	k = search.get()
	global sm
	sm = "subraction"
	global i
	i = int(k)
	search.delete(0,END)
	
b = Button(window,text="-",width=8,borderwidth=8,height=2,command=subract)
b.place(x=700,y=1400)

def multiply():
	k = search.get()
	global sm
	sm = "multiplication"
	global i
	i = int(k)
	search.delete(0,END)
	
	
b = Button(window,text="*",width=8,borderwidth=8,height=2,command=multiply)
b.place(x=3,y=1700)

def divide():
	k = search.get()
	global sm
	sm = "division"
	global i
	i = int(k)
	search.delete(0,END)
	
	
b = Button(window,text="/",width=8,borderwidth=8,height=2,command=divide)
b.place(x=350,y=1700)


def equal():
	n1 = search.get()
	n2 = int(n1)
	search.delete(0,END)
	

	
	if sm == "addition":
		search.insert(0,i + n2)
	elif sm == "subraction":
		search.insert(0,i - n2)
	elif sm == "multiplication":
		search.insert(0,i * n2)
	elif sm == "division":
		search.insert(0,i / n2)
	
	
def clear():
	search.delete(0,END)


b = Button(window,text="C",width=8,borderwidth=8,height=2,command=clear)
b.place(x=700,y=1700)

b = Button(window,text="=",width=8,borderwidth=8,height=2,command=equal)
b.place(x=350,y=2000)









	

window.mainloop()