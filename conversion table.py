from tkinter import *
root = Tk()

a = DoubleVar()
b = DoubleVar()
c= DoubleVar()
d = DoubleVar()

gram1 = DoubleVar()
kilo1 = DoubleVar()
tonne1 = DoubleVar()
celsius1 = DoubleVar()

def gramtoounce():
	a.set((gram1.get())*0.03527)
def kilotopound():
	b.set((kilo1.get())*2.204)
def tonnetostone():
	c.set((tonne1.get())*2.204)
def celtofar():
	d.set((celsius1.get()*1.8)+32)



gram = Label(root,text="enter gram")
g_value = Entry(root,textvariable=gram1)
g_buton = Button(root,text="convert",command=gramtoounce)
o_label = Entry(root,textvariable=a)
a.set(" ")

kilo_label = Label(root,text="enter kilo")
k_value = Entry(root, textvariable =kilo1)
k_buton = Button(root,text="convert",command=kilotopound)
p_label = Entry(root,textvariable=b)
b.set(" ")

tonne_label = Label(root,text="Enter tonne")
t_value = Entry(root,textvariable=tonne1)
t_buton = Button(root,text="convert",command=tonnetostone)
s_label = Entry(root,textvariable=c)
c.set(" ")

celsius_label = Label(root,text="enter celsius")
v_value = Entry(root,textvariable=celsius1)
c_buton = Button(root,text="convert",command=celtofar)
f_label = Entry(root,textvariable=d)
d.set(" ")

gram.grid(row=1,column=0)
g_value.grid(row=1,column=1)
g_buton.grid(row=1,column=2)
o_label.grid(row=1,column=3)

kilo_label.grid(row=2,column=0)
k_value.grid(row=2,column=1)
k_buton.grid(row=2,column=2)
p_label.grid(row=2,column=3)

tonne_label.grid(row=3,column=0)
t_value.grid(row=3,column=1)
t_buton.grid(row=3,column=2)
s_label.grid(row=3,column=3)

celsius_label.grid(row=4,column=0)
v_value.grid(row=4,column=1)
c_buton.grid(row=4,column=2)
f_label.grid(row=4,column=3)

root.mainloop()
