from tkinter import *


root=Tk()

root.geometry("750x500")
root.title("DNP")
root.configure(bg='gray25')


def hiithere():
    inp1=Entry(riteframe)
    inp1.config(text="source")
    inp1.grid(row=1,column=2,sticky=S)
    inp1 = Entry(riteframe)
    inp1.config(text="source")
    inp1.grid(row=1,column=1, sticky=S)



leftframe=Frame(root,bg="black",width=250, height=500)

leftframe.pack(side=LEFT)

riteframe=Frame(root)
riteframe.pack(side=RIGHT)

but1 = Button(leftframe, command=hiithere)
but1.config(text="scrren 1grab")
but1.grid(row=0,sticky=S)
but1= Button(leftframe,command=hiithere)
but1= Button(leftframe,width=20,height=2,command=quit)
but1.config(text="FTP ")
but1.grid(row=1,sticky=N)
but1= Button(leftframe,command=quit)
but1.config(text="scrren grab")
but1.grid(row=2,sticky=N)
but1= Button(leftframe,command=quit)
but1.config(text="scrren grab")
but1.grid(row=4,sticky=N)
but1= Button(leftframe,command=quit)
but1.config(text="scrren grab")
but1.grid(row=5,sticky=N)
but1= Button(leftframe,command=quit)
but1.config(text="scrren grab")
but1.grid(row=6,sticky=N)


root.mainloop()