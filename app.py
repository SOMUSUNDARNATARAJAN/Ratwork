from tkinter import *

window=Tk()

def add():
    k=float(n1.get())+float(n2.get())
    t1.delete("1.0",END)
    t1.insert(END,k)

l1=Label(window,text="Enter a number :",bg='orange',height=1,width=40)
l1.grid(row=0,column=1)
n1=StringVar()
n2=StringVar()
e1=Entry(window,textvariable=n1,bg="cyan")
e1.grid(row=1,column=1)
e2=Entry(window,textvariable=n2,bg="cyan")
e2.grid(row=2,column=1)
t1=Text(window,height=1,width=30,bg="cyan")
t1.grid(row=4,column=1)
b1=Button(window,text='ADD',bg="yellow",height=1,width=20,command=add)
b1.grid(row=3,column=1)

window.mainloop()