import os
import platform
import tkinter
from tkinter import *

n=platform.node()
o=platform.system()

root=tkinter.Tk()
root.geometry("260x220")
root.resizable(False, False)
root.title(n)
root.config(background='#ffe5cc')



def w():

	l = Label(root, text=o,
					padx=50,
					pady=10,
					font="League 25",
					fg="#990000",
					bg="#ffe5cc")
	l.grid(row=1,
					column=1,
					pady=10,
					padx=5)
    
	
	D = Button(root,
						text="SHUT DOWN",
						command=shutdown,
						width=20,
                        padx=4,pady=6,
						bg="#990000",
                        fg="#fffdd0",
						relief=GROOVE,
						font="Ray-Ban")
	D.grid(row=2,
					column=1,
					pady=10,
					padx=30)
	D1 = Button(root,
						text="RESTART",
						command=restart,
                        padx=4,pady=6,
						width=20,
						bg="#990000",
                        fg="#fffdd0",
						relief=GROOVE,
						font="Ray-Ban")
	D1.grid(row=3,
					column=1,
					pady=10,
					padx=30)
	


def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")

w()
root.mainloop()