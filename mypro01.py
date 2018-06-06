#Importing

from tkinter import *

import tkinter.filedialog

#Assumptions

root=Tk()

root.geometry("750x500")
root.title("DNP")
root.configure(bg='gray25')

#FN Definitions For Left Frames

def files():
    file = tkinter.filedialog.askopenfilename()
    show.set(file)
show = StringVar(None)





def hiithere():
    inp1 = Entry(riteframe, textvariable=show)

    inp1.grid(row=1, column=1, sticky=S)

    inp1 = Entry(riteframe)
    inp1.config(text="source")
    inp1.grid(row=1,column=2, sticky=S)
    but1=Button(riteframe, command=files)
    but1.config(text="source")
    but1.grid(row=2,column=1)



def hiither():
    inp1=Entry(riteframe)
    inp1.config(text="source")
    inp1.grid(row=2,column=2,sticky=S)
    inp1 = Entry(riteframe)
    inp1.config(text="source")
    inp1.grid(row=2,column=1, sticky=S)


#Frames Creation

leftframe=Frame(root,bg="black",width=250, height=500)

leftframe.pack(side=LEFT)

riteframe=Frame(root)
riteframe.pack(side=RIGHT)

#Left Frame Arrangements

but1 = Button(leftframe,width=20,height=2, command=hiithere)
but1.config(text="FileTransfer")
but1.grid(row=0,sticky=S)
but1= Button(leftframe,command=hiithere)
but1= Button(leftframe,width=20,height=2,command=hiither)
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

#End Card
root.mainloop()
