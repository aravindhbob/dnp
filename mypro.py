
##importing
from tkinter import *
import tkinter.messagebox



#root.destroy
##fn definition
def hello():
    print("hii there")

##MESSAGEBOX

#mess1= tkinter.messagebox.showwarning('header ' ,' message ')





##assumption
root = Tk()

quit("python3 mypro1.py")

##ADD PICS
pic=PhotoImage(file="folder_red.png")
pic2=PhotoImage(file="case.png")


#title
root.title("A&A")

# size of window
root.geometry("750x500")
root.configure(background='bisque2')


##add frames
top = Frame(root)

top.pack(side =TOP, fill=X)

down = Frame(root)
down.pack(side=BOTTOM,fill=X)

##the toolbar

tool= Frame(top, bg="bisque2")
but1= Button(tool,command=quit,bg='bisque2',fg='bisque3')
but1.config(image=pic,width="48",height="48")

but1.pack(side=LEFT,padx=2,pady=2)
#tool.pack(side=TOP, fill=X)

but1= Button(tool,command=quit,bg='bisque2',fg='bisque3')
but1.config(image=pic,width="48",height="48")
but1.pack(side=LEFT,padx=2,pady=2)
tool.pack(side=TOP, fill=X)



'''#add button bottom frame
butt2 = Button(down,fg = "white",bg="bisque2", command=exit)
butt2.config(image=pic,anchor="w")
butt2.pack(fill=X)

##add butt on top frame
butt1 = Button(top,fg = "bisque2",bg="bisque2", command=exit)
butt1.config(image=pic2,anchor="w")
butt1.pack(side=LEFT)

butt2 = Button(top,fg = "blue",bg="white", command=exit)
butt2.config(image=pic)
butt2.pack(side=LEFT)'''





#menu1
menu1 = Menu(root)
root.config(menu=menu1)

##submenu with separator
subMenu1 = Menu(menu1)
menu1.add_cascade(label="M1", menu=subMenu1)
subMenu1.add_command(label="sub1", command=hello)
subMenu1.add_command(label="sub2", command=hello)
subMenu1.add_separator()
subMenu1.add_command(label="sub3", command=hello)
subMenu1.add_command(label="exit", command=quit)

##menu2
menu2 = Menu(menu1)


##submenu

menu1.add_cascade(label="M2",menu=menu2)
menu2.add_command(label="sub1",command=hello)
menu2.add_command(label="sub2",command=hello)


##staatus bar
stat= Label(down, text="app online",bd=1,relief=SUNKEN,anchor=W)
stat.pack(side=BOTTOM,fill=X)


##pics upload







root.mainloop()








