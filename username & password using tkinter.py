import tkinter
from tkinter import*
from tkinter import messagebox
top=tkinter.Tk(className="LOGIN")
name="ashish"
pas="rvce"

user=StringVar()
pwd=StringVar()

def login():
	if(user.get()==name and pwd.get()==pas):
		messagebox.showinfo("alert","login Done")
	elif(user.get()=='' and pwd.get()==''):
		messagebox.showinfo("alert","Fields can't be empty !")
	else:
		messagebox.showinfo("alert","Wrong passwd or user name")

def clear():
	user.delete(0,END)
	pwd.delete(0,END)
	
l1=Label(top,text="USER NAME")
user=Entry(top,textvariable=user)
l2=Label(top,text="PASSWORD")
pwd=Entry(top,textvariable=pwd,show="*")
b1=Button(top,text="SUBMIT",command=login)
b2=Button(top,text="CLEAR",command=clear)

l1.pack()
user.pack()
l2.pack()
pwd.pack()
b1.pack()
b2.pack()

top.mainloop()