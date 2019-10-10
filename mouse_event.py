from tkinter import *
w=Tk()
def show(event):
    print("Left Button Clicked\n",end="")
    s1.set("Left Button Clicked")
def show1(event):
    print("Right Button Clicked\n",end="")
    s1.set("Right Button Clicked")

s1=StringVar()
s1.set("Button Not Clicked")
l5=Label(w,text="Click The Mouse Button(Left/Right) Here",font=("arial",20,"bold"))
l6=Label(w,textvariable=s1,font=("arial",20,"bold"))
l5.grid(row=1,column=1)
l6.grid(row =2,column=1)
w.bind('<Button-1>',show)
w.bind('<Button-3>',show1)
w.mainloop()
