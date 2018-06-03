##
from tkinter import *
import os
import tkinter.messagebox


#import subprocess

root=Tk()


#### for multi line comment use (''' texts ''')


root.title("A&A")
root.geometry("750x500")
root.configure(background='grey')
pic=PhotoImage(file="img.png")
lab=Label(root,image=pic)
lab.pack(fill=X)

det={'Alls':'paswd', 'bob':'bob'}


##opening the new script not creating window in tkinter

def create_window():
    #window = Toplevel(root,)
    os.system("python3 mypro.py")
    #subprocess.Popen("script2.py 1", shell=True)





##username and pass
usnm=Label(root,text="Name",width=5,height=2)
usnm.config(font=( 20))
pswd=Label(root,text="Passwd",width=10,height=5)
pswd.config()
inp1=Entry(root)
inp1.config(show="*")
inp2=Entry(root)
inp2.config(show="*")
usnm.pack(fill=X)
inp1.pack()
pswd.pack(fill=X)
inp2.pack()
inp1.bind("<A><B><C>",create_window)

def doNothing(event):

    flag = 0
    for inp1 in det:
        #print(inp1.get())
        #print(Entry)
        if det[inp1]==inp2.get():
            flag = 1
           # print("hello")
    if flag == 1:
        create_window()
        var = event
    else:
        tkinter.messagebox.showwarning('Die You Bitch', 'duck off man username or password is wrong ')

def helper(event):
    doNothing("duck")

butt2 = Button(root,fg="blue",bg="white",command=helper )
butt2.config(text='loganathan',height=48)
butt2.pack(fill=X)
butt2.bind("<Return>",helper)

root.mainloop()