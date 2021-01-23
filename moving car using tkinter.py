
from tkinter import *

root=Tk()


canvas=Canvas(root,height=800,width=1000)



rec=canvas.create_rectangle(40,100,320,200,fill="red",tags="car",width=3)

#rear glass
line=canvas.create_line(100,40,200,40,tags="car",width=3)
l1=canvas.create_line(100,40,80,100,tags="car",width=3)
#fontglass
l1=canvas.create_line(200,40,200,100,tags="car",width=3)
l1=canvas.create_line(200,40,280,100,tags="car",smooth="true",width="3")

#reartyre
c1=canvas.create_oval(50,160,130,240,tags="car",fill="black")
c1=canvas.create_oval(70,180,110,220,tags="car",fill="grey")
#fonttyre
c1=canvas.create_oval(250,160,330,240,tags="car",fill="black")
c1=canvas.create_oval(270,180,310,220,tags="car",fill="grey")

c1=canvas.create_oval(319,100,340,120,tags="car",fill="yellow")

def movement():
	canvas.move("car",6,5)
	canvas.after(100,movement)

canvas.pack()
movement()
mainloop()
